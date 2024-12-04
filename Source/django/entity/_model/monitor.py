from django.db import models
from entity._model.entity import Entity
from entity._model.port import Port


class Monitor(Entity):

    size = models.DecimalField(
        verbose_name="Boyut",
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    ports = models.ManyToManyField(
        verbose_name="Portlar", to=Port, blank=True
    )

    class Meta:
        verbose_name = "Monitör"
        verbose_name_plural = "Monitörler"
