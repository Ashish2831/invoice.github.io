from django.contrib import admin
from .models import PDFModel

# Register your models here.
@admin.register(PDFModel)
class PDFAdmin(admin.ModelAdmin):
    list_display = ['id', 'count', 'pdf']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()
        return super().delete_queryset(request, queryset)
