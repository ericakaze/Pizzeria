from django.contrib import admin

from .models import Pizza, topping, new_comment
admin.site.register(Pizza)
admin.site.register(topping)
admin.site.register(new_comment)
