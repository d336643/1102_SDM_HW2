from django.urls import path
from order import views

urlpatterns = [
    path('', views.indexView),
    path('orders/<int:oid>', views.orderDetailView),
    path('search_orders', views.search_orders),
    # path('orders/<int:oid>', views.order_detail),
]
