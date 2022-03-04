from django.core.management.base import BaseCommand

from faker import Faker
from faker_vehicle import VehicleProvider

from order.models import *
from random import randint

ITEM_SIZE = 20
USERNAME_SIZE = 15
ORDER_SIZE = 50
ITEM_NUM_PER_ORDER_LOWER = 1
ITEM_NUM_PER_ORDER_UPPER = 3
ITEM_QUANTITY_LOWER = 1
ITEM_QUANTITY_UPPER = 5
ORDER_NUM_PER_USER_LOWER = 2
ORDER_NUM_PER_USER_UPPER = 5


class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		names = [] #['山口 桃子', '李鈺婷', '張佳蓉'...]
		orders = [] #[Order...]
		items = [] #[Item...]

		# create random fake names
		fake = Faker(['ko_KR', 'zh_TW', 'ja_JP'])
		for i in range(USERNAME_SIZE):
			names.append(fake.name())


		# create random fake items and store Item objects
		fake = Faker()
		fake.add_provider(VehicleProvider)
		for i in range(ITEM_SIZE):
			i = Item(name=fake.unique.vehicle_make())
			i.save()
			items.append(i)

		# create Order/OrderItem objects
		for uname in names:
			order_num = randint(ORDER_NUM_PER_USER_LOWER, ORDER_NUM_PER_USER_UPPER)
			for i in range(order_num):
				o = Order(username=uname)
				o.save()
				orders.append(o)

				item_num = randint(ITEM_NUM_PER_ORDER_LOWER, ITEM_NUM_PER_ORDER_UPPER)
				for j in range(item_num):
					OrderItem(order=o, item=items[randint(0,ITEM_SIZE-1)], quantity=randint(ITEM_QUANTITY_LOWER,ITEM_QUANTITY_UPPER)).save()

				
