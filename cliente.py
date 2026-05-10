import logging

# Configuración del archivo de logs para registrar errores y eventos 
logging.basicConfig(
    filename='errores_sistema.log', 
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# --- EXCEPCIONES PERSONALES  ---
class ValidacionDatoError(Exception):
    """Excepción personalizada para errores de validación en datos del cliente."""
    pass

# --- CLASE ABSTRACTA DE ENTIDAD GENERAL  ---
from abc import ABC, abstractmethod

class EntidadBase(ABC):
    """Representa entidades generales del sistema Software FJ."""
    
    @abstractmethod
    def mostrar_informacion(self):
        """Método abstracto para obligar a las clases derivadas a implementarlo[cite: 11]."""
        pass

# --- CLASE CLIENTE [cite: 22] ---
class Cliente(EntidadBase):
    """
    Gestiona la información de los clientes con validaciones robustas y encapsulación.
    Autor: Andres Felipe Ceron Manrique
    ID: 1083841075 | Tel: 3103218279
    """

    def __init__(self, nombre, email, identificacion, telefono):
        # Atributos privados para cumplir con la encapsulación 
        self.__nombre = None
        self.__email = None
        self.__identificacion = None
        self.__telefono = None
        
        # Uso de setters para aplicar validaciones desde la creación
        try:
            self.nombre = nombre
            self.email = email
            self.identificacion = identificacion
            self.telefono = telefono
        except ValidacionDatoError as e:
            logging.error(f"Error al crear cliente: {e}")
            raise

    # GETTERS Y SETTERS CON VALIDACIONES ROBUSTAS [cite: 22]
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or len(valor.strip()) < 3:
            raise ValidacionDatoError("El nombre debe tener al menos 3 caracteres.")
        self.__nombre = valor

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        if "@" not in valor or "." not in valor:
            raise ValidacionDatoError(f"Email inválido: {valor}")
        self.__email = valor

    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, valor):
        # Validación de que la identificación sea numérica [cite: 19]
        if not str(valor).isdigit():
            raise ValidacionDatoError("La identificación debe ser un valor numérico.")
        self.__identificacion = valor

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        if not str(valor).isdigit():
            raise ValidacionDatoError("El teléfono debe contener solo números.")
        self.__telefono = valor

    # Implementación del método abstracto 
    def mostrar_informacion(self):
        return f"Cliente: {self.nombre} | ID: {self.identificacion} | Email: {self.email}"

# --- SIMULACIÓN DE OPERACIÓN [cite: 32] ---
if __name__ == "__main__":
    try:
        # Ejemplo con tus datos proporcionados
        nuevo_cliente = Cliente(
            nombre="Andres Felipe Ceron Manrique",
            email="ceronmanriqueandresfelipe@gmail.com",
            identificacion="1083841075",
            telefono="3103218279"
        )
        print("Operación exitosa:")
        print(nuevo_cliente.mostrar_informacion())
        
    except ValidacionDatoError as e:
        # Manejo controlado de excepciones [cite: 17, 32]
        print(f"No se pudo registrar el cliente: {e}")
    finally:
        print("Proceso de validación finalizado.") # Uso de bloque finally
