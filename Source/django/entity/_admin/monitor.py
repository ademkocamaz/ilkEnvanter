from django.contrib import admin
from entity._model.monitor import Monitor
from entity._admin.session import SessionInline


@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Monitor._meta.fields]
    list_display_links = [field.name for field in Monitor._meta.fields]
    search_fields = [field.name for field in Monitor._meta.fields]
    readonly_fields = [
        "user",
    ]

    save_on_top = True

    inlines = [
        SessionInline,
    ]

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.user = request.user
        obj.save()
