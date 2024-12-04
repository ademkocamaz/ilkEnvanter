from django.db import models
from entity._model.base import Base


class Session(Base):

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

    user_name = models.CharField(
        verbose_name="Kullanıcı Adı",
        max_length=500,
        blank=True,
        null=True,
    )

    password = models.CharField(
        verbose_name="Şifre",
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

    class Meta:
        verbose_name = "Oturum/Giriş Bilgisi"
        verbose_name_plural = "Oturum/Giriş Bilgileri"
