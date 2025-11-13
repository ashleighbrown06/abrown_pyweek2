# Morning Chore Prioritizer
# Time available before leaving for work: 7:15 am - 9:30 am = 135 minutes

time_available = 135  # total minutes before work

# Estimated times for each chore (in minutes)
walk_dog = 30
feed_dog = 5
run_dishwasher = 5
vacuum_living_room = 20
make_bed = 10
sweep_kitchen = 15

# Priority order (you can change this as you like)
# Dog-related chores are most urgent, then cleaning tasks
total_time_needed = walk_dog + feed_dog + run_dishwasher + vacuum_living_room + make_bed + sweep_kitchen

print("Good morning! Let's plan your chores before work.")
print(f"Total time available: {time_available} minutes")
print(f"Total estimated time for all chores: {total_time_needed} minutes\n")

if total_time_needed <= time_available:
    print("✅ You have enough time to complete all your chores!")
    print("Recommended order:")
    print("1. Walk the dog 🐕")
    print("2. Feed the dog 🍲")
    print("3. Make your bed 🛏️")
    print("4. Run the dishwasher 🍽️")
    print("5. Sweep the kitchen 🧹")
    print("6. Vacuum the living room 🧽")

elif total_time_needed - time_available <= 15:
    print("⚠️ You're a bit short on time! Focus on the most important tasks:")
    print("1. Walk the dog 🐕")
    print("2. Feed the dog 🍲")
    print("3. Make your bed 🛏️")
    print("4. Run the dishwasher 🍽️")
    print("If you have time left, sweep the kitchen or vacuum quickly.")

else:
    print("⏰ You don’t have enough time for everything.")
    print("Do these in order of priority:")
    print("1. Walk the dog 🐕")
    print("2. Feed the dog 🍲")
    print("3. Make your bed 🛏️")
    print("If there’s extra time, run the dishwasher or sweep the kitchen.")
    print("You may need to skip vacuuming today.")

print("\nHave a productive morning! ☀️")
