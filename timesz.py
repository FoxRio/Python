def format_duration(seconds):
    years = 0
    days = 0
    hours = 0
    minutes = 0
    answer = ""
    first = True
    if seconds > 31556926:
        years += seconds // 31556926
        seconds = seconds - years * 31556926
    if seconds > 86400:
        days += seconds // 86400
        seconds = seconds - days * 86400
    if seconds > 3600:
        hours += seconds // 3600
        seconds = seconds - hours * 3600
    if seconds > 60:
        minutes += seconds // 60
        seconds = seconds - minutes * 60

    if years > 1 and days > 1 and hours > 1 and minutes > 1 and seconds > 1:
        return f"{years} years, {days} days, {hours} hours, {minutes} minutes and {seconds} seconds"
    elif years == 1 and days == 1 and hours == 1 and minutes == 1 and seconds == 1:
        return f"{years} year, {days} day, {hours} hour, {minutes} minute and {seconds} second"
    elif year == 1 and days == 0 and hours == 0 and minutes == 0 and seconds == 0:
        return "1 year"
    elif year > 1 and days == 0 and hours == 0 and minutes == 0 and seconds == 0:
        return f"{years} years"


    if seconds == 1:
        answer += "and 1 second"
        first = False
    elif seconds > 1:
        answer += "and " + str(seconds) + seconds
        first = False


    if minutes == 1:
        if first:
            answer += "and 1 minute"
            first = False
        else:
            answer += " 1 minute"
    elif minutes > 1:
        if first:
            answer += "and" + str(minutes) + "minutes"
            first = False
        else:
            answer += ", " + str(minutes) + "minutes"


    if hours == 1:
        if first:
            answer += ""
print(format_duration(3662))




