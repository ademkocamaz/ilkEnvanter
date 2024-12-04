from django.contrib import admin
from entity._model.computer import Computer
from entity._admin.computer_session import ComputerSessionInline


@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Computer._meta.fields]
    list_display_links = [field.name for field in Computer._meta.fields]
    search_fields = [field.name for field in Computer._meta.fields]
    readonly_fields = [
        "user",
    ]

    save_on_top = True

    inlines = [
        ComputerSessionInline,
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
