RecurringExpenses = []

RecurringTransfers = []


def add_expense(**,
                name,
                start_date,
                frequency,
                frequency_unit,
                amount,
                transfers,
                details):
  expense = RecurringExpense(
    name=name,
    start_date=start_date,
    frequency=frequency,
    frequency_unit=frequency_unit,
    amount=amount,
    transfers=transfers,
    details=details
  ),
  RecurringExpenses.append(expense)


def get_expenses():
  return RecurringExpenses
