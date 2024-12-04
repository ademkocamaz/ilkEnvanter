from django.contrib import admin
from entity._model.license_session import LicenseSession

class LicenseSessionInline(admin.StackedInline):
    model = LicenseSession
    extra = 0
    max_num = 100
    classes = ("collapse-entry",)
    readonly_fields=["user",]
    fk_name="license_session"
