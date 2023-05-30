def convert_time(time_string):
    hours, minutes = map(int, time_string.split(":"))
    meridian = "AM"
    if hours > 12:
        hours -= 12
        meridian = "PM"
    elif hours == 12:
        meridian = "PM"
    elif hours == 0:
        hours = 12
    return f"{hours:02}:{minutes:02} {meridian}"
a=input()
print(convert_time(a))
    