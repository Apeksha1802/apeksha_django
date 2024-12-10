from django.db import models

# Create your models here.
class City(models.Model):
    name=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    pincode=models.IntegerField()
    class Meta:
        verbose_name_plural="cities"
    def __str__(self):
        return self.name