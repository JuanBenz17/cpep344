hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Convert everything to minutes
total_minutes = hour * 60 + mins + dura

# Compute final hour and minutes
end_hour = (total_minutes // 60) % 24
end_mins = total_minutes % 60

print(f"{end_hour}:{end_mins:02d}")
