from django.contrib import admin
from entity._model.session import Session

class SessionInline(admin.StackedInline):
    model = Session
    extra = 0
    max_num = 100
    classes = ("collapse-entry",)
    readonly_fields=["user",]
