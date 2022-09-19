from datetime import datetime, timedelta, date

users = [
    {'name': 'Ivan', 'birthday': '1982-09-30'},
    {'name': 'Alex', 'birthday': '1982-09-18'},
    {'name': 'Olga', 'birthday': '1982-09-25'},
    {'name': 'Oleg', 'birthday': '1982-09-24'},
    {'name': 'Vlad', 'birthday': '1982-09-26'}
]

def get_birthdays_per_week(users):
    
    def get_week_days(date):
        day_of_week = date.weekday()
        start_day = 7 - day_of_week
        end_day = start_day + 4
        weekend_date = date + timedelta(days=start_day - 2)
        start_date = date + timedelta(days=start_day)
        end_date = date + timedelta(days=end_day)
        birthday_dict = {}
        for i in range(start_day, end_day + 1):
            birthday_dict[(date + timedelta(days=i)).date().strftime('%A')] = []
        return weekend_date.date(), start_date.date(), end_date.date(), birthday_dict


    datenow = datetime.now()
    day_of_week = datenow.weekday()
    start_day = 7 - day_of_week
    end_day = start_day + 4
    weekend_date = (datenow + timedelta(days=start_day - 2)).date()
    start_date = (datenow + timedelta(days=start_day)).date()
    end_date = (datenow + timedelta(days=end_day)).date()
    birthdays = {}
    for i in range(start_day, end_day + 1):
        birthdays[(datenow + timedelta(days=i)).date().strftime('%A')] = []

    for el in users:
        days = None
        arr = map(int, el['birthday'].split('-'))
        user_birth = date(*arr)
        birth_date_now = date(datenow.year, user_birth.month, user_birth.day)
        if weekend_date <= birth_date_now <= end_date:
            if birth_date_now <= start_date:
                days = start_date.strftime('%A')
            else:
                days = birth_date_now.strftime('%A')
        if days:
            birthdays[days].append(el['name'])
           
    for key in birthdays:
        if birthdays[key]:
            print(key, ': ', ', '.join(birthdays[key]))

    return birthdays

get_birthdays_per_week(users)