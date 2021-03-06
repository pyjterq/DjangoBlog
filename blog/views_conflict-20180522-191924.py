from django.shortcuts import render
from django.conf import settings
from .models import Entry
# from .models import Category
from django.utils import timezone
from django.http import HttpResponse

# Create your views here.


def simple_view(request):
    return render(request, 'post.html', {
        'EXTERNAL_STATIC': settings.EXTERNAL_STATIC
    })


def post_list(request):
    entries = Entry.objects.filter(
        posted_at__lte=timezone.now()
    ).order_by('-posted_at')
    return render(request, 'posts_list.html', {'entries': entries})


def show_entry(request, slug):
    # return HttpResponse(slug)
    entry = Entry.objects.get(slug=slug)
    return render(request, 'post.html', {'entry': entry})
