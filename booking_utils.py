import csv
from datetime import datetime

SEAT_PRICING = {
    "Aisle": 5000,
    "Window": 4500,
    "Middle": 4000
}

FARE_MULTIPLIERS = {
    "Economy": 1.0,
    "Business": 2.5,
    "First": 4.0
}

def calculate_price(base_price, multiplier):
    """Calculate final price"""
    return base_price * multiplier

def format_currency(amount):
    """Format amount as currency"""
    return f"₹{amount:,.2f}"

def display_banner():
    """Show welcome banner"""
    print("\n" + "="*50)
    print("   AIRLINE SEAT BOOKING SYSTEM  ")
    print("="*50)

def display_menu():
    """Show main menu"""
    print("\n" + "-"*50)
    print("MAIN MENU:")
    print("-"*50)
    print("1. Book a Seat")
    print("2. View Available Seats")
    print("3. View All Bookings")
    print("4. Exit")
    print("-"*50)

def save_bookings_to_csv(bookings, filename="data/bookings.csv"):
    """Save all bookings to CSV file"""
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Booking ID", "Passenger", "Seat", "Type", "Class", "Price"])
            
            for booking in bookings:
                writer.writerow([
                    f"BK{booking.booking_id:03d}",
                    booking.passenger_name,
                    booking.seat.seat_no,
                    booking.seat.seat_type,
                    booking.fare_class,
                    booking.price
                ])
        print(f"\n✓ Data saved to {filename}")
        return True
    except Exception as e:
        print(f"\n✗ Error saving: {e}")
        return False

def pause():
    """Wait for user to press Enter"""
    input("\nPress Enter to continue...")