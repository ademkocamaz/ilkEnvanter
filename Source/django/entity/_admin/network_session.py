from django.contrib import admin
from entity._model.network_session import NetworkSession

class NetworkSessionInline(admin.StackedInline):
    model = NetworkSession
    extra = 0
    max_num = 100
    classes = ("collapse-entry",)
    readonly_fields=["user",]
    fk_name="network_session"
