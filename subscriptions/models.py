from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse

class StripeCustomer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class New(models.Model):
	views = models.IntegerField(default=0)
	name = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	upload = models.FileField(upload_to ='uploads/%Y/%m/%d/') 
	file_size = models.CharField(max_length=255)
	date = models.DateTimeField()
	tags = TaggableManager()

	def __str__(self):
		return self.name 

	def get_absolute_url(self):
		return reverse('detail', args=[self.id])

