from django.shortcuts import render, redirect
from .models import *
import json
from django.core import serializers
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
import json 
from django.core import serializers


# client = razorpay.Client(auth=("<YOUR_KEY>", "<YOUR_SECRET>"))

# Create your views here.

# @login_required
def home(request):
	if(request.user):
		username_id = request.user.id
		username = request.user
		user_data = User.objects.filter(id=username_id)
		user_type_flag = False
		for user_type in user_data:
			if(user_type.is_buyer):
				print('Buyer Login')
				cate = Books_Categories.objects.all()
				offer = Announcement.objects.all()
				books = Books_List.objects.all()
				new_books = Books_List.objects.all().order_by('-id')[:3]
				sellers = User.objects.filter(is_seller=True).order_by('-id')[:6]
				show_cart_add_btn = Cart.objects.all()
				return render(request,'main.htm',{'cate':cate,'offer':offer,'books':books,'new_books':new_books,'username':username,'sellers':sellers,'show_cart_add_btn':show_cart_add_btn})
			elif(user_type.is_seller):
				plan = Plans.objects.all()
				offer = seller_offer.objects.all()
				return render(request,'seller/seller_main.html',{'plan':plan,'offer':offer,'username':username})
	cate = Books_Categories.objects.all()
	offer = Announcement.objects.all()
	books = Books_List.objects.all()
	new_books = Books_List.objects.all().order_by('-id')[:3]
	sellers = User.objects.filter(is_seller=True).order_by('-id')[:6]
	return render(request,'main.htm',{'cate':cate,'offer':offer,'books':books,'new_books':new_books,'sellers':sellers})





def registration(request):
	return render(request,'registration.html')

def go_registration(request):
	if request.method == 'POST':
		buyer = request.POST.get('buyer')
		seller = request.POST.get('seller')
		username = request.POST.get('username')
		password = request.POST.get('password')
		password_hash = make_password(password)
		if str(buyer) == 'buyer_selected':
			print('buyer enter')
			buyer_data = User(username=username,password=password_hash,is_buyer=True)
			buyer_data.save()
		elif str(seller) == 'seller_selected':
			seller_data = User(username=username,password=password_hash,is_seller=True)
			seller_data.save()
		return HttpResponseRedirect(reverse('login'))	

def login(request):
	return render(request, 'login.htm')

def go_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		password_hash = make_password(password)
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				auth_login(request,user)
				return HttpResponseRedirect(reverse('home'))
			else:
				return HttpResponse("Your account was inactive.")
		else:
			print("Someone tried to login and failed.")
			print("They used username: {} and password: {}".format(username,password))
			return HttpResponse("Invalid login details given")
	return render(request, 'login.htm')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def help(request):
	return render(request, 'help.htm')



def check_username(request):
	if request.method == "GET":
		username = request.GET['username']
		if username:
			u = User.objects.filter(username=username).count()
			if u != 0:
				res = "Already In Use"
			else:
				res = "Ok"
		else:
			res = ""
		return HttpResponse('%s' % res)

@login_required
def book_detail(request, id):
	username = request.user
	book_detail = Books_List.objects.filter(id=id)
	print(book_detail,'##########')
	return render(request,'buyers/books_detail.html',{'book_detail':book_detail,'username':username})


@login_required
def buy_books(request, id):
	username = request.user
	book_detail = Books_List.objects.filter(id=id)
	book_cart = Cart.objects.all()
	len_cart = str(len(book_cart))
	print(id,'##########')
	return render(request,'buyers/buy_books.html',{'book_detail':book_detail,'username':username,'book_cart':book_cart,'len_cart':len_cart,})

@login_required
def add_cart(request):
	if request.method == "GET":
		print(request.user)
		book_name = request.GET['book_name']
		book_author = request.GET['book_author']
		book_price = request.GET['book_price']
		book_id = request.GET['book_id']
		print(book_id,'@@@@@@@@@@@@')
		if book_name and book_author and book_price and book_id:
			cart_user = Cart_user(username=request.user)
			cart_user.save()
			cart_data = Cart(user_id=cart_user,cart_bool=True,book_id=book_id,book_name=book_name,book_author=book_author,book_price=book_price)
			cart_data.save()
			book_no = Cart.objects.all()
			book_no = len(book_no)
		return HttpResponse('%s' % book_no)


@login_required
def add_to_cart(request, id):
	cart_user = Cart_user(username=request.user)
	return HttpResponseRedirect(reverse('home'))


@login_required
def delete_cart(request):
	if request.method == "GET":
		delete_id = request.GET['delete_id']
		if delete_id:
			cart_delete = Cart.objects.filter(book_id=delete_id)
			cart_delete.delete()
			book_no = Cart.objects.all()
			book_no = Cart.objects.all()
			book_no = str(len(book_no))
		return HttpResponse('%s' % book_no)


def search_book(request):
	if request.method == "GET":
		text = request.GET['text']
		if text:
			book_list = Books_List.objects.filter(book_name__icontains=text)
			data = serializers.serialize("json",book_list)
			if data =='[]':
				data = "Not Found"
			return HttpResponse(data)


def seller_add_book(request):
	return render(request,'seller/add_books.html')



