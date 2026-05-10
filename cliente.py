from Tarea4programacion import EntidadSistema, DatoInvalidoError

# --- CLASE CLIENTE ---
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
        return f"Cliente: {self.nombre} | ID: {self.identificacion} | Email: {self.email} | Tel: {self.telefono}
