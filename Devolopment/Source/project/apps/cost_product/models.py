from django.db import models

from product.models import Product

# Create your models here.
class Cost_Product(models.Model):
	id_cost = models.AutoField(primary_key=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cost_product')
	created = models.DateTimeField()
	dateend = models.DateTimeField()
	value = models.FloatField(default=0)

	def __str__(self):
		return str(self.product) + str(self.created)
