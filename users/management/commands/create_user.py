from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='sky@pro.com',
            first_name='test',
            last_name='test',
            is_staff=False,
            is_superuser=False,
            is_active=True,
        )
        user.set_password('123qwe456')
        user.save()