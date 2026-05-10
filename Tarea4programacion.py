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

# =========================================================
# CLASE CLIENTE
# =========================================================

class Cliente(EntidadSistema):
    """
    Gestiona la información de los clientes con validaciones robustas y encapsulación.
    Autor: Andres Felipe Ceron Manrique
    ID: 1083841075 | Tel: 3103218279
    """

    def __init__(self, codigo, nombre, email, identificacion, telefono):
        # Llamada al constructor de la clase abstracta principal (requerido por Francisco)
        super().__init__(codigo)
        
        # Atributos privados para cumplir con la encapsulación 
        self.__nombre = None
        self.__email = None
        self.__identificacion = None
        self.__telefono = None
        
        # Uso de setters para aplicar validaciones desde la creación
        self.nombre = nombre
        self.email = email
        self.identificacion = identificacion
        self.telefono = telefono

    # GETTERS Y SETTERS CON VALIDACIONES ROBUSTAS
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or len(valor.strip()) < 3:
            raise DatoInvalidoError("El nombre debe tener al menos 3 caracteres.")
        self.__nombre = valor.strip()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        if "@" not in valor or "." not in valor:
            raise DatoInvalidoError(f"Email inválido: {valor}")
        self.__email = valor

    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, valor):
        # Validación de que la identificación sea numérica 
        if not str(valor).isdigit():
            raise DatoInvalidoError("La identificación debe ser un valor numérico.")
        self.__identificacion = str(valor)

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        if not str(valor).isdigit():
            raise DatoInvalidoError("El teléfono debe contener solo números.")
        self.__telefono = str(valor)

    # Implementación del método abstracto exigido por EntidadSistema
    def mostrar_informacion(self):
        return f"Cliente: {self.nombre} | ID: {self.identificacion} | Email: {self.email} | Tel: {self.telefono}"
        