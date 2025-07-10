from django.db import models

class Microcontroller(models.Model):
    id_device = models.CharField(max_length=100, verbose_name="id положения конроллера")
    name = models.CharField(max_length=100, verbose_name="имя на схеме")
    ip = models.GenericIPAddressField(protocol='IPv4', verbose_name="IP-адрес")
    min_temp = models.FloatField(verbose_name="Мин. температура (°C)")
    max_temp = models.FloatField(verbose_name="Макс. температура (°C)")
    min_pressure = models.FloatField(verbose_name="Мин. давление (Атм)")
    max_pressure = models.FloatField(verbose_name="Макс. давление (Атм)")

    def __str__(self):
        return self.name
