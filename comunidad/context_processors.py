from .models import Intercambio

def notificaciones_pendientes(request):
    """
    Motor de notificaciones globales para la Red de Apoyo.
    Calcula cuántos pedidos de ayuda tiene el vecino sin resolver para
    dinamizar la reciprocidad en el territorio digital.
    """
    # 1. Verificamos si el vecino ha iniciado sesión
    if request.user.is_authenticated:
        try:
            # 2. Contamos las solicitudes dirigidas a sus habilidades que están pendientes
            conteo = Intercambio.objects.filter(
                habilidad__ofertante=request.user, 
                completado=False
            ).count()
            
            return {'notificaciones_conteo': conteo}
            
        except Exception:
            # 3. Fallback: Si hay un error técnico, devolvemos 0 para mantener la web en línea
            return {'notificaciones_conteo': 0}
            
    # 4. Si es un visitante anónimo, el conteo es siempre cero
    return {'notificaciones_conteo': 0}