from django.db import models
from jsonfield import JSONField

# Create your models here.

class File(models.Model):
    file = models.FileField(upload_to='documents/files')

    def __str__(self):
        return self.file.name
    
class SentenceTokenize(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    task = JSONField()

    def __str__(self):
        return f'{self.file}- task'