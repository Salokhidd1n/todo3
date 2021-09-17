from django.contrib import admin
from .models import Todo
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display =("pk","title","description","created_at")
    search_fields = ("title",)
    list_filter = ("created_at",)

admin.site.register(Todo, TodoAdmin)