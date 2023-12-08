from django.db import models
from entity._model.entity import Entity


class Computer(Entity):
    class Meta:
        verbose_name = "Bilgisayar"
        verbose_name_plural = "Bilgisayarlar"
