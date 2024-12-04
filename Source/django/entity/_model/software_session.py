from django.db import models
from entity._model.software import Software
from entity._model.session import Session


class SoftwareSession(Session):

    software = models.ForeignKey(
        verbose_name="Yazılım", to=Software, on_delete=models.CASCADE, name="software_session"
    )

    class Meta:
        verbose_name = "Yazılım Oturum/Giriş Bilgisi"
        verbose_name_plural = "Yazılım Oturum/Giriş Bilgileri"
