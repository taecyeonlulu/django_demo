from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=32)
    create_at = models.DateField()
    update_at = models.DateField()
