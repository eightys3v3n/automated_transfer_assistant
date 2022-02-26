from datetime import timedelta, datetime
from data import *
from database import *
from data_structures import *




def latest_balance():
  # Returns the correct balance for Recurring Expenses Account.
  pass


def generate_transfer(expense):
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
