from django.contrib import admin
from .models import Pizza, Topping


# class ToppingsInLine(admin.TabularInline):
#     model = Topping
#     extra = 1
#     fk_name = 'name'


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'created_by', 'slug')
    # inlines = [ToppingsInLine, ]


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')









