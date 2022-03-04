from django.db import models

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=20)
	class Meta:
		db_table = 'SDMHW2"."item'

	def __str__(self) -> str:
		return self.name

class Order(models.Model):
	username = models.CharField(max_length=20)
	items = models.ManyToManyField(Item, through='OrderItem')

	class Meta:
		db_table = 'SDMHW2"."order'

	def __str__(self) -> str:
		return f"{self.username}'s order{self.id}"


class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField()

	class Meta:
		db_table = 'SDMHW2"."order_item'
	
	def __str__(self) -> str:
		return f"{self.order} includes {self.quantity} {self.item}"
