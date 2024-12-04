from django.contrib import admin
from entity._model.device_session import DeviceSession

class DeviceSessionInline(admin.StackedInline):
    model = DeviceSession
    extra = 0
    max_num = 100
    classes = ("collapse-entry",)
    readonly_fields=["user",]
    fk_name="device_session"
