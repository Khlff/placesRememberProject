from allauth.socialaccount.models import SocialAccount
from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from feedbacker.forms import FeedbackForm
from feedbacker.models import Feedback


class CreateFeedbackTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.client.login(username='testuser', password='testpass')
        self.url = reverse("create_feedback")

    def test_create_feedback(self):
        """
        Тест на корректное создание формы.
        """
        response = self.client.post(
            self.url,
            {'title': 'Test title', 'comment': 'test comment', 'latitude': 50,
             'longitude': 50}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        feedback = Feedback.objects.get(user=self.user) # noqa
        self.assertEqual(feedback.title, 'Test title')
        self.assertEqual(feedback.comment, 'test comment')
        self.assertEqual(feedback.latitude, 50)
        self.assertEqual(feedback.longitude, 50)

    def test_create_feedback_with_invalid_data(self):
        """
        Тест на некорректное создание формы.
        """
        response = self.client.post(self.url, {'fdwwcvcwvw': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'errorlist')

    def test_create_feedback_with_get_request(self):
        """
        Тест на использование корректного шаблона и наличие формы.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback_adding.html')
        self.assertIsInstance(response.context['form'], FeedbackForm)

    def test_create_feedback_with_unauthenticated_user(self):
        """
        Тест на создание фидбэка неавторизованным пользователем.
        """
        self.client.logout()
        response = self.client.get(self.url)
        self.assertRedirects(response,
                             f'{reverse("account_login")}?next={self.url}')


class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.client.login(username='testuser', password='testpass')
        self.url = reverse('home')

    def test_home_with_authenticated_user_without_social_account(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertEqual(list(response.context['feedbacks']), [])
        self.assertNotIn('first_name', response.context)
        self.assertNotIn('last_name', response.context)
        self.assertNotIn('photo', response.context)

    def test_home_with_authenticated_user_with_social_account(self):
        """
        Тест обращения к home авторизированным через вк пользователем +
         корректная отдача информации о нём.
        """
        SocialAccount.objects.create( # noqa
            provider='vk',
            user=self.user,
            extra_data={
                'first_name': 'Nikita',
                'last_name': 'Ivanov',
                'photo': 'https://example.com/photo.jpg'
            }
        )
        response = self.client.get(self.url)
        self.assertEqual(list(response.context['feedbacks']), [])
        self.assertEqual(response.context['first_name'], 'Nikita')
        self.assertEqual(response.context['last_name'], 'Ivanov')
        self.assertEqual(response.context['photo'],
                         'https://example.com/photo.jpg')

    def test_home_with_unauthenticated_user(self):
        """
        Тест обращения к home неавторизованным пользователем.
        """
        self.client.logout()
        response = self.client.get(self.url)
        self.assertRedirects(response,
                             f'{reverse("account_login")}?next={self.url}')
