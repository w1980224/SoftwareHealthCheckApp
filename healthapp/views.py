from django.shortcuts import render
from .models import Card, Vote, Team
from django.db.models import Count

def summary_view(request):
    teams = Team.objects.all()
    cards = Card.objects.all()
    data = []

    for team in teams:
        team_data = {'team': team.name, 'cards': []}
        for card in cards:
            votes = Vote.objects.filter(team=team, card=card)
            summary = votes.values('vote').annotate(count=Count('vote'))
            vote_counts = {'green': 0, 'amber': 0, 'red': 0}
            for item in summary:
                vote_counts[item['vote']] = item['count']
            team_data['cards'].append({
                'card': card.title,
                'votes': vote_counts
            })
        data.append(team_data)

    return render(request, 'healthapp/summary.html', {'summary': data})
