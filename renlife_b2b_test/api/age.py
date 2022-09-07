import datetime

date = datetime.date.today()
year = date.year
month = date.month
if month < 10:
    month = str(0) + str(month)

def print_api_age(y:int = 0, d:int = 0):
    day = date.day
    this_day = day+d
    if this_day < 10:
        this_day = str(0) + str(this_day)
    age = str(year-y) + '-' + str(month) + '-' + str(this_day)
    # print(age)
    return age

class AssertAge():
    def max_age(self, max_vozrast):
        return print_api_age(y=max_vozrast + 1, d=0) + 'T00:00:00'

    def max_age_plus_1d(self, max_vozrast):
        return print_api_age(y=max_vozrast + 1, d=+1) + 'T00:00:00'

    def min_age(self, min_vozrast):
        return print_api_age(y=min_vozrast, d=0) + 'T00:00:00'

    def min_age_minus_1d(self, min_vozrast):
        return print_api_age(y=min_vozrast, d=-1) + 'T00:00:00'

    def error(self, zapros):
        return zapros['error']['data']['status']  == 'ERROR'

    def passed(self, zapros):
        return zapros['result']['insured'][0]['person_info']['birth_date']

