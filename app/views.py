from django.shortcuts import render, redirect
from .models import Vote

def voting_page(request):
    if request.method == "POST":
        selected_option = request.POST.get('state')

    if selected_option:
        try:
           vote_option = Vote.objects.get(id=selected_option)
           vote_option.votes += 1
           vote_option.save()
           return redirect('/')
        except Vote.DoesNotExist:
            return render(request, 'voting.html', {'error': 'Invalid option selected.'})


    options = Vote.objects.all()
    return render(request, 'voting.html', {'options': options})

