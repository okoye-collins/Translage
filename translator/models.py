from django.db import models
from jsonfield import JSONField
from accounts.models import UserProfile

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
    

LANGUAGE_CHOICES = (
    ('english','english'),
    ('Igbo','Igbo'),
    ('Yoruba','Yoruba'),
    ('Hausa','Hausa'),
)

class TextToTranslate(models.Model):
    text = models.TextField()

    def __str__(self):
        return f"{self.text}"


class Translation(models.Model):
    translator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    totranslate = models.ForeignKey(TextToTranslate, related_name='translations', on_delete=models.CASCADE)
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default='english')
    translation = models.TextField()

    def __str__(self):
        return f'{self.translator} -- transtation'
