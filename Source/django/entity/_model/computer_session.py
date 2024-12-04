from django.db import models
from entity._model.computer import Computer
from entity._model.session import Session


class ComputerSession(Session):

    computer = models.ForeignKey(
        verbose_name="Bilgisayar", to=Computer, on_delete=models.CASCADE, name="computer_session"
    )

    class Meta:
        verbose_name = "Bilgisayar Oturum/Giriş Bilgisi"
        verbose_name_plural = "Bilgisayar Oturum/Giriş Bilgileri"
