from django.db import models
from entity._model.license import License
from entity._model.session import Session


class LicenseSession(Session):

    license = models.ForeignKey(
        verbose_name="Lisans", to=License, on_delete=models.CASCADE, name="license_session"
    )

    class Meta:
        verbose_name = "Lisans Oturum/Giriş Bilgisi"
        verbose_name_plural = "Lisans Oturum/Giriş Bilgileri"
