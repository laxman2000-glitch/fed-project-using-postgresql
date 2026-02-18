from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    father = models.CharField(max_length=255)
    number= models.CharField(max_length=20)
    pincode= models.IntegerField()

    def __str__(self):
        return f"{self.name}-{self.father}-{self.nummber}"

