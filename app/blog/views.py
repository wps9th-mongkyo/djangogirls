from django.http import HttpResponse
from django.template import loader


def post_list(request):
    template = loader.get_template('blog/post_list.html')
    context = {}
    content = template.render(context, request)
    return HttpResponse(content)
