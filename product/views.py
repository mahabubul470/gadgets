from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Product, FilteringOption, Choice, FilteringValue
from django.db.models import Q


class ProductListView(View):

    def get(self, request):

        filter_choices = Choice.objects.all()
        filter_options = FilteringOption.objects.all()
        object_list = Product.objects.all()
        context = {'filter_choices': filter_choices,
                   'filter_options': filter_options,
                   "object_list": object_list}
        return render(request, 'product/product_list.html', context)


class FilterJsonview(View):

    def get(self, request):
        filter_params = request.GET
        filters = dict(filter_params)
        gadgets = Product.objects.all()
        filtered_products = gadgets  # Initialize with all products
        # Filter the filter options and filter choices from the query parameters to filter out the products
        for filter_option, filter_choices in filters.items():
            filter_value_ids = []
            for choice in filter_choices:
                filter_option_obj = FilteringOption.objects.get(name=filter_option)
                filter_value = FilteringValue.objects.filter(option=filter_option_obj, values__value=choice).first()
                if filter_value:
                    filter_value_ids.append(filter_value.id)
            filtered_products = filtered_products.filter(filters__in=filter_value_ids)

        # Return all the product if the query params are empty
        if len(filters) == 0:
            filtered_products = gadgets

        # Create a list of dictionaries representing the filtered products
        products_data = []
        for product in filtered_products:
            product_data = {
                'name': product.name,
                'price': product.price,
                'quantity': product.quantity,
                'created_at': product.created_at,
                'updated_at': product.updated_at,
                'image_url': product.image.url
            }
            products_data.append(product_data)

        # Return the filtered products as JSON response
        return JsonResponse(products_data, safe=False)
