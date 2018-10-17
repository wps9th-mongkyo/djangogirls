import random

from django.shortcuts import render


def post_list(request):
    context = {
        'pokemon': random.choice(['피카츄', '파이리', '꼬부기']),
    }
    # return render(
    #     request=request,
    #     template_name='blog/post_list.html',
    #     context=context
    # )
    return render(request, 'blog/post_list.html', context)
