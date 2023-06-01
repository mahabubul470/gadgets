from django.db import models
from django.utils import timezone


class FilteringOption(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Choice(models.Model):
    option = models.ForeignKey(FilteringOption, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value


class FilteringValue(models.Model):
    option = models.ForeignKey(FilteringOption, on_delete=models.CASCADE)
    values = models.ManyToManyField(Choice)

    def get_values_list(self):
        return [choice.value for choice in self.values.all()]

    def __str__(self):
        return ', '.join(self.get_values_list())


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    filters = models.ManyToManyField(FilteringValue)
    image = models.ImageField(upload_to='product_images/')
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
