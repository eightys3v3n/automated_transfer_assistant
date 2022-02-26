from unittest import TestCase, main
from data import *
from main import *


class TestRecurring(TestCase):
  def test_last_just_past(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=14,
                          frequency_unit=Unit.Days,
                          amount=10)
    last = last_of_recurring(recurring, datetime(2022, 2, 26))

    self.assertEqual(datetime(2022, 2, 25), last)


  def test_last_right_before(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=14,
                          frequency_unit=Unit.Days,
                          amount=10)
    last = last_of_recurring(recurring, datetime(2022, 2, 24))

    self.assertEqual(datetime(2022, 2, 25-14), last)


  def test_last_same_day(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=14,
                          frequency_unit=Unit.Days,
                          amount=10)
    last = last_of_recurring(recurring, datetime(2022, 2, 25))

    self.assertEqual(datetime(2022, 2, 25), last)


  def test_next_just_past(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=14,
                          frequency_unit=Unit.Days,
                          amount=10)
    next = next_of_recurring(recurring, datetime(2022, 2, 26))

    self.assertEqual(datetime(2022, 2, 25) + timedelta(days=recurring.frequency), next)


  def test_next_just_before(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=14,
                          frequency_unit=Unit.Days,
                          amount=10)
    next = next_of_recurring(recurring, datetime(2022, 2, 24))

    self.assertEqual(datetime(2022, 2, 25), next)


  def test_next_same_day(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=14,
                          frequency_unit=Unit.Days,
                          amount=10)
    next = next_of_recurring(recurring, datetime(2022, 2, 25))

    self.assertEqual(datetime(2022, 2, 25) + timedelta(days=recurring.frequency), next)


if __name__ == '__main__':
  main()
