from django.db import models
from entity._model.device import Device
from entity._model.session import Session


class DeviceSession(Session):

    device = models.ForeignKey(
        verbose_name="Aygıt", to=Device, on_delete=models.CASCADE, name="device_session"
    )

    class Meta:
        verbose_name = "Aygıt Oturum/Giriş Bilgisi"
        verbose_name_plural = "Aygıt Oturum/Giriş Bilgileri"
