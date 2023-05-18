from django.contrib import admin
from core.models import (Client,Address,VAT,Category,Product,Photo,Order,OrderDetail,CartLine)
# Register your models here.
admin.site.register(Client)
admin.site.register(Address)
admin.site.register(VAT)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Photo)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(CartLine)