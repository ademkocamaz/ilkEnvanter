from django.contrib import admin
from entity._model.network import Network

@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Network._meta.fields]
    list_display_links = [field.name for field in Network._meta.fields]
    search_fields = [field.name for field in Network._meta.fields]
    readonly_fields= ["user",]

    save_on_top = True

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.user = request.user
        obj.save()