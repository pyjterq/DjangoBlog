from django.shortcuts import render
from django.conf import settings

# Create your views here.


def simple_view(request):
    return render(request, 'post.html', {
        'EXTERNAL_STATIC': settings.EXTERNAL_STATIC
    })
