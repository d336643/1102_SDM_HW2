from django.core.management.base import BaseCommand
from order.models import *
'''
def __str__(self) -> str:
		return f"{self.order} includes {self.quantity} {self.item}"
'''

# env 1
import time

o = Order(username="Euni")
i = Item(name="Apple")

os = []
start_time = time.time()
for k in range(10000):
	os.append(OrderItem(order=o, item=i, quantity=100))

print(f"create: {time.time() - start_time}")
print("")


tmp=[]
start_time = time.time()
for i in range(10000):
	for o in os:
		tmp.append(str(o))
print(f"read: {time.time() - start_time}")
print("")

