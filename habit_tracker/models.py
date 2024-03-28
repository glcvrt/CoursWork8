from django.db import models

from users.models import User, NULLABLE


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=150, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE,
                                         verbose_name='Связанная привычка')
    frequency = models.IntegerField(default=1, verbose_name='Периодичность')
    reward = models.CharField(max_length=150, verbose_name='Вознаграждение', **NULLABLE)
    execution_time = models.TimeField(verbose_name='Время на выполнение')
    is_publication = models.BooleanField(default=True, verbose_name='Признак публичности')

    def __str__(self):
        return f'{self.user} будет {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
