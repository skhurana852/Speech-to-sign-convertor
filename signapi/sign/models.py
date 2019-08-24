from django.db import models

# Create your models here.
class Sign(models.Model):
    title = models.TextField()
    description = models.TextField(default='0000')

    def _str_(self):
        return self.title