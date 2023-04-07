# To calculate minutes and seconds from seconds:
# 7600 sec / 60 =  126.6666666666667(126 minutes)
# 0.6666666666667 * 60 = 40 sec(rounded).

###########################################
# hours, minutes, seconds from seconds:


print("12345 sec in hours, minutes, seconds format")
print()
hours = 12345 // 3600  # divide seconds by 60 min and 60 secs, without a remainder
print(hours)
minutes = 12345 % 3600 // 60  # first get remained seconds of hours, then divide it by 60 seconds without a remainder
print(minutes)
seconds = 12345 % 60  # get remained seconds of minutes
print(seconds)
print()
print("12345 sec is", hours, "hours", minutes, "minutes", seconds, "seconds")
