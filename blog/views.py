from django.shortcuts import render

def voting_page(request):
    return render(request, 'blog/voting.html')
