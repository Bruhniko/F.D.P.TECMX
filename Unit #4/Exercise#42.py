# -*- coding: utf-8 -*-

# sys: Para argumentos del sistema (sys.argv) y salida (sys.exit).
import sys

# Identifica el sistema operativo (Windows, Linux, etc.).
import platform

# Ejecuta comandos del sistema (como 'ping').
import subprocess

# PyQt5.QtCore: Clases "núcleo" no gráficas de PyQt.
from PyQt5.QtCore import Qt

# PyQt5.QtWidgets: Clases para crear la interfaz gráfica (GUI).
from PyQt5.QtWidgets import (
    QApplication, # Gestion de la aplicación.
    QWidget,      # Clase base para ventanas y widgets.
    QLabel,       # Muestra el texto (etiquetas).
    QLineEdit,    # Entrada de texto de una línea.
    QPushButton,  # Botónes.
    QTextEdit,    # Área de texto multilínea.
    QVBoxLayout,  # Ampliacion de widgets verticalmente.
    QHBoxLayout,  # Layout para alinear widgets horizontalmente.
    QMessageBox,  # Ventana de diálogo.
)

class PingApp(QWidget):
    """Ventana principal de la aplicación."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ping – PyQt5")
        self.resize(400, 300)

        # Widgets
        # Entrada de host / IP
        self.host_input = QLineEdit(self)
        self.host_input.setPlaceholderText("Ejemplo: google.com o 8.8.8.8")

        # Botón de ejecutar ping
        self.ping_btn = QPushButton("Enviar ping", self)
        self.ping_btn.clicked.connect(self.ejecutar_ping)

        # Área de texto donde se mostrará la salida
        self.resultado = QTextEdit(self)
        self.resultado.setReadOnly(True)

        # Layout
        entrada_layout = QHBoxLayout()
        entrada_layout.addWidget(QLabel("Destino:", self))
        entrada_layout.addWidget(self.host_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(entrada_layout)
        main_layout.addWidget(self.ping_btn)
        main_layout.addWidget(QLabel("Resultado:", self))
        main_layout.addWidget(self.resultado)

        self.setLayout(main_layout)

    def ejecutar_ping(self):
        """Construye y ejecuta el comando ping, mostrando la salida."""
        host = self.host_input.text().strip()
        if not host:
            QMessageBox.warning(self, "Entrada vacía", "Introduce una dirección IP o nombre de host.")
            return

        # Determinar parámetros según SO
        sistema = platform.system().lower()
        if "windows" in sistema:
            cmd = ["ping", "-n", "4", host]     # 4 pings en Windows
        else:  # Linux, macOS, etc.
            cmd = ["ping", "-c", "4", host]     # 4 pings en sistemas POSIX

        try:
            # Desactivar el botón mientras se ejecuta
            self.ping_btn.setEnabled(False)
            self.ping_btn.setText("Haciendo ping...")
            self.resultado.setPlainText("Por favor, espera...")
            QApplication.processEvents() # Forzar actualización de la GUI

            # Ejecutamos el comando y capturamos stdout + stderr
            proceso = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=10,         # Límite de 10 segundos
                encoding='utf-8',   # Asegurar codificación correcta
                errors='replace'    # Reemplaza caracteres si hay errores de decodificación
            )
            
            # Muestra la salida estándar si el comando tuvo éxito o si falló
            if proceso.returncode == 0:
                salida = proceso.stdout
            else:
                salida = proceso.stderr
                if not salida:
                    salida = proceso.stdout
            
            self.resultado.setPlainText(salida)

        except subprocess.TimeoutExpired:
            self.resultado.setPlainText("Error: tiempo de espera agotado (10 segundos).")
        except Exception as e:
            self.resultado.setPlainText(f"Ocurrió un error inesperado:\n{e}")
        finally:
            # Reactivar el botón al finalizar
            self.ping_btn.setEnabled(True)
            self.ping_btn.setText("Enviar ping")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = PingApp()
    ventana.show()
    sys.exit(app.exec_())