from django.db import models
from entity._model.base import Base
from entity._model.status import Status


class Entity(Base):

    tag = models.CharField(
        verbose_name="Etiket",
        max_length=500,
        blank=True,
        null=True,
    )

    name = models.CharField(
        verbose_name="Adı",
        max_length=500,
    )

    location = models.CharField(
        verbose_name="Konum",
        max_length=500,
        blank=True,
        null=True,
    )

    status = models.ForeignKey(
        verbose_name="Durum",
        to=Status,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    manufacturer = models.CharField(
        verbose_name="Üretici",
        max_length=500,
        blank=True,
        null=True,
    )

    brand = models.CharField(
        verbose_name="Marka",
        max_length=500,
        blank=True,
        null=True,
    )

    model = models.CharField(
        verbose_name="Model",
        max_length=500,
        blank=True,
        null=True,
    )

    serial_number = models.CharField(
        verbose_name="Seri Numarası",
        max_length=500,
        blank=True,
        null=True,
    )

    product_number = models.CharField(
        verbose_name="Ürün Numarası",
        max_length=500,
        blank=True,
        null=True,
    )

    inventory_number = models.CharField(
        verbose_name="Stok Numarası",
        max_length=500,
        blank=True,
        null=True,
    )

    used_by = models.CharField(
        verbose_name="Kullanan Birim / Kullanıcı",
        max_length=500,
        blank=True,
        null=True,
    )

    description = models.TextField(
        verbose_name="Açıklama",
        blank=True,
        null=True,
    )

    note = models.TextField(
        verbose_name="Not",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
