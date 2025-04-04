import time

class TiempoDeProcesamientoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Código antes de procesar la vista
        tiempo_inicio = time.time()

        response = self.get_response(request)

        # Código después de procesar la vista
        tiempo_fin = time.time()
        tiempo_total = tiempo_fin - tiempo_inicio

        response['X-Tiempo-De-Procesamiento'] = str(tiempo_total)
        print(tiempo_total)

        return response