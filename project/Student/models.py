from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

	
class User(AbstractUser):
	t = (
		(1,'Medicinist'),
		(2,'Org'),
		(3,'Anonymous'),
		)
	role = models.IntegerField(default=3,choices=t)
	g=[('M',"Male"),('F','Female')]
	age=models.IntegerField(default=10)
	impf=models.ImageField(upload_to='Profiles/',default="Note.jpg")
	gender=models.CharField(max_length=10,choices=g)
	organization_name=models.CharField(max_length=120)
	phone_no=models.IntegerField(null=True)
	pan_no=models.CharField(max_length=20)
	address=models.CharField(max_length=200)

class MedicineInfo(models.Model):
	medicine_name=models.CharField(max_length=120)
	quantity=models.CharField(max_length=30)
	batch_no=models.IntegerField()
	category=models.CharField(max_length=120)
	production_date=models.DateField()
	entry_date=models.DateField()
	expiry_date=models.DateField()
	uid=models.ForeignKey(User,on_delete=models.CASCADE)
