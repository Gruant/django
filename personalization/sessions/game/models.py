from django.db import models


class Player(models.Model):
    player_id = models.CharField(max_length=128, verbose_name='id игрока')


class Game(models.Model):
    game_id = models.CharField(max_length=128, verbose_name='id игры')
    is_finished = models.BooleanField(verbose_name='Игра завершена', default=False)
    is_active = models.BooleanField(verbose_name='Игра завершена, но не просмотрена создателем', default=True)
    number = models.IntegerField(default=0)
    players = models.ManyToManyField(Player, through='PlayerGameInfo', related_name='game_info')
    god = models.ForeignKey(Player, on_delete=models.CASCADE, default=None)


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    winner = models.BooleanField(verbose_name='Победитель', default=False)




