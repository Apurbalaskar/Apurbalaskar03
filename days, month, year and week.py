def convert_days(total_days):
    years = total_days // 365
    remaining_days = total_days % 365

    months = remaining_days // 30
    remaining_days = remaining_days % 30

    weeks = remaining_days // 7
    days = remaining_days % 7

    return years, months, weeks, days


total_days = int(input("Enter the number of days: "))


years, months, weeks, days = convert_days(total_days)


print(f"{total_days} days is equivalent to:")
print(f"{years} year(s), {months} month(s), {weeks} week(s), and {days} day(s).")
