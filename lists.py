# Create a list of days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Initialize an empty list to store steps
steps = []

# Loop to get user input for each day
for day in days:
    step_count = int(input(f"How many steps did you take on {day}? "))
    steps.append(step_count)

# Display the steps recorded for each day
print("\nSteps recorded for each day:")
for day, step in zip(days, steps):
    print(f"{day}: {step} steps")

# Calculate and display the total number of steps taken in the week
total_steps = sum(steps)
print(f"\nTotal steps taken in the week: {total_steps}")

# Calculate and display the average number of steps taken
average = round(total_steps / len(steps))
print(f"Average steps taken per day: {average}")
