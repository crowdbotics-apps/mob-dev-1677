from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Testing(models.Model):
    "Generated Model"
    tes = models.BigIntegerField()


class TES(models.Model):
    "Generated Model"
    ad = models.BigIntegerField()


class Hello(models.Model):
    "Generated Model"
    ads = models.BigIntegerField()


class AnotherTest(models.Model):
    "Generated Model"
    my_id = models.BigIntegerField()
    name = models.CharField(max_length=256,)
