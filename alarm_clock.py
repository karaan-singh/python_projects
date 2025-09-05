import datetime
import time

alarm_time = input("Set alarm time (HH:MM:SS, 24-hour format): ")

print(f"Alarm set for {alarm_time}. Type 'quit' and press Enter to exit early.")

while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        print("⏰ Alarm! Time's up!")
        break
    # Check for user input to quit
    if time.time() % 10 < 1:  # Every ~10 seconds, prompt for quit
        user_input = input("Type 'quit' to exit or press Enter to continue: ")
        if user_input.lower() == 'quit':
            print("Alarm cancelled.")
            break
    time.sleep(1)