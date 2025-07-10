from django.http import JsonResponse
from django.shortcuts import render
from .models import Microcontroller  # импортируй свою модель
from .services import controller_data_cache

def dashboard_view(request):
    controllers = Microcontroller.objects.all()
    controllers_dict = {c.id_device: c for c in controllers}
    return render(request, 'monitor/dashboard.html',
{'controllers_dict': controllers_dict
    })  # путь к шаблону
def api_status(request):
    return JsonResponse(controller_data_cache, safe=False)