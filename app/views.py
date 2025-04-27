from django.shortcuts import render, redirect
from .models import Vote, Team, Card, Session
from django.contrib.auth.decorators import login_required
from django.http import Http404

def voting_page(request, team_id, session_id):
    try:
        team = Team.objects.get(id=team_id)
    except Team.DoesNotExist:
        raise Http404("Team does not exist")

    try:
        session = Session.objects.get(id=session_id)
    except Session.DoesNotExist:
        raise Http404("Session does not exist")

    cards = Card.objects.all()

    if request.method == "POST":
        selected_card_id = request.POST.get('card_id')
        selected_vote = request.POST.get('vote')
        selected_progress = request.POST.get('progress_status')

        if selected_card_id and selected_vote and selected_progress:
            try:
                card = Card.objects.get(id=selected_card_id)

                existing_vote = Vote.objects.filter(user=request.user, team=team, card=card).first()

                if existing_vote:
                   existing_vote.vote = selected_vote
                   existing_vote.progress_status = selected_progress
                   existing_vote.save()
                else:
                    Vote.objects.create(
                        user=request.user,
                        team=team,
                        session=session,
                        card=card,
                        vote=selected_vote,
                        progress_status=selected_progress
                    
                    )
            except Card.DoesNotExist:
                return render(request, 'voting.html', {'team': team, 'cards:' cards, 'error': 'Invalid card selected'})

            return redirect('voting.html', team_id=team.id)


    return render(request, 'voting.html', {
        'team': team, 
        'session' session,
        'cards': cards
    })


