# Implementar los metodos de la capa de negocio de socios.

from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 10

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        try:
            return self.datos.buscar(id_socio)
        except:
            return None

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        try:
            return self.datos.buscar_dni(dni_socio)
        except:
            return None

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        return self.datos.todos()

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        if not self.regla_1(socio) or not self.regla_2(socio) or not self.regla_3():
            return False
        self.datos.alta(socio)
        return True

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        socio = self.buscar(id_socio)
        if socio is None:
            return False
        else:
            self.datos.baja(socio.id_socio)
            return True

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        if not self.regla_2(socio):
            return False
        self.datos.modificacion(socio)
        return True

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        if self.buscar_dni(socio.dni) is not None:
            raise DniRepetido("El DNI ya existe.")


    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        if ( len(socio.nombre) > self.MIN_CARACTERES
            and len(socio.nombre) < self.MAX_CARACTERES
            and len(socio.apellido) > self.MIN_CARACTERES
            and len(socio.apellido) < self.MAX_CARACTERES
        ):
            raise LongitudInvalida("El nombre y apellido del socio debe ser mayor a 3 caracteres y menor a 15 caracteres")


    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        if len(self.todos()) >= self.MAX_SOCIOS:
            raise MaximoAlcanzado("Numero maximo de socios alcanzado")
