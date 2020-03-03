from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)




class Books_Categories(models.Model):
	categories_name = models.CharField(max_length=80)
	def __str__(self):
		return self.categories_name


class Announcement(models.Model):
	dis_num = models.CharField(max_length=80)
	offer_title = models.CharField(max_length=80) 
	offer_description = models.CharField(max_length=80) 
	def __str__(self):
		return self.offer_title


	
class Books_List(models.Model):
	newbook_id = models.ForeignKey(Books_Categories, on_delete=models.CASCADE,)
	book_name = models.CharField(max_length=80) 
	book_price = models.CharField(max_length=80) 
	books_description = models.CharField(max_length=80) 
	book_author_name = models.CharField(max_length=80) 
	book_image = models.ImageField(upload_to='upload_images', blank=True, null=True)
	def __str__(self):
		return self.book_name



class Plans(models.Model):
	plan_name = models.CharField(max_length=80) 
	plan_features = models.CharField(max_length=80) 
	plan_validity = models.CharField(max_length=80) 
	plan_prices = models.CharField(max_length=80) 
	def __str__(self):
		return self.plan_name



class seller_offer(models.Model):
	dis_num = models.CharField(max_length=80)
	offer_title = models.CharField(max_length=80) 
	offer_description = models.CharField(max_length=80) 
	def __str__(self):
		return self.offer_title

class Cart_user(models.Model):
	username = models.CharField(max_length=50)
	def __str__(self):
		return self.username



class Cart(models.Model):
	user_id = models.ForeignKey(Cart_user, on_delete=models.CASCADE)
	cart_bool = models.BooleanField(default=False)
	book_id = models.CharField(max_length=11, default='book_id')
	book_name = models.CharField(max_length=80) 
	book_author = models.CharField(max_length=80, default='book_author') 
	book_price = models.CharField(max_length=80)
	def __str__(self):
		return self.book_name


	





		




	
	
