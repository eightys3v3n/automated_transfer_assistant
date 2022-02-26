from enum import Enum, auto
from dataclasses import dataclass
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import config
from data import Paycheque


class Unit(Enum):
  Days = auto()
  Months = auto()
  Years = auto()


class Account(Enum):
  Paycheque         = auto()
  RecurringExpenses = auto()
  Spending          = auto()
  CreditCard        = auto()


@dataclass
class Recurring:
  start_date: datetime
  amount: float
  frequency: float
  frequency_unit: Unit
  # Last()
  # Next()


class RecurringExpense(Recurring):
  # Transfers[]
  name: str
  notes: str
  pass

# Each recurring expense is composed of these transfers:
# On paycheque, 1/x amount from paycheque into recurring expenses
# On expense, amount from recurring expense into credit card


class RecurringTransfer(Recurring):
  # From Account
  # To Account
  pass

# Can be daily, weekly, bi-weekly, monthly, yearly, monthend



def next_of_recurring(recurring, now=None):
  # Returns the date of the next occurance
  if now is None:
    now = datetime.today()

  last_occurance = last_of_recurring(recurring, now=now)

  if recurring.frequency_unit == Unit.Days:
    next_occurance = last_occurance + timedelta(days=recurring.frequency)
    return next_occurance

  elif recurring.frequency_unit == Unit.Months:
    next_occurance = last_occurance + relativedelta(months=1)
    return next_occurance

  elif recurring.frequency_unit == Unit.Years:
    next_occurance = last_occurance + relativedelta(years=1)
    return next_occurance

  else:
    raise NotImplemented()
Recurring.next = next_of_recurring


def last_of_recurring(recurring, now=None):
  # Returns the date of the most recent previous occurance
  if now is None:
    now = today()

  if recurring.frequency_unit == Unit.Days:
    days_since_start = now - recurring.start_date
    occurances_since = days_since_start.days // recurring.frequency
    last_occurance = recurring.start_date + timedelta(days=occurances_since * recurring.frequency)
    return last_occurance

  elif recurring.frequency_unit == Unit.Months:
    last_occurance = recurring.start_date

    while last_occurance <= now:
      last_occurance += relativedelta(months=recurring.frequency)
    last_occurance -= relativedelta(months=recurring.frequency)

    return last_occurance

  elif recurring.frequency_unit == Unit.Years:
    last_occurance = recurring.start_date

    while last_occurance <= now:
      last_occurance += relativedelta(years=recurring.frequency)
    last_occurance -= relativedelta(years=recurring.frequency)

    return last_occurance

  else:
    raise NotImplemented()
Recurring.last = last_of_recurring
