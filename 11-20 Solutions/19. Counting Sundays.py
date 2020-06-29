common_year = 365
leap_year = 366

start_year = 1901
end_year = 2000

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

months = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}


def number_of_days_calculator(start, end):
    number_of_days = 0
    for year in range(start, end + 1):
        if year % 4 == 0:
            number_of_days += leap_year
        else:
            number_of_days += common_year
    return number_of_days


number_of_days = number_of_days_calculator(start_year, end_year)

current_month = None
month_counter = 0

current_weekday = None
weekday_counter = 1

current_year = start_year

current_date = 1

results = 0

for d in range(1, number_of_days + 1):
    current_month = list(months)[month_counter]
    current_weekday = days[weekday_counter]

    if current_weekday == "Sunday" and current_date == 1:
        results += 1

    current_date += 1
    weekday_counter += 1

    if weekday_counter > 6:
        weekday_counter = 0

    if current_date > months[current_month]:
        month_counter += 1
        current_date = 1

    if month_counter > 11:
        month_counter = 0
        current_year += 1

    if current_year % 4 == 0:
        months["February"] = 29
    else:
        months["February"] = 28
print(results)
