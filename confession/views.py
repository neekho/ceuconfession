from django.shortcuts import render
from . models import Confession
# Create your views here.


def home(request):

    context = {
        # 'confessions': Confession.objects.filter(moderated=True)
        'confessions': Confession.objects.all()

    }


    return render(request, "confession/attempt.html", context)


def about(request):

    context = {
        # 'confessions': Confession.objects.filter(moderated=True)
        'confessions': Confession.objects.all()

    }

    return render(request, "confession/about.html", context)

