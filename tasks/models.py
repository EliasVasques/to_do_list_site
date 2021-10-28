from typing import Optional
from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.

class Task(models.Model):
    title = CharField(max_length=50)
    description = TextField()
    situation = CharField(max_length=5, default='doing')

    def __str__(self) -> str:
        return self.title
