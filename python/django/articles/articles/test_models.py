from django.test import TestCase
from articles.models import Article, Reporter
from datetime import date
class mocks:
    pub_date = date(2005, 7, 27)

class AnimalTestCase(TestCase):
    def setUp(self):
        r = Reporter.objects.create(first_name='John', last_name='Smith', email='dumb_email')
        Article.objects.create(id=None, headline='Extra!', pub_date=mocks.pub_date, reporter=r)

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        extra = Article.objects.get(headline='Extra!')
        self.assertEqual(extra.pub_date, mocks.pub_date)