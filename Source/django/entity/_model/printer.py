from django.db import models
from entity._model.entity import Entity
from entity._model.port import Port

class Printer(Entity):
    
    ports = models.ManyToManyField(
        verbose_name="Portlar",
        to=Port
    )

    class Meta:
        verbose_name="Yazıcı"
        verbose_name_plural="Yazıcılar"