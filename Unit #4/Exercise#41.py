# -*- coding: utf-8 -*-
''' Realizar lo siguiente:
    1. Comentar los atributos de cada una de las clases.
    2. Agregar atributos a cada una de las clases (con base en sus diagramas de clase). Estos
    atributos tienen que recibir las mismas acciones que los demás.
    3. Guardar los datos en un archivo .txt '''

class Alumno:
    def __init__(self, nombre: str, numero_control: str, email: str, carrera=None):
        self.nombre = nombre                # str: Nombre del alumno
        self.numero_control = numero_control  # Numero de control 
        self.email = email                  # email
        self.carrera = carrera              # Carrera inscrita del alumno
        self.calificaciones = {}            # Diccionario

    def asignar_carrera(self, carrera):
        self.carrera = carrera

    def consulta_calificacion(self, nombre_materia: str):
        if nombre_materia in self.calificaciones:
            return self.calificaciones[nombre_materia]
        else:
            return f'No hay calificación registrada para "{nombre_materia}".'

    def __repr__(self):
        return f'Alumno("{self.nombre}", "{self.numero_control}", "{self.email}")'


class Universidad:
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre          # Nombre de la institución
        self.direccion = direccion    # Domicilio de la universidad
        self.carreras = []            # Carrera
        self.alumnos = []             # Alumno
        self.profesores = []          # Profesor

    # Gestion de las carreras
    def agregar_carrera(self, carrera):
        self.carreras.append(carrera)

    def obtener_carrera(self, nombre_carrera: str):
        for c in self.carreras:
            if c.nombre == nombre_carrera:
                return c
        return None

    # Registros xd

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)


class Carrera:
    def __init__(self, nombre: str, duracion_semestres: int):
        self.nombre = nombre                    # Nombre de la carrera
        self.duracion_semestres = duracion_semestres # Semestres de la carrera
        self.materias = []                      # Lista de objetos Materia

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def obtener_materia(self, nombre_materia: str):
        for m in self.materias:
            if m.nombre == nombre_materia:
                return m
        return None

    def __repr__(self):
        return f'Carrera("{self.nombre}", {self.duracion_semestres} semestres)'


class Materia:
    def __init__(self, nombre: str, codigo_materia: str, creditos: int, carrera: Carrera):
        self.nombre = nombre                # Nombre de la materia
        self.codigo_materia = codigo_materia  # Identificadorde la materia
        self.creditos = creditos            # Valor de la materia
        self.carrera = carrera              # Carrera a la que pertenece

    def __repr__(self):
        return f'Materia("{self.nombre}", Cod: "{self.codigo_materia}", Carrera="{self.carrera.nombre}")'


class Profesor:
    def __init__(self, nombre: str, numero_empleado: str, materia: Materia):
        self.nombre = nombre                # Nombre del profesor
        self.numero_empleado = numero_empleado # Identificador del profesor
        self.materia = materia              # Materia impartida por el profesor

    def registra_calificacion(self, alumno: Alumno, calificacion: float):

        # Asigna la calificación

        alumno.calificaciones[self.materia.nombre] = calificacion
        print(f'Calificación registrada: {alumno.nombre} -> '
              f'{self.materia.nombre}: {calificacion}')

    def __repr__(self):
        return f'Profesor("{self.nombre}", ID: "{self.numero_empleado}", Materia: {self.materia.nombre})'

# MAIN

if __name__ == "__main__":

    # 1. Creación de Universidad

    uni = Universidad("Instituto Tecnológico de Fátima", "Av. de la Universidad 123")

    # 2. Creación de Carreras

    ing = Carrera("Ingeniería en Software", 8)
    lic = Carrera("Licenciatura en Ciencias Sociales", 9)

    uni.agregar_carrera(ing)
    uni.agregar_carrera(lic)

    # 3. Creación de Materias

    calc = Materia("Cálculo I", "SOFT101", 8, ing)
    fis = Materia("Física I", "SOFT102", 8, ing)
    sociologia = Materia("Introducción a la Sociología", "SOC101", 6, lic)

    ing.agregar_materia(calc)
    ing.agregar_materia(fis)
    lic.agregar_materia(sociologia)

    # 4. Creación de Alumnos

    juan = Alumno("Juan Pérez", "2023001", "juan.perez@uni.com")
    luisa = Alumno("Luisa Gómez", "2023002", "luisa.gomez@uni.com")

    # Asignación de carrera a alumnos

    juan.asignar_carrera(ing)
    luisa.asignar_carrera(ing)

    # Registro de alumnos en la universidad

    uni.agregar_alumno(juan)
    uni.agregar_alumno(luisa)

    # 5. Creación de Profesores

    prof_garcia = Profesor("Dr. García", "EMP456", calc)
    prof_rodriguez = Profesor("Mtra. Rodríguez", "EMP457", fis)

    # Registro de los profesores en la universidad

    uni.agregar_profesor(prof_garcia)
    uni.agregar_profesor(prof_rodriguez)

    # 6.- Acciones (Registra las calificaciones)

    print("--- Registrando Calificaciones ---")
    prof_garcia.registra_calificacion(juan, 8.5)
    prof_garcia.registra_calificacion(luisa, 9.0)
    prof_rodriguez.registra_calificacion(juan, 7.5)
    print("----------------------------------\n")

    # 7.- Consultas (Imprime en la consola)

    print("--- Consultando Calificaciones ---")
    print(f"Juan - Cálculo I: {juan.consulta_calificacion('Cálculo I')}")
    print(f"Juan - Física I: {juan.consulta_calificacion('Física I')}")
    print(f"Luisa - Cálculo I: {luisa.consulta_calificacion('Cálculo I')}")
    print(f"Luisa - Física I: {luisa.consulta_calificacion('Física I')}")
    print("----------------------------------\n")

    print("Materias de Ingeniería:", [m.nombre for m in ing.materias])

    # GUARDAR LOS DATOS EN UN ARCHIVO .TXT

    print("\n[INFO] Guardando datos en 'reporte_universidad.txt'...")

    try:
        with open("reporte_universidad.txt", "w", encoding="utf-8") as f:
            f.write(f"REPORTE DE LA UNIVERSIDAD: {uni.nombre}\n")
            f.write(f"Dirección: {uni.direccion}\n")
            f.write("="*40 + "\n\n")

            f.write("--- PROFESORES ---\n")
            for p in uni.profesores:
                f.write(f"  - {p.nombre} (ID: {p.numero_empleado})\n")
                f.write(f"    Materia: {p.materia.nombre}\n")
            f.write("\n")

            f.write(" CARRERAS Y MATERIAS \n")
            for c in uni.carreras:
                f.write(f"  - Carrera: {c.nombre} (Duración: {c.duracion_semestres} semestres)\n")
                f.write(f"    Materias:\n")
                for m in c.materias:
                    f.write(f"      * {m.nombre} (Código: {m.codigo_materia}, Créditos: {m.creditos})\n")
            f.write("\n")

            f.write(" ALUMNOS Y CALIFICACIONES \n")
            for a in uni.alumnos:
                f.write(f"  - Alumno: {a.nombre} (Control: {a.numero_control}, Email: {a.email})\n")
                f.write(f"    Carrera: {a.carrera.nombre}\n")
                f.write(f"    Calificaciones:\n")
                if not a.calificaciones:
                    f.write("      * Sin calificaciones registradas.\n")
                else:
                    for materia_nombre, calif in a.calificaciones.items():
                        f.write(f"      * {materia_nombre}: {calif}\n")
                f.write("\n")

        print("Reporte guardado exitosamente.")

    except IOError as e:
        print(f"[ERROR] No se pudo escribir el archivo: {e}")