from django.db import models

# Create your models here.

class Todo(models.Model):
    plan = models.TextField(max_length=100)
    status = models.BooleanField(default=False)
    def __str__(self):
        return(f"{self.id}. {self.plan}: {self.status}")