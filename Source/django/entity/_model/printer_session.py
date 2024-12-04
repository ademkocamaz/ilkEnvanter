from django.db import models
from entity._model.printer import Printer
from entity._model.session import Session


class PrinterSession(Session):

    printer = models.ForeignKey(
        verbose_name="Yazıcı", to=Printer, on_delete=models.CASCADE, name="printer_session"
    )

    class Meta:
        verbose_name = "Yazıcı Oturum/Giriş Bilgisi"
        verbose_name_plural = "Yazıcı Oturum/Giriş Bilgileri"
