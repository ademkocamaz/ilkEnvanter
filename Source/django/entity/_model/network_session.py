from django.db import models
from entity._model.network import Network
from entity._model.session import Session


class NetworkSession(Session):

    network = models.ForeignKey(
        verbose_name="Ağ Cihazı", to=Network, on_delete=models.CASCADE, name="network_session"
    )

    class Meta:
        verbose_name = "Ağ Cihazı Oturum/Giriş Bilgisi"
        verbose_name_plural = "Ağ Cihazı Oturum/Giriş Bilgileri"
