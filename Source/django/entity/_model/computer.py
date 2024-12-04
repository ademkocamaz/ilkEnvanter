from django.db import models
from entity._model.entity import Entity
from entity._model.port import Port

class Computer(Entity):

    ports = models.ManyToManyField(verbose_name="Portlar", to=Port, blank=True)

    class Meta:
        verbose_name = "Bilgisayar"
        verbose_name_plural = "Bilgisayarlar"
