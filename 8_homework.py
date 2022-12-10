import datetime
import calendar

users = [{'name': 'John',
          'birthday': datetime.date(1890, 12, 14)},
         {'name': 'Johns_twin',
          'birthday': datetime.date(1989, 12, 14)},
         {'name': 'Susan',
          'birthday': datetime.date(2007, 12, 11)},
         {'name': 'Alan',
          'birthday': datetime.date(1989, 12, 16)},
         {'name': 'Kevin',
          'birthday': datetime.date(1989, 12, 10)}]

res_weekdays = {"Saturday": [],
                "Sunday": [],
                "Monday": [],
                "Tuesday": [],
                "Wednesday": [],
                "Thursday": [],
                "Friday": []}


def date_range_list(start_date, end_date):
    date_list = []
    curr_date = start_date
    while curr_date <= end_date:
        format_date = curr_date.strftime("%m-%d")
        date_list.append(format_date)
        curr_date += datetime.timedelta(days=1)
    return date_list


def saturday_start_date(my_date):
    if my_date.weekday() < 6:
        return my_date + datetime.timedelta((5-my_date.weekday()) % 7)
    else:
        return my_date + datetime.timedelta((5-my_date.weekday()) % 7 - 7)


def friday_start_date(my_date):
    if my_date.weekday() > 4:
        return my_date + datetime.timedelta((3-my_date.weekday()) % 7+1)
    else:
        return my_date + datetime.timedelta(7+(4-my_date.weekday()) % 7)


def get_birthdays_per_week(users):
    my_date = datetime.date.today()
    #my_date = datetime.date(2022, 12, 10)

    saturday = saturday_start_date(my_date)
    friday = friday_start_date(my_date)

    date_list = date_range_list(saturday, friday)

    for user in users:
        format_user_birthday = user['birthday'].strftime("%m-%d")
        if format_user_birthday in date_list:
            temp_date = datetime.date(
                my_date.year, user['birthday'].month, user['birthday'].day)
            if calendar.day_name[temp_date.weekday()] == 'Saturday' or calendar.day_name[temp_date.weekday()] == 'Sunday':
                res_weekdays['Monday'].append(user["name"])
            else:
                res_weekdays[calendar.day_name[temp_date.weekday()]
                             ].append(user["name"])

    for key, value in res_weekdays.items():
        if value != []:
            print(f'{key}: {", ".join(value)}')


def main():
    get_birthdays_per_week(users)


if __name__ == "__main__":
    main()
