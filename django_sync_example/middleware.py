import time


class APITrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.start_time = time.time()
        response = self.get_response(request)
        process_time = str(time.time() - request.start_time)
        response["X-Process-Time"] = str(process_time)
        return response
