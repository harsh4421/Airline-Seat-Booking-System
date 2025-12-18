import matplotlib.pyplot as plt

def create_simple_chart():
    """Create a simple booking chart"""
    
    # Sample data
    fare_classes = ['Economy', 'Business', 'First']
    bookings = [5, 3, 2]  # Replace with your actual numbers
    
    # Create bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(fare_classes, bookings, color=['green', 'blue', 'gold'])
    plt.xlabel('Fare Class')
    plt.ylabel('Number of Bookings')
    plt.title('Bookings by Fare Class')
    
    # Save chart
    plt.savefig('outputs/bookings_chart.png')
    print("✓ Chart saved to outputs/bookings_chart.png")
    plt.show()

# Run this to create chart
create_simple_chart()

