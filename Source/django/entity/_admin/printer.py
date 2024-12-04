from django.contrib import admin
from entity._model.printer import Printer
from entity._admin.printer_session import PrinterSessionInline


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Printer._meta.fields]
    list_display_links = [field.name for field in Printer._meta.fields]
    search_fields = [field.name for field in Printer._meta.fields]
    readonly_fields = [
        "user",
    ]

    save_on_top = True

    inlines = [
        PrinterSessionInline,
    ]

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.user = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        """
        Given an inline formset save it to the database.
        """
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.save()
            formset.save()