from django.db import models
from entity._model.entity import Entity
from entity._model.port import Port


class Network(Entity):

    ip_address = models.CharField(
        verbose_name="IP Adresi",
        max_length=500,
        blank=True,
        null=True,
    )

    ports = models.ManyToManyField(
        verbose_name="Portlar", to=Port, blank=True
    )

    class Meta:
        verbose_name = "Ağ Cihazı"
        verbose_name_plural = "Ağ Cihazları"
