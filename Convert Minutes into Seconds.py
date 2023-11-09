import random
def conversion(mins):
    seconds = mins * 60
    return seconds

mins = random.randrange(1440)
print("Minutes: ", mins)
convert = conversion(mins)
print("Seconds", convert)
