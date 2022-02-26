
from datetime import timedelta, datetime
from data import *


def next_of_recurring(recurring, now=None):
  # Returns the date of the next occurance
  if now is None:
    now = datetime.today()

  last_occurance = last_of_recurring(recurring, now=now)

  if recurring.frequency_unit == Unit.Days:
    next_occurance = last_occurance + timedelta(days=recurring.frequency)
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

  else:
    raise NotImplemented()
Recurring.last = last_of_recurring


def first_paycheque_after_expense(expense):
  # returns the first paycheque date after a given recurring expense
  pass



def latest_balance():
  # Returns the correct balance for Recurring Expenses Account.
  pass


def add_recurring_expense(
    start_date     = None,
    frequency      = None,
    frequency_unit = None,
    amount         = None
  ):
  # Adds a recurring expense
  expense = RecurringExpense(
    start_date,
    frequency,
    frequency_unit,
    amount
  )

  # Allocate money from paycheque
  expense.transfers.append(
    RecurringTransfer(
      start_date     = Paycheque.next(),
      frequency      = Paycheque.frequency,
      frequency_unit = Paycheque.frequency_unit,
      amount         = None,                      # not sure yet
      from_account   = Account.Paycheque,
      to_account     = Account.RecurringExpenses
    )
  )

  # Pay expense
  expense.transfers.append(
    RecurringTransfer(
      start_date     = expense.next(),
      frequency      = expense.frequency,
      frequency_unit = expense.frequency_unit,
      amount         = expense.amount,                      # not sure yet
      from_account   = Account.RecurringExpenses,
      to_account     = Account.CreditCard
    )
  )


def generate_recurring_transfer():
  # Uses a recurring expense to generate all required recurring transfers
  #frequency = every payqueque
  #frequency_unit = every payqueque

  #Start date = first paycheque after expense start date

  #amount = divide expense amount by frequency into max number of days in a year. multiply that by max number of days in this frequency
  pass
