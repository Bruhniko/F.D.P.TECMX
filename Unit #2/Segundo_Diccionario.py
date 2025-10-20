import json

biblioteca = {
    "978-84-376-0494-7": {
        "título": "Cien años de soledad",
        "autor": ["Gabriel García Márquez"],
        "géneros": ["Realismo mágico", "Novela histórica"]
    },
    "978-84-204-1625-5": {
        "título": "Don Quijote de la Mancha",
        "autor": ["Miguel de Cervantes Saavedra"],
        "géneros": ["Novela de caballería", "Sátira"]
    },
    "978-84-670-6232-5": {
        "título": "La sombra del viento",
        "autor": ["Carlos Ruiz Zafón"],
        "géneros": ["Misterio", "Ficción histórica"]
    },
    "978-84-339-7134-0": {
        "título": "Rayuela",
        "autor": ["Julio Cortázar"],
        "géneros": ["Novela experimental", "Boom latinoamericano"]
    },
        "906-81-569-7254-2": {
        "título": "Bajo la Misma Estrella",
        "autor": ["John Green"],
        "géneros": ["Novela de amor", "Juvenil"]
    }
}

isbn = "978-84-376-0494-7"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:", info_libro)
