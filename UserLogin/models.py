from django.db import models
import os

# Create your models here.
class PDFModel(models.Model):
    count = models.IntegerField(default=0)
    pdf = models.FileField(upload_to='pdfs/')

    def delete(self):
        if os.path.isfile(self.pdf.path):
            os.remove(self.pdf.path)
        super(PDFModel, self).delete()
