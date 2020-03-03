from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Books_Categories)
admin.site.register(Announcement)
admin.site.register(Books_List)
admin.site.register(User)
admin.site.register(Plans)
admin.site.register(seller_offer)
admin.site.register(Cart)
admin.site.register(Cart_user)