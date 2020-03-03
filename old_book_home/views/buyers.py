from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
# from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

# from ..decorators import student_required
from ..forms import  BuyersSignUpForm
from .models import *


class StudentSignUpView(CreateView):
    model = User
    form_class = BuyersSignUpForm
    template_name = 'registration.html'
    def get_context_data(self, **kwargs):
        print(kwargs,'#######')
        kwargs['user_type'] = 'buyers'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

