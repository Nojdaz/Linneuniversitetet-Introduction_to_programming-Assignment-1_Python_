seconds = float(input("Enter time is seconds: "))
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print("This corresponds to:", hour, "hours,",
      minutes, "minutes and", seconds, "seconds.")
