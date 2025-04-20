from main_site.models import VisitorCount

class visitorCounter:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time initialization

    def __call__(self, request):
        response = self.get_response(request)
        VisitorCount.increment(request, response)
        return response