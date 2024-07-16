def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
result = is_year_leap(2020)
print(f"год 2020: {result}")
result = is_year_leap(2021)
print(f"год 2021: {result}")