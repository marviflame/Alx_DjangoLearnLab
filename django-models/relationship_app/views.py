from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm



from .models import Book, UserProfile
from .models import Library

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def index(request):
    return render(request, 'relationship_app/index.html')


def list_books(request):
    items = Book.objects.all()
    book_list = [f"{i.title} by {i.author}" for i in items]
    return render(request, "relationship_app/list_books.html", {"book_list": book_list})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['library'] = self.object
        return context

def check_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(check_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')  

#Check for Librarian
def check_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(check_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

#Checking if member exists
def check_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(check_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

