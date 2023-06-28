from django.http import HttpResponse
from blog.models import Post, Category
from django.contrib.auth.forms import AuthenticationForm
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
# from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse


# Create your views here.
def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]
    # print(posts)

    cats = Category.objects.all()

    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'Home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()

    # print(post)
    return render(request, 'posts.html', {'post': post, 'cats': cats})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("/home")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/home/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

