from django.contrib import admin
from entity._model.computer_session import ComputerSession

class ComputerSessionInline(admin.StackedInline):
    model = ComputerSession
    extra = 0
    max_num = 100
    classes = ("collapse-entry",)
    readonly_fields=["user",]
    fk_name="computer_session"
