from django.contrib import admin
from .models import PDFModel

# Register your models here.
@admin.register(PDFModel)
class PDFAdmin(admin.ModelAdmin):
    list_display = ['id', 'count', 'pdf']
