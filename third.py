def greeting(seconds):
    hours = seconds //3600
    minutes = (seconds - hours *3600 ) // 60
    remaining_seconds = seconds - ( (hours * 3600) + (minutes * 60))
    return hours, minutes, remaining_seconds

hours, minutes, remaining_seconds = greeting(3900)

print(hours, minutes, remaining_seconds)
