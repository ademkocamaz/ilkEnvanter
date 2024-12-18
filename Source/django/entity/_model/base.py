from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):

    edited = models.DateTimeField(
        verbose_name="Değiştirilme Tarih/Saat",
        auto_now=True,
        blank=True,
        null=True
    )

    created = models.DateTimeField(
        verbose_name="Oluşturulma Tarih/Saat",
        auto_now_add=True,
        blank=True,
        null=True
    )

    user = models.ForeignKey(
        verbose_name="Düzenleyen Kullanıcı",
        to=User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
