def get_weekday(day, month, year):
    # Step 1: Weekday Map
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    # Step 2: Century Anchor Days
    # 1800s: Friday (5), 1900s: Wednesday (3), 2000s: Tuesday (2), 2100s: Sunday (0)
    century_prefix = (year // 100)
    if century_prefix == 18: anchor = 5
    elif century_prefix == 19: anchor = 3
    elif century_prefix == 20: anchor = 2
    elif century_prefix == 21: anchor = 0
    else:
        # For dates outside 1800-2199, use the 400-year cycle
        cyc = [2, 0, 5, 3] # Index for centuries % 4
        anchor = cyc[(century_prefix - 20) % 4]

    # Step 3: Calculate the Year's Doomsday
    last_two_digits = year % 100
    a = last_two_digits // 12
    b = last_two_digits % 12
    c = b // 4
    
    # Sum of steps + century anchor
    total = a + b + c + anchor
    year_doomsday = total % 7 # This is the weekday that all "doomsdays" fall on this year

    # Step 4: Identify the closest "Doomsday" date for the given month
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    # Standard Doomsday dates (4/4, 6/6, 8/8, 10/10, 12/12, etc.)
    doomsdays = {
        1: 32 if is_leap else 31, # Jan 32 (Feb 1) or Jan 31
        2: 29 if is_leap else 28, # Last day of Feb
        3: 0,  # "March 0" is used as a reference for March 7, 14, 21, 28
        4: 4, 5: 9, 6: 6, 7: 11, 8: 8, 9: 5, 10: 10, 11: 7, 12: 12
    }
    
    # Calculate difference between target day and the month's doomsday
    target_doomsday = doomsdays[month]
    day_diff = day - target_doomsday
    
    # Final Calculation
    result_index = (year_doomsday + day_diff) % 7
    return days[result_index]

# --- Test Case: March 14, 2026 ---
test_day, test_month, test_year = 14, 3, 2026
print(f"The date {test_month}/{test_day}/{test_year} is a {get_weekday(test_day, test_month, test_year)}.")
