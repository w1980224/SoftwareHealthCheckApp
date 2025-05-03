from django.shortcuts import render
from .models import Card, Vote, Session

def summary_view(request):
    cards = Card.objects.all()
    card_data = []
    
    session = Session.objects.filter(is_active=True).first()
    print("ACTIVE SESSION:", session)

    if session:
        for card in cards:
            votes = Vote.objects.filter(card=card, session=session)
            print(f"Card: {card.title}, Votes: {votes.count()}")

            if votes.exists():
                green = votes.filter(vote_value='green').count()
                amber = votes.filter(vote_value='amber').count()
                red = votes.filter(vote_value='red').count()
                improving = votes.filter(progress=True).count()

                card_data.append({
                    'card': card,
                    'total_votes': votes.count(),
                    'green': green,
                    'amber': amber,
                    'red': red,
                    'improving': improving,
                })

    print("FINAL DATA:", card_data)
    return render(request, 'summary.html', {'card_data': card_data})

