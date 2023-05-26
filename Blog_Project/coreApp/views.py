from django.shortcuts import render, get_object_or_404, redirect
from .models import Twit
from .forms import AddPostForm, NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import FavoritePost, Twit
from django.contrib import messages
from django.urls import reverse
def homePage(request):
    twits = Twit.objects.all().order_by('-postDate')
    return render(request, "app/home.html", {
        'twits': twits
    })

def postDetail(request, pk):
    twit = get_object_or_404(Twit, pk=pk)
    return render(request, "app/post-detail.html", {
        'twit': twit
    })

def addPost(request):

    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.userPost = request.user
            form.save()
        return redirect("homePage")
    else:
        form = AddPostForm()

    return render(request, "app/add-post.html", {
        'form': form
    })

def deletePost(request, pk):
    twit = get_object_or_404(Twit, pk=pk)
    if request.user == twit.userPost:
        if request.method == "POST":
            Twit.objects.filter(pk=pk).delete()
            return redirect("homePage")

    return render(request, "app/delete-post.html", {
        'twit': twit
    })

def editPost(request, pk):
    twit = get_object_or_404(Twit, pk=pk)
    form = AddPostForm(request.POST or None, instance=twit)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("postDetail", pk=twit.pk)
    return render(request, "app/edit-post.html", {
        'twit': twit,
        'form': form
    })

def signUp(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # message
            return redirect("homePage")
    else:
        form = NewUserForm()
    return render(request, "user/sign-up.html", {
        'form': form
    })

def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # message
                return redirect("homePage")
            else:
                pass
                # message
    else:
        form = AuthenticationForm()
    return render(request, "user/login.html", {
        'form': form
    })

def logoutUser(request):
    logout(request)
    # message
    return redirect("homePage")


def add_to_favorite(request, pk):
    post = get_object_or_404(Twit, pk=pk)

    # Проверяем, что пользователь аутентифицирован
    if not request.user.is_authenticated:
        messages.warning(request, 'Чтобы добавить пост в избранное, вам нужно войти в систему.')
        return redirect('login')

    # Создаем запись в таблице FavoritePost, если ее еще нет
    favorite_post, created = FavoritePost.objects.get_or_create(user=request.user, post=post)

    if created:
        messages.success(request, 'Пост добавлен в избранное.')
    else:
        messages.warning(request, 'Пост уже находится в избранном.')

    return redirect(reverse('postDetail', args=[post.pk]))


def remove_from_favorite(request, pk):
    post = Twit.objects.get(pk=pk)
    favorite_post = FavoritePost.objects.get(
        user=request.user,
        post=post
    )
    favorite_post.delete()
    return redirect('post_detail', pk=pk)

@login_required
def favorite_posts(request):
    # Получаем все избранные посты пользователя
    favorite_posts = FavoritePost.objects.filter(user=request.user)
    context = {'favorite_posts': favorite_posts}
    return render(request, 'user/favorite_posts.html', context)