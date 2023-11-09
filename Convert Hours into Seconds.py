import random
def conversion(hours):
    seconds = hours * 3600
    return seconds

hours = random.randrange(24)
seconds = conversion(hours)
print("Hours:", hours)
print("Seconds:", seconds)
