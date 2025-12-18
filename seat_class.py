from datetime import datetime
import booking_utils as utils

class Seat:
    """Represents one seat"""
    
    def __init__(self, seat_no, seat_type):
        self.seat_no = seat_no          # Like "1A", "2B"
        self.seat_type = seat_type      # Aisle, Window, Middle
        self.booked = False             # Is seat booked?
        self.passenger = None           # Who booked it?
    
    def book_seat(self, passenger_name):
        """Book this seat"""
        if not self.booked:
            self.booked = True
            self.passenger = passenger_name
            return True
        return False
    
    def is_available(self):
        """Check if seat is free"""
        return not self.booked


class Booking:
    """Represents one booking"""
    
    booking_counter = 0  # Counts total bookings
    
    def __init__(self, passenger_name, seat, fare_class, price):
        Booking.booking_counter += 1
        self.booking_id = Booking.booking_counter
        self.passenger_name = passenger_name
        self.seat = seat
        self.fare_class = fare_class
        self.price = price
        self.booking_time = datetime.now()


class BookingSystem:
    """Main system that manages everything"""
    
    def __init__(self):
        self.seats = []
        self.bookings = []
        self.total_revenue = 0
        self.create_seats()
    
    def create_seats(self):
        """Create all seats (30 seats = 5 rows × 6 seats)"""
        seat_types = ["Window", "Middle", "Aisle", "Aisle", "Middle", "Window"]
        
        for row in range(1, 6):  # 5 rows
            for col in range(6):  # 6 seats per row
                seat_no = f"{row}{chr(65 + col)}"  # 1A, 1B, 1C, etc.
                seat_type = seat_types[col]
                seat = Seat(seat_no, seat_type)
                self.seats.append(seat)
        
        print(f"✓ Created {len(self.seats)} seats")
    
    def book_seat(self, passenger_name, seat_preference, fare_class):
        """Book a seat for passenger"""
        
        # Find available seat of requested type
        for seat in self.seats:
            if not seat.booked and seat.seat_type == seat_preference:
                # Calculate price
                base_price = utils.SEAT_PRICING[seat_preference]
                multiplier = utils.FARE_MULTIPLIERS[fare_class]
                price = utils.calculate_price(base_price, multiplier)
                
                # Book the seat
                seat.book_seat(passenger_name)
                
                # Create booking record
                booking = Booking(passenger_name, seat, fare_class, price)
                self.bookings.append(booking)
                self.total_revenue += price
                
                # Show confirmation
                self.show_booking_confirmation(booking)
                return True
        
        print(f"\n✗ Sorry, no {seat_preference} seats available!")
        return False
    
    def show_booking_confirmation(self, booking):
        """Display booking details"""
        print("\n" + "="*50)
        print("🎉 BOOKING CONFIRMED!")
        print("="*50)
        print(f"Booking ID    : BK{booking.booking_id:03d}")
        print(f"Passenger     : {booking.passenger_name}")
        print(f"Seat Number   : {booking.seat.seat_no}")
        print(f"Seat Type     : {booking.seat.seat_type}")
        print(f"Fare Class    : {booking.fare_class}")
        print(f"Price         : {utils.format_currency(booking.price)}")
        print("="*50)
    
    def show_available_seats(self):
        """Display all available seats"""
        print("\n" + "="*50)
        print("AVAILABLE SEATS")
        print("="*50)
        
        # Group by type
        aisle_seats = []
        window_seats = []
        middle_seats = []
        
        for seat in self.seats:
            if not seat.booked:
                if seat.seat_type == "Aisle":
                    aisle_seats.append(seat.seat_no)
                elif seat.seat_type == "Window":
                    window_seats.append(seat.seat_no)
                else:
                    middle_seats.append(seat.seat_no)
        
        # Display
        if window_seats:
            print(f"\nWindow Seats (₹4,500): {', '.join(window_seats)}")
        if aisle_seats:
            print(f"Aisle Seats (₹5,000): {', '.join(aisle_seats)}")
        if middle_seats:
            print(f"Middle Seats (₹4,000): {', '.join(middle_seats)}")
        
        total_available = len(window_seats) + len(aisle_seats) + len(middle_seats)
        print(f"\nTotal Available: {total_available}/{len(self.seats)}")
    
    def show_all_bookings(self):
        """Display all bookings"""
        print("\n" + "="*50)
        print("ALL BOOKINGS")
        print("="*50)
        
        if not self.bookings:
            print("\nNo bookings yet!")
            return
        
        print(f"\n{'ID':<8} {'Passenger':<20} {'Seat':<6} {'Class':<10} {'Price':<12}")
        print("-"*50)
        
        for booking in self.bookings:
            print(f"BK{booking.booking_id:03d}   "
                  f"{booking.passenger_name:<20} "
                  f"{booking.seat.seat_no:<6} "
                  f"{booking.fare_class:<10} "
                  f"₹{booking.price:>9,.2f}")
        
        print("-"*50)
        print(f"\nTotal Bookings: {len(self.bookings)}")
        print(f"Total Revenue: {utils.format_currency(self.total_revenue)}")
        print(f"Occupancy: {len(self.bookings)}/{len(self.seats)} seats "
              f"({len(self.bookings)*100//len(self.seats)}%)")
        