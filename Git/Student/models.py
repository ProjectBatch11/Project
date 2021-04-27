from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

	
# class User(AbstractUser):
# 	t = (
# 		(1,'Medicinist'),
# 		(2,'Org'),
# 		(3,'Anonymous'),
# 		)
# 	role = models.IntegerField(default=3,choices=t,max_length=5)
