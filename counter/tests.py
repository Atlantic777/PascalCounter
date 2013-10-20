from django.test import TestCase
from models import *
from datetime import datetime


class SessionCreateTest(TestCase):
    def test_create_new_session(self):
        s = Session()
        self.assertFalse(s.date is None)

    def test_create_new_session_with_date(self):
        d = datetime.now()
        s = Session(date=d)
        self.assertTrue(s.date == d)

class SessionCounterTest(TestCase):
    def setUp(self):
        self.session = Session()

    def test_read_counter(self):
        self.assertEqual(self.session.counter, 0)

    def test_increase_counter(self):
        self.session.increase()
        self.assertEqual(self.session.counter, 1)
