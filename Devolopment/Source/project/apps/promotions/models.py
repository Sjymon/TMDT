from django.db import models

from product.models import Product
# Create your models here.
class Promotion(models.Model):
	id_promotion = models.AutoField(primary_key=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='promotion_for_product')
	name_promotion = models.CharField(max_length=50, unique=True)
	created = models.DateTimeField()
	dateend = models.DateTimeField()
	discount = models.FloatField(default=0)

	def __str__(self):
		return self.name_promotion

	# def save(self, *args, **kwargs):
	# 	if Promotion.objects.all():
	# 		id_last = Promotion.objects.all().last().id + 1
	# 	else:
	# 		id_last = 1
	# 	self.id_promotion = "PMO" + str(id_last)
	# 	super(Promotion, self).save(*args, **kwargs)