from django.shortcuts import redirect, render

from . models import Confession

from . forms import ConfessionForm
# Create your views here.


def home(request):

    if request.method == 'POST':
        form = ConfessionForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = ConfessionForm()

    context = {
        # 'confessions': Confession.objects.filter(moderated=True)
        'confessions': Confession.objects.all(),
        'form': form

    }


    return render(request, "confession/attempt.html", context)


def confess(request):
    if request.method == 'POST':
        form = ConfessionForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = ConfessionForm()
     



    return render(request, "confession/confession.html", {'form': form})





def about(request):

    context = {
        # 'confessions': Confession.objects.filter(moderated=True)
        'confessions': Confession.objects.all()

    }

    return render(request, "confession/about.html", context)

