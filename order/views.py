from ast import Try
from django.shortcuts import render

from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http.request import HttpRequest

from order.models import *

# Create your views here.
def indexView(request: HttpRequest):
	usernames = list(set([n[0] for n in Order.objects.all().values_list('username')]))
	return render(request, "index.html", { 'usernames': usernames })

def orderDetailView(request: HttpRequest, oid):
	try:
		order = Order.objects.get(id=oid)
		items = [item[0] for item in order.items.values_list('name')]
	except:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	return render(request, "order_detail_view.html", {"order":order, 'items':items})

@api_view(['GET'])
def search_orders(request):
	name = request.GET.get('name', None)
	if request.method == 'GET':
		orders =Order.objects.filter(username=name).values()
		return Response(orders, status=status.HTTP_200_OK)

@api_view(['GET'])
def order_detail(request, oid):
	try:
		order = Order.objects.get(id=oid)
	except:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		data = {"oid": order.id, "customer": order.username}
		items = [item[0] for item in order.items.values_list('name')]
		data["items"] = items
		return Response(data, status=status.HTTP_200_OK)
