from django.contrib import admin
from .models import Property, PropertyImage


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'city', 'price', 'bedrooms', 'bathrooms', 'property_type', 'is_published', 'is_featured'
    )
    list_filter = ('city', 'property_type', 'is_published', 'is_featured')
    search_fields = ('title', 'city', 'address')
    list_editable = ('is_published', 'is_featured')
    inlines = [PropertyImageInline]


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'sort_order')


