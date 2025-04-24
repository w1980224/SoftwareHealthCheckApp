from django.shortcuts render

def voting_page(request):
    return render(request, 'myblog/voting.html')
