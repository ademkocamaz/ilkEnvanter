from django.contrib import admin
from entity._model.printer import Printer

@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Printer._meta.fields]
    list_display_links = [field.name for field in Printer._meta.fields]
    search_fields = [field.name for field in Printer._meta.fields]
    readonly_fields= ["user",]

    save_on_top = True

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.user = request.user
        obj.save()