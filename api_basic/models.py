from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = [('read-only', 'read-only'), ('read-write', 'read-write'),]
    role = models.CharField(max_length=32, choices=ROLES, default='read-only')
# Create your models here.
class NBAplayers(models.Model):
	first_name = models.CharField(max_length=100)
	h_in = models.DecimalField(max_digits=5, decimal_places=2)
	h_meters = models.DecimalField(max_digits=5, decimal_places=2)
	last_name = models.CharField(max_length=120)

	def __str__(self):
		return self.first_name

