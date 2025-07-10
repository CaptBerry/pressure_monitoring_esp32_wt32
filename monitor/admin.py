from django.contrib import admin
from .models import Microcontroller

@admin.register(Microcontroller)
class MicrocontrollerAdmin(admin.ModelAdmin):
    list_display = ('id_device', 'name', 'ip', 'min_temp', 'max_temp', 'min_pressure', 'max_pressure')
