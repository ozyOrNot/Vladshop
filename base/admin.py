from django.contrib import admin
from .models import *
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Notebook)
admin.site.register(notebook_has_Cart)
admin.site.register(SmartPhone)
admin.site.register(smartphone_has_Cart)
admin.site.register(Order)
# Register your models here.
