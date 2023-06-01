from django.contrib import admin
from .models import FilteringOption, Choice, FilteringValue, Product


class FilteringValueInline(admin.TabularInline):
    model = FilteringValue
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('filters',)

    def display_filters(self, obj):
        filters = obj.filters.all()
        return ', '.join(f'{fv.option}: {fv}' for fv in filters)

    display_filters.short_description = 'Filters'

    def display_options(self, obj):
        options = FilteringOption.objects.all()
        return ', '.join(f'{option}: {", ".join(option.choice_set.values_list("value", flat=True))}' for option in options)

    display_options.short_description = 'Options'

    list_display = ('name', 'price', 'quantity', 'display_filters')


admin.site.register(FilteringOption)
admin.site.register(Choice)
admin.site.register(FilteringValue)
admin.site.register(Product, ProductAdmin)
