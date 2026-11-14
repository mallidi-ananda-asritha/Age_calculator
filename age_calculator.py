
import calendar
from datetime import datetime, date, timedelta


def calculate_age(dob, today):
    """Calculate exact age in years, months and days."""

    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    # Borrow days from the previous month
    if days < 0:
        previous_month = today.replace(day=1) - timedelta(days=1)
        days += previous_month.day
        months -= 1

    # Borrow months from the previous year
    if months < 0:
        months += 12
        years -= 1

    return years, months, days


def main():
    print("=" * 45)
    print("          SMART AGE CALCULATOR")
    print("=" * 45)

    while True:
        dob_input = input(
            "\nEnter your Date of Birth (DD-MM-YYYY): "
        )

        try:
            dob = datetime.strptime(
                dob_input, "%d-%m-%Y"
            ).date()

            # Ensure the input follows the required format
            if dob.strftime("%d-%m-%Y") != dob_input:
                print("Invalid date format. Please try again.")
                continue

            today = date.today()

            # Check for future dates
            if dob > today:
                print("Error: Date of birth cannot be in the future.")
                continue

            # Calculate exact age
            years, months, days = calculate_age(dob, today)

            print("\n" + "=" * 45)
            print("             YOUR AGE")
            print("=" * 45)

            print(f"Years  : {years}")
            print(f"Months : {months}")
            print(f"Days   : {days}")

            print("\nYour exact age is:")
            print(f"{years} Years, {months} Months, {days} Days")

            print("=" * 45)

            break

        except ValueError:
            print("Invalid date! Please enter a valid date.")


if __name__ == "__main__":
    main()
