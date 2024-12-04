from django.contrib import admin
from entity._model.printer_session import PrinterSession

class PrinterSessionInline(admin.StackedInline):
    model = PrinterSession
    extra = 0
    max_num = 100
    classes = ("collapse-entry",)
    readonly_fields=["user",]
    fk_name="printer_session"
