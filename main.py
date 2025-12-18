import os
from seat_class import BookingSystem
import booking_utils as utils

def book_new_seat(system):
    """Handle booking process"""
    print("\n" + "="*50)
    print("BOOK A NEW SEAT")
    print("="*50)
    
    # Get passenger name
    passenger = input("\nEnter passenger name: ").strip()
    if not passenger:
        print(" Name cannot be empty!")
        return
    
    # Show seat types
    print("\nAvailable Seat Types:")
    print("1. Window (₹4,500)")
    print("2. Aisle (₹5,000)")
    print("3. Middle (₹4,000)")
    
    # Get seat type choice
    choice = input("\nChoose seat type (1-3): ").strip()
    
    if choice == "1":
        seat_type = "Window"
    elif choice == "2":
        seat_type = "Aisle"
    elif choice == "3":
        seat_type = "Middle"
    else:
        print(" Invalid choice!")
        return
    
    # Show fare classes
    print("\nFare Classes:")
    print("1. Economy (Base Price)")
    print("2. Business (2.5x Price)")
    print("3. First Class (4x Price)")
    
    # Get fare class choice
    choice = input("\nChoose fare class (1-3): ").strip()
    
    if choice == "1":
        fare_class = "Economy"
    elif choice == "2":
        fare_class = "Business"
    elif choice == "3":
        fare_class = "First"
    else:
        print(" Invalid choice!")
        return
    
    # Book the seat
    system.book_seat(passenger, seat_type, fare_class)


def main():
    """Main function - program starts here"""
    
    # Create data folder if it doesn't exist
    os.makedirs('data', exist_ok=True)
    os.makedirs('outputs', exist_ok=True)
    
    # Show welcome banner
    utils.display_banner()
    
    # Create booking system
    print("\n Initializing system...")
    system = BookingSystem()
    
    # Main menu loop
    while True:
        utils.display_menu()
        
        choice = input("\n Enter your choice (1-4): ").strip()
        
        if choice == "1":
            # Book a seat
            book_new_seat(system)
            utils.pause()
        
        elif choice == "2":
            # View available seats
            system.show_available_seats()
            utils.pause()
        
        elif choice == "3":
            # View all bookings
            system.show_all_bookings()
            
            # Ask if user wants to save
            if system.bookings:
                save = input("\n Save bookings to CSV? (yes/no): ").strip().lower()
                if save in ['yes', 'y']:
                    utils.save_bookings_to_csv(system.bookings)
            
            utils.pause()
        
        elif choice == "4":
            # Exit
            print("\n" + "="*50)
            print("Thank you for using our system!")
            print(" Safe travels! Goodbye!")
            print("="*50 + "\n")
            
            # Save data before exit
            if system.bookings:
                utils.save_bookings_to_csv(system.bookings)
            
            break
        
        else:
            print("\n Invalid choice! Please enter 1-4")
            utils.pause()


# Run the program
if __name__ == "__main__":
    main()