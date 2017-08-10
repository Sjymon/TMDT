from django.db import models

# Create your models here.
class Unit(models.Model):
	id_unit = models.AutoField(primary_key=True)
	name_unit = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name_unit