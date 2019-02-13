from django.contrib import admin
from .models import Restaurant, Item, FavoriteRestaurant

admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(FavoriteRestaurant)
