# -*- coding: utf-8 -*-

# Agregar un atributo al objeto Alumno de Edad. Si es mayor de edad que imprima un mensaje
# (Nota: Se agrega un campo "Edad" a la GUI, ya que no hay un objeto "Alumno")


import sys
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget,      
    QLabel,       
    QLineEdit,    
    QPushButton, 
    QVBoxLayout,  
    QHBoxLayout,  
    QMessageBox,  
)


class RegistroAlumnos(QWidget):
    """Ventana principal de la aplicación."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Alumnos")
        self.resize(350, 220) # Ajustar el tamaño de la ventana

        self.nombre_edit = QLineEdit(self)
        self.nombre_edit.setPlaceholderText("Ej.: Ana García")

        self.carrera_edit = QLineEdit(self)
        self.carrera_edit.setPlaceholderText("Ej.: Ingeniería Informática")

        # Campo edad
        self.edad_edit = QLineEdit(self)
        self.edad_edit.setPlaceholderText("Ej.: 21")

        self.guardar_btn = QPushButton("Guardar", self)
        self.guardar_btn.clicked.connect(self.guardar_alumno)

        # Botón Limpiar
        self.limpiar_btn = QPushButton("Limpiar", self)
        self.limpiar_btn.clicked.connect(self.limpiar_campos)

        # Layout
        form_layout = QVBoxLayout()

        # Nombre
        fila_nombre = QHBoxLayout()
        fila_nombre.addWidget(QLabel("Nombre:", self))
        fila_nombre.addWidget(self.nombre_edit)
        form_layout.addLayout(fila_nombre)

        # Carrera
        fila_carrera = QHBoxLayout()
        fila_carrera.addWidget(QLabel("Carrera:", self))
        fila_carrera.addWidget(self.carrera_edit)
        form_layout.addLayout(fila_carrera)

        # Edad
        fila_edad = QHBoxLayout()
        fila_edad.addWidget(QLabel("Edad:", self))
        fila_edad.addWidget(self.edad_edit)
        form_layout.addLayout(fila_edad)


        # Botones
        botones_layout = QHBoxLayout()
        botones_layout.addStretch()
        botones_layout.addWidget(self.guardar_btn)
        botones_layout.addWidget(self.limpiar_btn)
        form_layout.addLayout(botones_layout)

        self.setLayout(form_layout)

        # Ruta del archivo donde se guardan los datos
        self.ruta_archivo = Path("alumnos.txt")

    def guardar_alumno(self):
        nombre = self.nombre_edit.text().strip()
        carrera = self.carrera_edit.text().strip()
        edad_str = self.edad_edit.text().strip()

        # Validación de campos
        if not nombre or not carrera or not edad_str:
            QMessageBox.warning(
                self,
                "Campos incompletos",
                "Debes rellenar nombre, carrera y edad.",
            )
            return

        #   Validación de edad
        try:
            edad_num = int(edad_str)
        except ValueError:
            QMessageBox.warning(
                self, "Edad inválida", "La edad debe ser un número entero."
            )
            return
        
        mensaje_adicional = ""
        if edad_num >= 18:
            # Si es mayor de edad
            mensaje_adicional = f"\n\n¡{nombre} es mayor de edad!"
        # Guardar la edad en el archivo
        linea = f"{nombre} – {carrera} – {edad_num} años\n"

        try:
            with self.ruta_archivo.open("a", encoding="utf-8") as f:
                f.write(linea)
        except OSError as e:
            QMessageBox.critical(
                self,
                "Error de escritura",
                f"No se pudo guardar el registro.\nDetalle: {e}",
            )
            return

        QMessageBox.information(
            self,
            "Guardado",
            f"Alumno guardado correctamente en '{self.ruta_archivo}'." + mensaje_adicional,
        )
        self.limpiar_campos()

    def limpiar_campos(self):
        self.nombre_edit.clear()
        self.carrera_edit.clear()
        self.edad_edit.clear()
        self.nombre_edit.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = RegistroAlumnos()
    ventana.show()
    sys.exit(app.exec_())