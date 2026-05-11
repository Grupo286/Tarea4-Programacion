# SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES,
# SERVICIOS Y RESERVAS
# EMPRESA: SOFTWARE FJ
#
# Autor: Francisco Jimeno Yucuma Morales,Andres Felipe Ceron Manrique.
# Curso: Programación
#
# Este sistema fue desarrollado utilizando:
# ✔ Programación Orientada a Objetos
# ✔ Abstracción
# ✔ Herencia
# ✔ Polimorfismo
# ✔ Encapsulación
# ✔ Manejo avanzado de excepciones
# ✔ Archivos de logs
#
# IMPORTANTE:
# El sistema NO utiliza bases de datos.
# Toda la información se maneja mediante objetos y listas.
# =========================================================


# =========================================================
# IMPORTACIÓN DE LIBRERÍAS
# =========================================================

# ABC y abstractmethod permiten crear clases abstractas.
from abc import ABC, abstractmethod

# datetime se utiliza para registrar fecha y hora en logs.
from datetime import datetime


# =========================================================
# ARCHIVO DE LOGS
# =========================================================

# Nombre del archivo donde se guardarán errores y eventos.
LOG_FILE = "logs_software_fj.txt"


def registrar_log(mensaje):
    """
    Esta función guarda mensajes dentro del archivo de logs.

    Parámetro:
    mensaje -> texto que se desea guardar en el archivo.
    """

    # Abrimos el archivo en modo agregar.
    # encoding="utf-8" permite guardar caracteres especiales.
    with open(LOG_FILE, "a", encoding="utf-8") as archivo:

        # Obtiene fecha y hora actual.
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Guarda la información dentro del archivo.
        archivo.write(f"[{fecha}] {mensaje}\n")


# =========================================================
# EXCEPCIONES PERSONALIZADAS
# =========================================================

# Todas las excepciones del sistema heredarán de ErrorSistema.


class ErrorSistema(Exception):
    """
    Clase base para errores personalizados.
    """
    pass


class DatoInvalidoError(ErrorSistema):
    """
    Error generado cuando un dato ingresado es inválido.
    """
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """
    Error generado cuando un servicio no está disponible.
    """
    pass


class ReservaInvalidaError(ErrorSistema):
    """
    Error generado cuando una reserva es incorrecta.
    """
    pass


class CalculoCostoError(ErrorSistema):
    """
    Error generado cuando ocurre un problema calculando costos.
    """
    pass


# =========================================================
# CLASE ABSTRACTA GENERAL
# =========================================================

class EntidadSistema(ABC):
    """
    Clase abstracta principal del sistema.

    Todas las entidades del sistema heredarán de esta clase.
    """

    def __init__(self, codigo):

        # Validación del código.
        if not codigo:
            raise DatoInvalidoError(
                "El código no puede estar vacío."
            )

        # Atributo protegido.
        self._codigo = codigo

    @abstractmethod
    def mostrar_informacion(self):
        """
        Método abstracto.

        Todas las clases hijas deberán implementarlo.
        """
        pass 
    