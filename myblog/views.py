from django.shortcuts render

def voting_page(request):
    return render(request, 'blog/voting.html')
