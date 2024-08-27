from datetime import datetime

def display_current_datetime():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    num_days = int(input("Enter the number of days to add to the current date: "))
    future_date = (datetime.datetime.now() + datetime.timedelta(days=num_days))
    print(f"Future date: {future_date.strftime("%Y-%m-%d %H:%M:%S")}")


display_current_datetime()
calculate_future_date()