from database import *



Paycheque = Recurring(
  start_date=datetime(2022, 2, 25),
  frequency=14,
  frequency_unit=Unit.Days,
  amount=300
)
# Shaw contractor
# Feb 15, 339.8
# Jan 31, 381.25
# 15th and last day of the month.
# Effectively every 13-16 days -_-
# >= $300
# So paid $300 every two weeks on (Friday?)



expenses = [
  { name="Podcast Addict",
    start_date     = datetime(2021, 2, 22),
    frequency      = 1,
    frequency_unit = Unit.Months,
    amount         = 1.29,
    transfers      = [],
    notes          = "Podcast app on Google Play"},
  { name="Google Drive",
    start_date     = datetime(2019, 7, 23),
    frequency      = 1,
    frequency_unit = Unit.Years,
    amount         = 39.99,
    transfers      = [],
    notes          = "Google Drive 100GB storage"},
  { name="Protospace",
    start_date     = datetime(2019, 10, 19),
    frequency      = 1,
    frequency_unit = Unit.Months,
    amount         = 35,
    transfers      = [],
    notes          = "Maker space membership"},
  { name="Domain:eighty7.ca",
    start_date     = datetime(2019, 10, 7),
    frequency      = 1,
    frequency_unit = Unit.Years,
    amount         = 18,
    transfers      = [],
    notes          = ""},
  { name="License Renewal",
    start_date     = datetime(2014, 8, 30),
    frequency      = 5,
    frequency_unit = Unit.Years,
    amount         = 90,
    transfers      = [],
    notes          = ""},
  { name="Tidal",
    start_date     = datetime(2022, 3, 19),
    frequency      = 1,
    frequency_unit = Unit.Months,
    amount         = 14.99,
    transfers      = [],
    notes          = "Family account, split between mum and Stephen, might not continue"},
  { name="RemoDB",
    start_date     = datetime(2021, 1, 6),
    frequency      = 1,
    frequency_unit = Unit.Years,
    amount         = 3.09,
    transfers      = [],
    notes          = "SQL Database Client app on Google Play"},
  { name="BitWarden Premium",
    start_date     = datetime(2020, 4, 9),
    frequency      = 1,
    frequency_unit = Unit.Years,
    amount         = 15,
    transfers      = [],
    notes          = "Auto-fill 2FA codes; $10 USD"},
  { name="Bitwarden Family Organization",
    start_date     = datetime(2020, 4, 9),
    frequency      = 1,
    frequency_unit = Unit.Years,
    amount         = 17,
    transfers      = [],
    notes          = "Sharing between everyone at Mum's; $12 USD"},
  { name="CubeACR Call Recorder",
    start_date     = datetime(2021, 12, 13),
    frequency      = 1,
    frequency_unit = Unit.Years,
    amount         = 13.64,
    transfers      = [],
    notes          = "Android call recorder in Google Play"},
]

for expense in expenses:
  add_expense(**expense)
