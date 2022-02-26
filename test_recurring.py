from unittest import TestCase, main
from data_structures import *


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









  def test_last_just_past_months(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=1,
                          frequency_unit=Unit.Months,
                          amount=10)
    last = last_of_recurring(recurring, datetime(2022, 2, 26))

    self.assertEqual(datetime(2022, 2, 25), last)

  def test_last_right_before_months(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=1,
                          frequency_unit=Unit.Months,
                          amount=10)
    last = last_of_recurring(recurring, datetime(2022, 2, 24))

    self.assertEqual(datetime(2022, 1, 25), last)

  def test_last_same_day_months(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=1,
                          frequency_unit=Unit.Months,
                          amount=10)
    last = last_of_recurring(recurring, datetime(2022, 2, 25))

    self.assertEqual(datetime(2022, 2, 25), last)

  def test_last_just_past_diff_months(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=1,
                          frequency_unit=Unit.Months,
                          amount=10)
    last = last_of_recurring(recurring, datetime(2022, 3, 24))

    self.assertEqual(datetime(2022, 2, 25), last)


  def test_next_just_past_months(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=1,
                          frequency_unit=Unit.Months,
                          amount=10)
    next = next_of_recurring(recurring, datetime(2022, 2, 26))

    self.assertEqual(datetime(2022, 3, 25), next)

  def test_next_just_before_months(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=1,
                          frequency_unit=Unit.Months,
                          amount=10)
    next = next_of_recurring(recurring, datetime(2022, 1, 25))

    self.assertEqual(datetime(2022, 2, 25), next)

  def test_next_same_day_months(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=1,
                          frequency_unit=Unit.Months,
                          amount=10)
    next = next_of_recurring(recurring, datetime(2022, 2, 25))

    self.assertEqual(datetime(2022, 3, 25), next)

  def test_next_just_past_diff_months(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=1,
                          frequency_unit=Unit.Months,
                          amount=10)
    next = next_of_recurring(recurring, datetime(2022, 3, 24))

    self.assertEqual(datetime(2022, 3, 25), next)






  def test_last_just_past_years(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=1,
                          frequency_unit=Unit.Years,
                          amount=10)
    last = last_of_recurring(recurring, datetime(2022, 2, 26))

    self.assertEqual(datetime(2022, 2, 25), last)

  def test_last_right_before_years(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=1,
                          frequency_unit=Unit.Years,
                          amount=10)
    last = last_of_recurring(recurring, datetime(2022, 2, 24))

    self.assertEqual(datetime(2021, 2, 25), last)

  def test_last_same_day_years(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=1,
                          frequency_unit=Unit.Years,
                          amount=10)
    last = last_of_recurring(recurring, datetime(2022, 2, 25))

    self.assertEqual(datetime(2022, 2, 25), last)

  def test_last_just_past_diff_years(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=1,
                          frequency_unit=Unit.Years,
                          amount=10)
    last = last_of_recurring(recurring, datetime(2023, 1, 24))

    self.assertEqual(datetime(2022, 2, 25), last)


  def test_next_just_past_years(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=1,
                          frequency_unit=Unit.Years,
                          amount=10)
    next = next_of_recurring(recurring, datetime(2022, 2, 26))

    self.assertEqual(datetime(2023, 2, 25), next)

  def test_next_just_before_years(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=1,
                          frequency_unit=Unit.Years,
                          amount=10)
    next = next_of_recurring(recurring, datetime(2022, 1, 25))

    self.assertEqual(datetime(2022, 2, 25), next)

  def test_next_same_day_years(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=1,
                          frequency_unit=Unit.Years,
                          amount=10)
    next = next_of_recurring(recurring, datetime(2022, 2, 25))

    self.assertEqual(datetime(2023, 2, 25), next)

  def test_next_just_past_diff_years(self):
    recurring = Recurring(start_date=datetime(2022, 2, 25),
                          frequency=1,
                          frequency_unit=Unit.Years,
                          amount=10)
    next = next_of_recurring(recurring, datetime(2022, 3, 24))

    self.assertEqual(datetime(2023, 2, 25), next)




if __name__ == '__main__':
  main()
