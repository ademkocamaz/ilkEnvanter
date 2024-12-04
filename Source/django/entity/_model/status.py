from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):

    name = models.CharField(
        verbose_name="Durum Adı",
        max_length=500,
    )

    edited = models.DateTimeField(
        verbose_name="Değiştirilme Tarih/Saat",
        auto_now=True,
    )

    created = models.DateTimeField(
        verbose_name="Oluşturulma Tarih/Saat",
        auto_now_add=True,
    )

    user = models.ForeignKey(
        verbose_name="Düzenleyen Kullanıcı",
        to=User,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Durum"
        verbose_name_plural = "Durumlar"
