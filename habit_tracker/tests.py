from rest_framework import status
from rest_framework.test import APITestCase

from habit_tracker.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self) -> None:
        """Подготовка данных перед каждым тестом"""
        self.user = User.objects.create(
            email='test@test.com'
        )
        self.user.set_password('qwe123')
        self.user.save()
        response = self.client.post('/api/token/', {"email": "test@test.com", "password": "qwe123"})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_habits(self):
        """Тест создания модели Habit"""
        test = Habit.objects.create(place="garden", time="13:30",
                                    action="test",
                                    is_pleasant=True, frequency=1, reward=None, execution_time="00:02",
                                    is_publication=True, user=self.user, related_habit=None)
        response = self.client.post('/api/habits/create/', {"place": "garden", "time": "13:30",
                                                        "action": "test", "is_pleasant": True,
                                                        "frequency": 1, "reward": 'None', "execution_time": "00:02",
                                                        "is_publication": True, "user": self.user.pk})
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(test.place, 'garden')

    def test_list_habits(self):
        """Тест списка модели Habit"""
        self.test_create_habits()
        response = self.client.get('/api/habits/')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_get_habit(self):
        """Тест деталей модели Habit"""
        self.test_create_habits()
        response = self.client.get(f'/api/habits/detail/4/')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'id': 4, 'place': 'garden', 'time': '13:30:00',
                                           'action': 'test', 'is_pleasant': True, 'frequency': 1,
                                           'reward': 'None', 'execution_time': '00:02:00', 'is_publication': True, 'user': 2,
                                           'related_habit': None})

    def test_list_habits_public(self):
        """Тест списка публичности модели Habit"""
        self.test_create_habits()
        response = self.client.get('/api/habits/public/')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 2)
