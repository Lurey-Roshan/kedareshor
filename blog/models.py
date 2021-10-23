from django.db import models
import datetime
# Create your models here.






class Notice(models.Model):
	name=models.CharField(max_length=255)
	date=models.DateField(auto_now_add=True)
	pic=models.ImageField(upload_to='notice/')



	def __str__(self):
		return self.name

