from enum import Enum, auto
from dataclasses import dataclass
from datetime import datetime


class Unit(Enum):
  Days = auto()


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
  pass

# Each recurring expense is composed of these transfers:
# On paycheque, 1/x amount from paycheque into recurring expenses
# On expense, amount from recurring expense into credit card


class RecurringTransfer(Recurring):
  # From Account
  # To Account
  pass

# Can be daily, weekly, bi-weekly, monthly, yearly, monthend


Paycheque = Recurring(
  start_date=datetime(2022, 2, 25),
  frequency=14,
  frequency_unit=Unit.Days,
  amount=300
)
# Feb 15, 339.8
# Jan 31, 381.25
# 15th and last day of the month.
# Effectively every 13-16 days -_-
# >= $300
# So paid $300 every two weeks on (Friday?)
