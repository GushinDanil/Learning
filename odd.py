from datetime import datetime


odds = [1, 3, 5, 7, 9, 11, 13.12,14, "Hello", 17, 19, 21, 23, 25, 27, 29, 31, 33,  37, 39, 41, 43]

right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("This minute seems a little odd")
elif right_this_minute != odds:
    print("not an odd minute")
else:
    print("fuck you")


