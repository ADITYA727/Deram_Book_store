from .views import *
from django.urls import path, include

urlpatterns = [
path('', home, name="home"),
path('registration/', registration),
path('registration/go_registration/', go_registration),
path('login/', login ,name="login"),
path('help/', help),
path('logout/', user_logout),
path('login/go_login/', go_login),
path('check_username/', check_username),
path('book_detail/<int:id>', book_detail),
path('buy_books/<int:id>', buy_books),
path('add_cart/', add_cart),
path('delete_cart/', delete_cart),
path('search_book/', search_book),
path('add_to_cart/<int:id>', add_to_cart),
path('add_book', seller_add_book),
]
