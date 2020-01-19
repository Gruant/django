from django.shortcuts import render
from .models import Player, Game, PlayerGameInfo
from .forms import Form
import random


def show_home(request):
    context = {}

    user_id = request.session.session_key
    if not user_id:
        user_id = request.session.session_key

    player = Player.objects.filter(player_id=user_id).first()
    if not player:
        player = Player.objects.create(player_id=user_id)

    games = Game.objects.filter(is_finished=False)
    done_games = games.filter(is_active=False)
    if done_games:
        game = done_games.first()
        if game.god == player:
            count = PlayerGameInfo.objects.filter(winner=True).get(game=game.id)
            context = {
                'count': count.count,
                'number': game.number,
                'owner': True
            }
            game.is_finished = True
            game.save()
        else:
            count = PlayerGameInfo.objects.filter(winner=True).get(game=game.id)
            context = {
                'count': count.count,
                'number': game.number
            }
    else:
        if not games:
            random_num = random.randint(1, 100)
            game = Game.objects.create(game_id=random.randint(1, 100), god=player, number=random_num)
            game.players.add(player)
            context['number'] = game.number
            request.session['game_id'] = game.game_id
        else:
            game = games.first()
            if game.god != player:
                game.players.add(player)
                context['form'] = Form()
            else:
                context['number'] = game.number

    if request.method == 'POST':
        game_count = PlayerGameInfo.objects.filter(game_id=game)
        count = game_count.get(player=player.id)
        num = int(request.POST.get('text'))
        real_num = int(game.number)

        if num > real_num:
            context['answer'] = "Cлишком большое число!"
            count.count += 1
            count.save()
        elif num < real_num:
            count.count += 1
            count.save()
            context['answer'] = "Cлишком маленькое число!"
        elif num == real_num:
            count.count += 1
            count.winner = True
            context['answer'] = "Успех"
            game.is_active = False
            game.save()
            count.save()

    return render(
        request,
        'home.html',
        context=context
    )
