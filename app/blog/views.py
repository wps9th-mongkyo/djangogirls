import os

from django.http import HttpResponse, request
from django.utils import timezone


def post_list(request):
    current_path = os.path.abspath(__file__)
    blog_path = os.path.dirname(current_path)
    app_path = os.path.dirname(blog_path)
    post_list_path = os.path.join(app_path, 'templates', 'blog', 'post_list.html')

    with open(post_list_path, 'rt') as f:
        content = f.read()
    return HttpResponse(content)
