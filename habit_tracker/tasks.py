from datetime import datetime

import requests
from celery import shared_task
from config.settings import TELEGRAM_TOKEN
from habit_tracker.models import Habit


@shared_task
def send_habit_message():
    time_now = datetime.now()
    for hab in Habit.objects.all():
        if hab.time.minute == time_now.minute and hab.time.hour == time_now.hour:
            message = f"Не забудьте {hab.action} в {hab.place}"
            url_get_updates = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?&chat_id=5111843782&text={message}"
            response = requests.get(url_get_updates)
