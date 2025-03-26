def convertToSeconds(hours, minutes):
    seconds = (hours * 3600) + (minutes * 60)
    return seconds

def convertToHours(minutes):
    hours = minutes / 60
    return hours

print(convertToSeconds(3,25))
print(convertToHours(120))
