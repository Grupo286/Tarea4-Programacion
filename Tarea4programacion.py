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

    def __init__(self, codigo, nombre, documento, telefono):

        # Llama al constructor de la clase padre.
        super().__init__(codigo)

        # Encapsulación:
        # atributos privados usando doble guion bajo.
        self.__nombre = None
        self.__documento = None
        self.__telefono = None

        # Uso de setters.
        self.nombre = nombre
        self.documento = documento
        self.telefono = telefono

    # =====================================================
    # PROPIEDAD NOMBRE
    # =====================================================

    @property
    def nombre(self):
        """
        Getter del nombre.
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        """
        Setter del nombre con validación.
        """

        if not valor or len(valor.strip()) < 3:
            raise DatoInvalidoError(
                "El nombre debe tener mínimo 3 caracteres."
            )

        self.__nombre = valor.strip()

    # =====================================================
    # PROPIEDAD DOCUMENTO
    # =====================================================

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):

        # Verifica que solo existan números.
        if not str(valor).isdigit():
            raise DatoInvalidoError(
                "El documento debe contener solo números."
            )

        self.__documento = str(valor)

    # =====================================================
    # PROPIEDAD TELÉFONO
    # =====================================================

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):

        # Validación del teléfono.
        if not str(valor).isdigit() or len(str(valor)) < 7:
            raise DatoInvalidoError(
                "El teléfono debe tener mínimo 7 dígitos."
            )

        self.__telefono = str(valor)   
    
# =====================================================
# MÉTODO MOSTRAR INFORMACIÓN
# =====================================================

    def mostrar_informacion(self):

        return (
            f"Cliente: {self.__nombre} | "
            f"Documento: {self.__documento} | "
            f"Teléfono: {self.__telefono}"
        )


# =========================================================
# CLASE ABSTRACTA SERVICIO
# =========================================================

class Servicio(EntidadSistema):
    """
    Clase abstracta para representar servicios.
    """

    def __init__(self, codigo, nombre, valor_base,
                 disponible=True):

        # Llamado al constructor padre.
        super().__init__(codigo)

        # Validación del valor base.
        if valor_base <= 0:
            raise DatoInvalidoError(
                "El valor base debe ser mayor que cero."
            )

        self._nombre = nombre
        self._valor_base = valor_base
        self._disponible = disponible

    @abstractmethod
    def calcular_costo(self,
                        duracion,
                        descuento=0,
                        impuesto=0):
        """
        Método abstracto para calcular costos.
        """
        pass

    @abstractmethod
    def describir_servicio(self):
        """
        Método abstracto para describir servicios.
        """
        pass

 # =====================================================
 # VALIDAR DISPONIBILIDAD
 # =====================================================

    def validar_disponibilidad(self):

        if not self._disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self._nombre} "
                f"no está disponible."
            )

 # =====================================================
 # MOSTRAR INFORMACIÓN
 # =====================================================

    def mostrar_informacion(self):

        return self.describir_servicio()


# =========================================================
# CLASE RESERVA DE SALA
# =========================================================

class ReservaSala(Servicio):
    """
    Servicio especializado para reservas de salas.
    """

    def calcular_costo(self,
                        duracion,
                        descuento=0,
                        impuesto=0):

        try:

            # Validación de duración.
            if duracion <= 0:
                raise CalculoCostoError(
                    "La duración debe ser mayor que cero."
                )

            # Fórmula del costo.
            costo = self._valor_base * duracion

            # Aplicación de descuento.
            costo -= costo * descuento

            # Aplicación de impuesto.
            costo += costo * impuesto

            return costo

        except Exception as error:

            # Encadenamiento de excepciones.
            raise CalculoCostoError(
                "Error calculando costo "
                "de reserva de sala."
            ) from error

    def describir_servicio(self):

        return (
            f"Reserva de sala: {self._nombre} "
            f"| Valor hora: ${self._valor_base}"
        ) 

# =========================================================
# CLASE ALQUILER DE EQUIPO
# =========================================================

class AlquilerEquipo(Servicio):
    """
    Servicio especializado para alquiler de equipos.
    """

    def calcular_costo(self,
                        duracion,
                        descuento=0,
                        impuesto=0):

        try:

            if duracion <= 0:
                raise CalculoCostoError(
                    "La duración debe ser mayor que cero."
                )

            costo = self._valor_base * duracion

            # Si el alquiler es mayor o igual a 5 horas
            # se aplica descuento adicional.
            if duracion >= 5:
                costo -= costo * 0.10

            costo -= costo * descuento
            costo += costo * impuesto

            return costo

        except Exception as error:

            raise CalculoCostoError(
                "Error calculando costo "
                "de alquiler."
            ) from error

    def describir_servicio(self):

        return (
            f"Alquiler de equipo: {self._nombre} "
            f"| Valor hora: ${self._valor_base}"
        )


# =========================================================
# CLASE ASESORÍA ESPECIALIZADA
# =========================================================

class AsesoriaEspecializada(Servicio):
    """
    Servicio especializado para asesorías.
    """

    def calcular_costo(self,
                        duracion,
                        descuento=0,
                        impuesto=0):

        try:

            if duracion <= 0:
                raise CalculoCostoError(
                    "La duración debe ser mayor que cero."
                )

            costo = self._valor_base * duracion

            # Incremento del 20%
            # por ser asesoría especializada.
            costo += costo * 0.20

            costo -= costo * descuento
            costo += costo * impuesto

            return costo

        except Exception as error:

            raise CalculoCostoError(
                "Error calculando asesoría."
            ) from error

    def describir_servicio(self):

        return (
            f"Asesoría especializada: "
            f"{self._nombre} "
            f"| Valor hora: ${self._valor_base}"
        )


# =========================================================
# CLASE RESERVA
# =========================================================

class Reserva:
    """
    Clase que representa una reserva.
    """

    def __init__(self,
                 cliente,
                 servicio,
                 duracion):

        # Verifica si cliente es válido.
        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError(
                "Cliente inválido."
            )

        # Verifica si servicio es válido.
        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError(
                "Servicio inválido."
            )

        # Verifica duración.
        if duracion <= 0:
            raise ReservaInvalidaError(
                "La duración debe ser mayor que cero."
            )

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.costo_total = 0

    # =====================================================
    # CONFIRMAR RESERVA
    # =====================================================

    def confirmar(self):

        try:

            # Verifica disponibilidad.
            self.servicio.validar_disponibilidad()

            self.estado = "Confirmada"

            registrar_log(
                f"Reserva confirmada para "
                f"{self.cliente.nombre}"
            )

            return "Reserva confirmada."

        except ServicioNoDisponibleError as error:

            registrar_log(f"ERROR: {error}")

            raise

        finally:

            registrar_log(
                "Proceso de confirmación finalizado."
            )

    # =====================================================
    # CANCELAR RESERVA
    # =====================================================

    def cancelar(self):

        if self.estado == "Cancelada":

            raise ReservaInvalidaError(
                "La reserva ya está cancelada."
            )

        self.estado = "Cancelada"

        registrar_log(
            f"Reserva cancelada para "
            f"{self.cliente.nombre}"
        )

        return "Reserva cancelada."

    # =====================================================
    # PROCESAR RESERVA
    # =====================================================

    def procesar(self):

        try:

            # Solo se procesan reservas confirmadas.
            if self.estado != "Confirmada":

                raise ReservaInvalidaError(
                    "La reserva debe estar confirmada."
                )

            # Cálculo del costo total.
            self.costo_total = (
                self.servicio.calcular_costo(
                    self.duracion,
                    descuento=0.05,
                    impuesto=0.19
                )
            )

        except ReservaInvalidaError as error:

            registrar_log(
                f"ERROR DE RESERVA: {error}"
            )

            raise

        except CalculoCostoError as error:

            registrar_log(
                f"ERROR DE CÁLCULO: {error}"
            )

            raise

        else:

            self.estado = "Procesada"

            registrar_log(
                f"Reserva procesada. "
                f"Costo total: ${self.costo_total:.2f}"
            )

            return (
                f"Reserva procesada. "
                f"Costo total: ${self.costo_total:.2f}"
            )

        finally:

            registrar_log(
                "Proceso de reserva finalizado."
            )


# =========================================================
# LISTAS INTERNAS
# =========================================================

# Aquí se almacenan los objetos.

clientes = []
servicios = []
reservas = []


# =========================================================
# FUNCIÓN PARA EJECUTAR OPERACIONES
# =========================================================

def ejecutar_operacion(numero, funcion):

    print(f"\n--- Operación {numero} ---")

    try:

        resultado = funcion()

    except ErrorSistema as error:

        print(f"Error controlado: {error}")

        registrar_log(
            f"ERROR CONTROLADO "
            f"EN OPERACIÓN {numero}: {error}"
        )

    except Exception as error:

        print(f"Error grave: {error}")

        registrar_log(
            f"ERROR GRAVE "
            f"EN OPERACIÓN {numero}: {error}"
        )

    else:

        print(resultado)

        registrar_log(
            f"OPERACIÓN {numero} EXITOSA"
        )

    finally:

        print("La aplicación continúa funcionando.")


# =========================================================
# OPERACIONES DE PRUEBA
# =========================================================

def op1():

    cliente = Cliente(
        "C001",
        "Francisco Yucuma",
        "1084923560",
        "3012134262"
    )

    clientes.append(cliente)

    return cliente.mostrar_informacion()

def op2():
    cliente = Cliente("C002", "andres ceron", "1083841075", "3103218279")
    clientes.append(cliente)
    return cliente.mostrar_informacion()

def op3():

    # Cliente inválido.
    cliente = Cliente(
        "C002",
        "An",
        "ABC123",
        "123"
    )

    clientes.append(cliente)

    return cliente.mostrar_informacion()


def op4():

    servicio = ReservaSala(
        "S001",
        "Sala ejecutiva",
        50000
    )

    servicios.append(servicio)

    return servicio.describir_servicio()


def op4():

    servicio = AlquilerEquipo(
        "S002",
        "Video Beam Epson",
        30000
    )

    servicios.append(servicio)

    return servicio.describir_servicio()

def op5():
    servicio = AlquilerEquipo("S002", "Video Beam Epson", 30000)
    servicios.append(servicio)
    return servicio.describir_servicio()

def op6():

    servicio = AsesoriaEspecializada(
        "S003",
        "Asesoría en Software",
        80000
    )

    servicios.append(servicio)

    return servicio.describir_servicio()

def op7():
    servicio = ReservaSala("S004", "Sala dañada", -10000)
    servicios.append(servicio)
    return servicio.describir_servicio()


def op8():
    reserva = Reserva(clientes[0], servicios[0], 3)
    reservas.append(reserva)
    reserva.confirmar()
    return reserva.procesar()


def op9():
    reserva = Reserva(clientes[1], servicios[1], 6)
    reservas.append(reserva)
    reserva.confirmar()
    return reserva.procesar()


def op10():
    reserva = Reserva(clientes[0], servicios[2], 2)
    reservas.append(reserva)
    reserva.confirmar()
    reserva.cancelar()
    return reserva.procesar()


def op11():
    servicio_no_disponible = ReservaSala(
        "S005",
        "Sala en mantenimiento",
        45000,
        disponible=False
    )

    reserva = Reserva(clientes[0], servicio_no_disponible, 2)
    reservas.append(reserva)
    reserva.confirmar()
    return reserva.procesar()


def op12():
    reserva = Reserva(clientes[0], servicios[0], -4)
    reservas.append(reserva)
    return reserva.mostrar_reserva()


def op13():
    costo = servicios[2].calcular_costo(
        duracion=3,
        descuento=0.10,
        impuesto=0.19
    )
    return f"Cálculo con descuento e impuesto: ${costo:.2f}"



# =========================================================
# PROGRAMA PRINCIPAL
# =========================================================

if __name__ == "__main__":

    registrar_log(
        "Inicio del sistema Software FJ."
    )

    operaciones = [
        op1,
        op2,
        op3,
        op4,
        op5,
        op6,
        op7,
        op8,
        op9,
        op10,
        op11,
        op12,
        op13

    ]


    # Ejecuta todas las operaciones.
    for i, operacion in enumerate(
            operaciones,
            start=1):

        ejecutar_operacion(i, operacion)

    registrar_log(
        "Fin de la ejecución del sistema."
    )

    print("\nSistema finalizado correctamente.")
       