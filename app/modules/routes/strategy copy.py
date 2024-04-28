rom abc import ABC, abstractmethod

class EstrategiaTienda(ABC):
    @abstractmethod
    def calcular_ruta(self, producto: str, cantidad: int) -> str:
        pass

    @abstractmethod
    def calcular_costo_envio(self, producto: str, cantidad: int) -> float:
        pass

    @abstractmethod
    def calcular_tiempo_entrega(self, producto: str, cantidad: int) -> int:
        pass

class EnvioNormal(EstrategiaTienda):
    def calcular_ruta(self, producto: str, cantidad: int) -> str:
        return "Envío estándar"

    def calcular_costo_envio(self, producto: str, cantidad: int) -> float:
        return 5.00

    def calcular_tiempo_entrega(self, producto: str, cantidad: int) -> int:
        return 3

class EnvioExpress(EstrategiaTienda):
    def calcular_ruta(self, producto: str, cantidad: int) -> str:
        return "Envío express"

    def calcular_costo_envio(self, producto: str, cantidad: int) -> float:
        return 10.00

    def calcular_tiempo_entrega(self, producto: str, cantidad: int) -> int:
        return 1

class RecogidaLocal(EstrategiaTienda):
    def calcular_ruta(self, producto: str, cantidad: int) -> str:
        return "Recogida en tienda"

    def calcular_costo_envio(self, producto: str, cantidad: int) -> float:
        return 0.00

    def calcular_tiempo_entrega(self, producto: str, cantidad: int) -> int:
        return 0
