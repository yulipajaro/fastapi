from abc import ABC, abstractmethod

class EstrategiaDescuento(ABC):
    @abstractmethod
    def calcular_descuento(self, precio_base: float) -> float:
        pass

class SinDescuento(EstrategiaDescuento):
    def calcular_descuento(self, precio_base: float) -> float:
        return 0.0

class DescuentoEstudiante(EstrategiaDescuento):
    def calcular_descuento(self, precio_base: float) -> float:
        return precio_base * 0.2  # Descuento del 20% para estudiantes

class DescuentoNiño(EstrategiaDescuento):
    def calcular_descuento(self, precio_base: float) -> float:
        return precio_base * 0.5  # Descuento del 50% para niños

class DescuentoMilitar(EstrategiaDescuento):
    def calcular_descuento(self, precio_base: float) -> float:
        return precio_base * 0.3  # Descuento del 30% para militares

class DescuentoDiaSemana(EstrategiaDescuento):
    def __init__(self, dia_semana: str):
        self.dia_semana = dia_semana.lower()

    def calcular_descuento(self, precio_base: float) -> float:
        if self.dia_semana in ['lunes', 'miércoles']:
            return precio_base * 0.4  # Descuento del 40% para los lunes y miércoles
        else:
            return precio_base

class PrecioEntrada:
    def __init__(self, estrategia_descuento: EstrategiaDescuento):
        self.estrategia_descuento = estrategia_descuento

    def calcular_precio_final(self, precio_base: float) -> float:
        descuento = self.estrategia_descuento.calcular_descuento(precio_base)
        return precio_base - descuento





