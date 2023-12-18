from django.http import JsonResponse

def index(req):
    if req.method == "GET":
        return JsonResponse({'response': True})
