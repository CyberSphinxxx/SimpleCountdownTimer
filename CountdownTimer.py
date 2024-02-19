import time

while True:
    try:
        duration = int(input("Enter the duration: "))
        unit = input("Choose unit (h for hours, m for minutes, s for seconds): ").lower()

        if unit == 'h':
            duration *= 3600
            
        elif unit == 'm':
            duration *= 60
            
        elif unit != 's':
            print("Invalid unit. Please choose from h, m, or s.")
            continue

        while True:
            add_more = input("Do you want to add more time? (yes/no): ").lower()
            if add_more == 'yes':
                more_duration = int(input("Enter additional duration: "))
                more_unit = input("Choose unit (h for hours, m for minutes, s for seconds): ").lower()

                if more_unit == 'h':
                    more_duration *= 3600
                    
                elif more_unit == 'm':
                    more_duration *= 60
                    
                elif more_unit != 's':
                    print("Invalid unit. Please choose from h, m, or s.")
                    continue

                duration += more_duration
            elif add_more == 'no':
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

        print("Countdown started.")

        while duration > 0:
            mins, secs = divmod(duration, 60)
            hours, mins = divmod(mins, 60)
            timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            duration -= 1

        print("Time's up!")

        choice = input("Do you want to start a new countdown? (yes/no): ").lower()
        if choice != 'yes':
            break

    except ValueError:
        print("Please enter a valid number.")
