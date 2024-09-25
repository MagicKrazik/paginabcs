# models.py
from django.db import models
from django.conf import settings
import os

class PDFFile(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    filename = models.CharField(max_length=255)  # Store just the filename
    preview_image = models.ImageField(upload_to='pdf_previews/')

    def __str__(self):
        return self.title

    @property
    def file_path(self):
        return os.path.join(settings.STATIC_URL, 'pdf', self.filename)