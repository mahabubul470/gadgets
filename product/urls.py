from django.urls import path

from .views import ProductListView, FilterJsonview

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product-list'),
    path('filter', FilterJsonview.as_view(), name='filtered-products')
]
