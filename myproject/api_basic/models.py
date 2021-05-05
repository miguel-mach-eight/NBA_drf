from django.db import models

# Create your models here.
class NBAplayers(models.Model):
	first_name = models.CharField(max_length=100)
	h_inches = models.DecimalField(max_digits=5, decimal_places=2)
	h_meters = models.DecimalField(max_digits=5, decimal_places=2)
	last_name = models.CharField(max_length=120)

	def __str__(self):
		return self.first_name