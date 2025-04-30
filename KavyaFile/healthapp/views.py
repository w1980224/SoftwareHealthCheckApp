from django.shortcuts import render
from .models import Card, Vote, Session

def summary_view(request):
    cards = Card.objects.all()
    card_data = []

    session = Session.objects.filter(is_active=True).first()
    print("SESSION:", session)

    if session:
        for card in cards:
            print("CARD:", card.title)
            votes = Vote.objects.filter(card=card, session=session)
            print("VOTE COUNT:", votes.count())

            if votes.exists():
                green = votes.filter(vote_value='green').count()
                amber = votes.filter(vote_value='amber').count()
                red = votes.filter(vote_value='red').count()
                improving = votes.filter(progress=True).count()

                print(f"{card.title} - Green: {green}, Amber: {amber}, Red: {red}")

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
