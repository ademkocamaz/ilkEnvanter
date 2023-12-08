from django.db import models
from entity._model.entity import Entity


class Software(Entity):
    
    license_key = models.TextField(
        verbose_name="Lisans Anahtarı",
        blank=True,
        null=True,
    )

    license_start_date = models.DateTimeField(
        verbose_name="Lisans Başlangıç Tarih / Saat",
        blank=True,
        null=True,
    )

    license_end_date = models.DateTimeField(
        verbose_name="Lisans Bitiş Tarih / Saat",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Yazılım"
        verbose_name_plural = "Yazılımlar"
