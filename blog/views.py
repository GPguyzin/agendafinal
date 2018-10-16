from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm, PostCad
from .models import Post, Comment, PostCd
from django.utils.timezone import localdate
from datetime import datetime
from events.models import Event


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    day = datetime(localdate().year, localdate().month, localdate().day)
    context = {

        'events': Event.objects.filter(
            date='{:%Y-%m-%d}'.format(day)).order_by('-priority', 'event'),
        'form': form

    }
    return render(request, 'blog/post_edit.html', context)




@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    day = datetime(localdate().year, localdate().month, localdate().day)
    context = {

        'events': Event.objects.filter(
            date='{:%Y-%m-%d}'.format(day)).order_by('-priority', 'event'),
        'form':form

    }

    return render(request, 'blog/post_edit.html', context)

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def post_cad(request):
    posts = PostCd.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_cad.html', {'posts': posts})



def post_ncad(request):
    if request.method == "POST":
        form = PostCad(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detailcad', pk=post.pk)
    else:
        form = PostCad()
        return render(request, 'blog/post_ncad.html', {'form': form})

def post_detailcad(request, pk):
    post = get_object_or_404(PostCd, pk=pk)
    return render(request, 'blog/post_detailcad.html', {'post': post})


def post_editcad(request, pk):
    post = get_object_or_404(PostCd, pk=pk)
    if request.method == "POST":
        form = PostCad(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detailcad', pk=post.pk)
    else:
        form = PostCad(instance=post)
    return render(request, 'blog/post_ncad.html', {'form': form})

def post_remove2(request, pk):
    post = get_object_or_404(PostCd, pk=pk)
    post.delete()
    return redirect('post_cad')








