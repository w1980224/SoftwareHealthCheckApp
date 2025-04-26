from django.shortcuts import render
from django.http import HttpResponseReDirect
from .models import Vote

def vote(request):
    if request.method == "POST":
        selected_option = request.POST.get('vote_option')

        if selected_option:
        vote_option = Vote.objects.get(id=selected_option)
        vote_option.votes += 1
        vote_option.save()
        return redirect('/')

    return HttpResponseRedirect('/request/')

    options = Vote.objects.all()

    return render(request, 'voting.html', {'options': options})

