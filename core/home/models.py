from django.db import models

# Create your models here.
# here we are making an schema of stundent

class student(models.Model):
    # id = models.AutoField() this is by default add my django and it's primary key
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    feepaid = models.BooleanField()



