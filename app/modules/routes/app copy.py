from fastapi import APIRouter, Depends, HTTPException
from enum import Enum
from .strategy import EnvioNormal, EnvioExpress, RecogidaLocal, EstrategiaTienda

class TipoEnvio(Enum):
    NORMAL = "normal"
    EXPRESS = "express"
    LOCAL = "local"

def obtener_estrategia_envio(tipo_envio: TipoEnvio) -> EstrategiaTienda:
    if tipo_envio == TipoEnvio.NORMAL:
        return EnvioNormal()
    elif tipo_envio == TipoEnvio.EXPRESS:
        return EnvioExpress()
    elif tipo_envio == TipoEnvio.LOCAL:
        return RecogidaLocal()
    else:
        raise HTTPException(status_code=400, detail="Tipo de envío inválido")

router = APIRouter()

@router.get("/calcular_ruta")
def calcular_ruta(producto: str, cantidad: int, tipo_envio: TipoEnvio, envio: EstrategiaTienda = Depends(obtener_estrategia_envio)) -> str:
    return envio.calcular_ruta(producto, cantidad)

@router.get("/calcular_costo_envio")
def calcular_costo_envio(producto: str, cantidad: int, tipo_envio: TipoEnvio, envio: EstrategiaTienda = Depends(obtener_estrategia_envio)) -> float:
    return envio.calcular_costo_envio(producto, cantidad)

@router.get("/calcular_tiempo_entrega")
def calcular_tiempo_entrega(producto: str, cantidad: int, tipo_envio: TipoEnvio, envio: EstrategiaTienda = Depends(obtener_estrategia_envio)) -> int:
    return envio.calcular_tiempo_entrega(producto, cantidad)
