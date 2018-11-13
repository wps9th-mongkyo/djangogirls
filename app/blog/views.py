import random
import re
from datetime import timezone

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.order_by('-created_date')
    # content = ''
    # content + '<ul>'
    # for post in posts:
    #     content += f'<li>{ post.title }</li>'
    # content += '</ul>'
    context = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post
    }

    return render(request, 'blog/post_detail.html', context)


def post_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.author
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_create.html', {'form': form})