from pyexpat import model
from statistics import mode
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Author
from django.urls import reverse_lazy

# Create your views here.

class AuthorListV(ListView):
    model = Author


class AuthorDetailView(DetailView):
    model = Author

    def get_context_data(self, **kwargs) :
        return super().get_context_data(**kwargs)


class AuthorCreateView(CreateView):
    model = Author
    fields = '__all__'


class AuthorUpdateView(UpdateView):
    model = Author
    fields = '__all__'
    template_name_suffix = '_update_form'


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author_list')