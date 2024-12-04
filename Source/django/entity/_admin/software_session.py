from django.contrib import admin
from entity._model.software_session import SoftwareSession

class SoftwareSessionInline(admin.StackedInline):
    model = SoftwareSession
    extra = 0
    max_num = 100
    classes = ("collapse-entry",)
    readonly_fields=["user",]
    fk_name="software_session"
