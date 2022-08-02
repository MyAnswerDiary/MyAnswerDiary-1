from pyexpat import model
from django.db import models

class UserModel(models.Model):
    user_id = models.CharField(max_length=15)
    user_pw = models.CharField(max_length=128)
    user_name = models.CharField(max_length=15)

    def __str__(self):
        return self.userName

    class Meta:
        db_table = '유저'