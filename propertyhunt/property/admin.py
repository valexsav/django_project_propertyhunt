from django.contrib import admin
from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main info', {
            'fields': ('name', 'owner')
        }),
        ('Details', {
            'fields': ('price', 'location', 'area')
        }),
        ('Description', {
            'fields': ('description', 'photo')
        }),
    )

    # используется для отображения полей в списке объектов модели
    list_display = (
        'name',
        'owner',
        'price',
        'location',
        'area',
        'price_with_agency_fee',
        'price_with_agency_fee_2'
    )
    
    search_fields = ('name__istartswith',)

    # список полей,которые можно редактировать внутри списка
    list_editable = ('price', 'location', 'area')

    # дефолт сортировка
    ordering = ('-price',)

    list_filter = ('area', 'owner__role')


    def price_with_agency_fee_2(self, obj):
        return round(obj.price * 1.1)   
    
    price_with_agency_fee_2.short_description = 'Agency fee'

    actions = ['increase_price_by_10_percent', 'decrease_price_by_10_percent']

    def increase_price_by_10_percent(self, request, queryset):
        for obj in queryset:
            obj.price *= 1.1
            obj.save()

    increase_price_by_10_percent.short_description = 'Increase by 10%%'

    def decrease_price_by_10_percent(self, request, queryset):
        for obj in queryset:
            obj.price *= 0.9
            obj.save()

    decrease_price_by_10_percent.short_description = 'Decrease by 10%%'
