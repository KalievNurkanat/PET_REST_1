from django.db import models
from beast_sets.settings import AUTH_USER_MODEL
from common.models import BaseModel
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.title}"


class Animal(BaseModel):
    title = models.CharField(max_length=35)
    max_run_speed = models.IntegerField()
    size = models.CharField()
    is_endangered = models.BooleanField(default=False)
    is_domestic = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    lives_in = models.CharField(max_length=60)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
    

        




