# defining time slots
time_slots = ['Morning', "Midday", "Afternoon", "Evening"]

# list for user heart rate inputs
heart_rate = []

#loop to input heart rate

for time in time_slots:
    bpm = int(input(f"Enter your heart rate for {time}: "))
    heart_rate.append([time, bpm])
   
#calculating average
total = 0
for rate in heart_rate:
    total = total + rate[1]
average = round(total/len(heart_rate))
print("your average heart rate for the day is: ", average)
