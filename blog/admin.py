from django.contrib import admin
from core.models import (TagDict,Post,FavouritePost,Profile,Comment)

# Register your models here.


admin.site.register(TagDict)
admin.site.register(Post)
admin.site.register(FavouritePost)
admin.site.register(Profile)
admin.site.register(Comment)