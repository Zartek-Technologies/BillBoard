from django.shortcuts import render
from boards.models import BillBoard
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .forms import BillBoardForm, BillBoardUpdateForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from boards.choices import *
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class BillBordListView(LoginRequiredMixin, ListView):
    model = BillBoard
    template_name = 'user/home.html'  # <app>/<model>_<viewtype>.html
    queryset = BillBoard.objects.all()
    context_object_name = 'BillBord_list' 
    paginate_by = 3   
    ordering = ['city'] 

    def get_queryset(self):
        return BillBoard.objects.all().order_by('city')

class BillBoardCreateView(LoginRequiredMixin, CreateView):
    model = BillBoard
    template_name = 'user/addnew.html'
    form_class = BillBoardForm
    success_url = reverse_lazy('user:BillBord_list')

class BillBoardDeleteView(LoginRequiredMixin, DeleteView):
    model = BillBoard
    success_url = reverse_lazy('user:BillBord_list')

class BillBoardUpdateView(LoginRequiredMixin, UpdateView):
    model = BillBoard
    form_class = BillBoardUpdateForm
    template_name = 'user/EditBillBoard.html'    
    success_url = reverse_lazy('user:BillBord_list')

    def form_valid(self, form):            
        return super(BillBoardUpdateView, self).form_valid(form)

class BillBordSearchView(LoginRequiredMixin, ListView):
    model = BillBoard
    template_name = 'user/SearchBillBoard.html'  # <app>/<model>_<viewtype>.html    
    context_object_name = 'BillBord_list'    

    def get_queryset(self):
        search_query = self.request.GET.get('search', None)
        try:
            objects = BillBoard.objects.get(boardId= search_query)
        except BillBoard.DoesNotExist:
            return False       
        
        return BillBoard.objects.get(boardId= search_query)

class BillBordFilterView(LoginRequiredMixin, ListView):
    model = BillBoard
    template_name = 'user/home.html'  # <app>/<model>_<viewtype>.html    
    context_object_name = 'BillBord_list' 
    paginate_by = 3   
    ordering = ['boardId']

    def get_queryset(self):
        search_query = self.request.GET.get('search', None)
        try:
            objects = BillBoard.objects.filter(city= search_query)
        except BillBoard.DoesNotExist:
            return False        
        
        return BillBoard.objects.filter(city= search_query)