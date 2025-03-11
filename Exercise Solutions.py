"""
Hritvik JV
Winter 2025
"""
import math

##############################
# Solution 1: Book Collection
##############################

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []
    
    def __str__(self):
        return f'"{self.title}" by {self.author}'
    
    def __repr__(self):
        return f'Book("{self.title}", "{self.author}")'
    
    def add_review(self, rating):
        if 1 <= rating <= 5:
            self.reviews.append(rating)
        else:
            raise ValueError("Rating must be between 1 and 5")
    
    def get_average_rating(self):
        if not self.reviews:
            return 0
        return sum(self.reviews) / len(self.reviews)
    
    def is_recommended(self):
        return self.get_average_rating() >= 4.0


def test_book_collection():
    # Create books
    book1 = Book("The Hobbit", "J.R.R. Tolkien")
    book2 = Book("Harry Potter", "J.K. Rowling")
    
    # Test string representations
    print(str(book1))
    print(book1)
    
    # Add reviews
    book1.add_review(5)
    book1.add_review(4)
    book1.add_review(5)
    
    book2.add_review(3)
    book2.add_review(3)
    book2.add_review(4)
    
    # Test average rating
    print(f"{book1.title} average rating: {book1.get_average_rating()}")
    print(f"{book2.title} average rating: {book2.get_average_rating()}")
    
    # Test recommendation
    print(f"{book1.title} is recommended: {book1.is_recommended()}")
    print(f"{book2.title} is recommended: {book2.is_recommended()}")


##############################
# Solution 2: Shape Hierarchy
##############################

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area method")
    
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter method")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"Circle(radius={self.radius})"


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
        # Verify that the sides can form a triangle
        if not (self.side1 + self.side2 > self.side3 and
                self.side1 + self.side3 > self.side2 and
                self.side2 + self.side3 > self.side1):
            raise ValueError("The given sides cannot form a triangle")
    
    def area(self):
        # Using Heron's formula
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def __str__(self):
        return f"Triangle(sides={self.side1}, {self.side2}, {self.side3})"


def test_shape_hierarchy():
    # Create shapes
    rect = Rectangle(5, 3)
    circle = Circle(4)
    triangle = Triangle(3, 4, 5)
    
    # Test area and perimeter
    print(f"{rect} - Area: {rect.area()}, Perimeter: {rect.perimeter()}")
    print(f"{circle} - Area: {circle.area():.2f}, Perimeter: {circle.perimeter():.2f}")
    print(f"{triangle} - Area: {triangle.area()}, Perimeter: {triangle.perimeter()}")


##############################
# Solution 3: Playlist Manager
##############################

import random

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration  # in seconds
    
    def __str__(self):
        minutes, seconds = divmod(self.duration, 60)
        return f'"{self.title}" by {self.artist} ({minutes}:{seconds:02d})'
    
    def __repr__(self):
        return f'Song("{self.title}", "{self.artist}", {self.duration})'


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
    
    def remove_song(self, title):
        for i, song in enumerate(self.songs):
            if song.title == title:
                return self.songs.pop(i)
        return None
    
    def total_duration(self):
        return sum(song.duration for song in self.songs)
    
    def shuffle(self):
        shuffled_playlist = Playlist(f"{self.name} (Shuffled)")
        shuffled_songs = random.sample(self.songs, len(self.songs))
        for song in shuffled_songs:
            shuffled_playlist.add_song(song)
        return shuffled_playlist
    
    def filter_by_artist(self, artist):
        filtered_playlist = Playlist(f"{artist} songs from {self.name}")
        for song in self.songs:
            if song.artist == artist:
                filtered_playlist.add_song(song)
        return filtered_playlist
    
    def __str__(self):
        minutes, seconds = divmod(self.total_duration(), 60)
        result = f"Playlist: {self.name} ({len(self.songs)} songs, {minutes}:{seconds:02d})\n"
        for i, song in enumerate(self.songs, 1):
            result += f"{i}. {song}\n"
        return result.strip()


def test_playlist_manager():
    # Create songs
    song1 = Song("Bohemian Rhapsody", "Queen", 354)
    song2 = Song("Hotel California", "Eagles", 390)
    song3 = Song("We Will Rock You", "Queen", 122)
    song4 = Song("Imagine", "John Lennon", 183)
    
    # Create playlist
    playlist = Playlist("Classic Rock")
    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.add_song(song3)
    playlist.add_song(song4)
    
    # Print playlist
    print(playlist)
    
    # Filter by artist
    queen_songs = playlist.filter_by_artist("Queen")
    print("\n" + str(queen_songs))
    
    # Test total duration
    minutes, seconds = divmod(playlist.total_duration(), 60)
    print(f"\nTotal duration: {minutes}:{seconds:02d}")
    
    # Remove a song
    removed = playlist.remove_song("Imagine")
    print(f"\nRemoved: {removed}")
    print(playlist)


##############################
# Solution 4: Weather Station
##############################

class WeatherData:
    def __init__(self, temperature, humidity, pressure, timestamp):
        self.temperature = temperature  # in Celsius
        self.humidity = humidity  # percentage
        self.pressure = pressure  # hPa
        self.timestamp = timestamp  # "YYYY-MM-DD HH:MM"
    
    def __str__(self):
        return f"[{self.timestamp}] Temp: {self.temperature}°C, Humidity: {self.humidity}%, Pressure: {self.pressure} hPa"


class WeatherStation:
    def __init__(self, location):
        self.location = location
        self.readings = []
    
    def add_reading(self, reading):
        self.readings.append(reading)
    
    def avg_temperature(self):
        if not self.readings:
            return None
        return sum(r.temperature for r in self.readings) / len(self.readings)
    
    def min_temperature(self):
        if not self.readings:
            return None
        return min(r.temperature for r in self.readings)
    
    def max_temperature(self):
        if not self.readings:
            return None
        return max(r.temperature for r in self.readings)
    
    def get_readings_by_date(self, date):
        # Filter readings where timestamp starts with the given date
        return [r for r in self.readings if r.timestamp.startswith(date)]
    
    def __str__(self):
        result = f"Weather Station at {self.location} ({len(self.readings)} readings)\n"
        result += f"Temperature range: {self.min_temperature():.1f}°C to {self.max_temperature():.1f}°C\n"
        result += f"Average temperature: {self.avg_temperature():.1f}°C"
        return result


def test_weather_station():
    # Create weather station
    station = WeatherStation("Portland")
    
    # Add readings
    station.add_reading(WeatherData(23.5, 65.0, 1013.2, "2023-06-10 08:00"))
    station.add_reading(WeatherData(26.8, 60.2, 1012.1, "2023-06-10 12:00"))
    station.add_reading(WeatherData(25.1, 62.5, 1011.8, "2023-06-10 16:00"))
    station.add_reading(WeatherData(18.7, 75.0, 1014.5, "2023-06-11 08:00"))
    station.add_reading(WeatherData(22.3, 70.1, 1013.9, "2023-06-11 12:00"))
    
    # Print station information
    print(station)
    
    # Get readings for a specific date
    june_10_readings = station.get_readings_by_date("2023-06-10")
    print(f"\nReadings for 2023-06-10:")
    for reading in june_10_readings:
        print(reading)


##############################
# Solution 5: BankAccount Hierarchy
##############################

class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance
    
    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"{self.__class__.__name__} ({self.account_number}): {self.holder_name}, Balance: ${self.balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, initial_balance=0.0, interest_rate=0.01):
        super().__init__(account_number, holder_name, initial_balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest


class CheckingAccount(BankAccount):
    def __init__(self, account_number, holder_name, initial_balance=0.0, transaction_fee=1.0):
        super().__init__(account_number, holder_name, initial_balance)
        self.transaction_fee = transaction_fee
    
    def withdraw(self, amount):
        total_amount = amount + self.transaction_fee
        if total_amount > self.balance:
            raise ValueError("Insufficient funds (including transaction fee)")
        self.balance -= total_amount
        return self.balance


class CreditAccount(BankAccount):
    def __init__(self, account_number, holder_name, initial_balance=0.0, credit_limit=1000.0, interest_rate=0.18):
        super().__init__(account_number, holder_name, initial_balance)
        self.credit_limit = credit_limit
        self.interest_rate = interest_rate
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self.balance - amount < -self.credit_limit:
            raise ValueError("Exceeds credit limit")
        self.balance -= amount
        return self.balance
    
    def apply_interest(self):
        # Apply interest only on negative balance
        if self.balance < 0:
            interest = abs(self.balance) * self.interest_rate
            self.balance -= interest
            return interest
        return 0


def test_bank_account_hierarchy():
    # Create accounts
    savings = SavingsAccount("S123", "Alice Smith", 1000.0, 0.05)
    checking = CheckingAccount("C456", "Bob Johnson", 500.0, 1.50)
    credit = CreditAccount("R789", "Charlie Brown", 0.0, 2000.0, 0.20)
    
    # Test transactions
    print("Initial state:")
    print(savings)
    print(checking)
    print(credit)
    
    print("\nAfter transactions:")
    savings.deposit(500)
    interest_earned = savings.apply_interest()
    print(f"{savings} (Interest earned: ${interest_earned:.2f})")
    
    try:
        checking.withdraw(400)
        print(checking)
    except ValueError as e:
        print(f"Error: {e}")
    
    credit.withdraw(1500)
    interest_charged = credit.apply_interest()
    print(f"{credit} (Interest charged: ${interest_charged:.2f})")


##############################
# Solution 6: Event Registration System
##############################

class Participant:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    
    def __str__(self):
        return f"{self.name} ({self.email})"
    
    def __repr__(self):
        return f'Participant("{self.name}", "{self.email}", "{self.phone}")'


class Event:
    def __init__(self, name, date, venue, max_participants):
        self.name = name
        self.date = date
        self.venue = venue
        self.max_participants = max_participants
        self.registered = []
    
    def register(self, participant):
        if self.is_full():
            return False
        
        # Check if participant is already registered (by email)
        for p in self.registered:
            if p.email == participant.email:
                return False
        
        self.registered.append(participant)
        return True
    
    def unregister(self, email):
        for i, participant in enumerate(self.registered):
            if participant.email == email:
                return self.registered.pop(i)
        return None
    
    def is_full(self):
        return len(self.registered) >= self.max_participants
    
    def get_available_spots(self):
        return self.max_participants - len(self.registered)
    
    def get_participant_list(self):
        return '\n'.join([f"{i+1}. {p}" for i, p in enumerate(self.registered)])
    
    def __str__(self):
        return f"{self.name} on {self.date} at {self.venue} ({len(self.registered)}/{self.max_participants} participants)"


class EventManager:
    def __init__(self):
        self.events = []
    
    def add_event(self, event):
        self.events.append(event)
    
    def remove_event(self, name):
        for i, event in enumerate(self.events):
            if event.name == name:
                return self.events.pop(i)
        return None
    
    def get_events_by_date(self, date):
        return [event for event in self.events if event.date == date]
    
    def register_participant(self, event_name, participant):
        for event in self.events:
            if event.name == event_name:
                return event.register(participant)
        return False
    
    def __str__(self):
        return f"Event Manager ({len(self.events)} events)"


def test_event_registration_system():
    # Create event manager
    manager = EventManager()
    
    # Create events
    conference = Event("Tech Conference", "2023-09-15", "Convention Center", 200)
    workshop = Event("Python Workshop", "2023-09-15", "University Lab", 30)
    meetup = Event("Developer Meetup", "2023-09-20", "Startup Hub", 50)
    
    # Add events to manager
    manager.add_event(conference)
    manager.add_event(workshop)
    manager.add_event(meetup)
    
    # Create participants
    p1 = Participant("John Doe", "john@example.com", "555-123-4567")
    p2 = Participant("Jane Smith", "jane@example.com", "555-765-4321")
    p3 = Participant("Bob Brown", "bob@example.com", "555-555-5555")
    
    # Register participants
    manager.register_participant("Python Workshop", p1)
    manager.register_participant("Python Workshop", p2)
    manager.register_participant("Developer Meetup", p1)
    manager.register_participant("Developer Meetup", p3)
    
    # Print events
    print(manager)
    print("\nAll events:")
    for event in manager.events:
        print(event)
    
    # Print events by date
    print("\nEvents on 2023-09-15:")
    for event in manager.get_events_by_date("2023-09-15"):
        print(event)
    
    # Print workshop participants
    print("\nPython Workshop participants:")
    print(workshop.get_participant_list())
    
    # Unregister a participant
    removed = workshop.unregister("jane@example.com")
    print(f"\nRemoved: {removed}")
    print(f"Available spots in workshop: {workshop.get_available_spots()}")


##############################
# Solution 7: Library System
##############################

class LibraryBook:
    def __init__(self, title, author, isbn, published_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.published_year = published_year
        self.available = True
    
    def __str__(self):
        status = "Available" if self.available else "Checked Out"
        return f'"{self.title}" by {self.author} ({self.published_year}) [ISBN: {self.isbn}] - {status}'


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.books_checked_out = []
    
    def __str__(self):
        return f"{self.name} (ID: {self.member_id}) - {len(self.books_checked_out)} books checked out"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def add_member(self, member):
        self.members.append(member)
    
    def check_out_book(self, isbn, member_id):
        # Find the book
        book = None
        for b in self.books:
            if b.isbn == isbn and b.available:
                book = b
                break
        
        if not book:
            return False
        
        # Find the member
        member = None
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break
        
        if not member:
            return False
        
        # Check out the book
        book.available = False
        member.books_checked_out.append(book)
        return True
    
    def return_book(self, isbn):
        # Find the book in library
        book = None
        for b in self.books:
            if b.isbn == isbn and not b.available:
                book = b
                break
        
        if not book:
            return False
        
        # Find which member has the book
        for member in self.members:
            for i, b in enumerate(member.books_checked_out):
                if b.isbn == isbn:
                    # Remove from member's checked out books
                    member.books_checked_out.pop(i)
                    # Mark as available
                    book.available = True
                    return True
        
        return False
    
    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]
    
    def search_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]
    
    def get_available_books(self):
        return [book for book in self.books if book.available]
    
    def get_checked_out_books(self):
        return [book for book in self.books if not book.available]
    
    def __str__(self):
        return f"{self.name} Library ({len(self.books)} books, {len(self.members)} members)"


def test_library_system():
    # Create library
    library = Library("Community Library")
    
    # Create books
    book1 = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1925)
    book2 = LibraryBook("To Kill a Mockingbird", "Harper Lee", "9780061120084", 1960)
    book3 = LibraryBook("1984", "George Orwell", "9780451524935", 1949)
    book4 = LibraryBook("Pride and Prejudice", "Jane Austen", "9780141439518", 1813)
    book5 = LibraryBook("The Catcher in the Rye", "J.D. Salinger", "9780316769488", 1951)
    
    # Add books to library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
    
    # Create members
    member1 = Member("Alice Johnson", "M001")
    member2 = Member("Bob Smith", "M002")
    
    # Add members to library
    library.add_member(member1)
    library.add_member(member2)
    
    # Check out books
    library.check_out_book("9780743273565", "M001")  # Great Gatsby to Alice
    library.check_out_book("9780061120084", "M001")  # Mockingbird to Alice
    library.check_out_book("9780451524935", "M002")  # 1984 to Bob
    
    # Print library status
    print(f"Library: {library.name}")
    print("\nAvailable books:")
    for book in library.get_available_books():
        print(book)
    
    print("\nChecked out books:")
    for book in library.get_checked_out_books():
        print(book)
    
    # Search by author
    print("\nBooks by Jane Austen:")
    for book in library.search_by_author("Jane Austen"):
        print(book)
    
    # Return a book
    library.return_book("9780743273565")
    print("\nAfter returning The Great Gatsby:")
    print(f"Books checked out by Alice: {len(member1.books_checked_out)}")
    print(f"Available books: {len(library.get_available_books())}")


##############################
# Solution 8: Store Inventory System
##############################

from datetime import datetime

class Product:
    def __init__(self, name, price, product_id, quantity):
        self.name = name
        self.price = price
        self.product_id = product_id
        self.quantity = quantity
    
    def calculate_value(self):
        return self.price * self.quantity
    
    def update_quantity(self, amount):
        new_quantity = self.quantity + amount
        if new_quantity < 0:
            raise ValueError("Cannot have negative quantity")
        self.quantity = new_quantity
    
    def is_in_stock(self):
        return self.quantity > 0
    
    def __str__(self):
        return f"{self.name} (ID: {self.product_id}) - ${self.price:.2f} x {self.quantity} = ${self.calculate_value():.2f}"


class Perishable(Product):
    def __init__(self, name, price, product_id, quantity, expiry_date):
        super().__init__(name, price, product_id, quantity)
        self.expiry_date = expiry_date
    
    def is_expired(self, current_date):
        # Compare dates as strings (format: "YYYY-MM-DD")
        return self.expiry_date < current_date
    
    def calculate_value(self):
        current_date = datetime.now().strftime("%Y-%m-%d")
        if self.is_expired(current_date):
            return 0
        return super().calculate_value()
    
    def __str__(self):
        return f"{super().__str__()} - Expires: {self.expiry_date}"


class Electronics(Product):
    def __init__(self, name, price, product_id, quantity, warranty_months, brand):
        super().__init__(name, price, product_id, quantity)
        self.warranty_months = warranty_months
        self.brand = brand
    
    def calculate_value(self):
        # 10% markup for electronics
        return self.price * self.quantity * 1.1
    
    def __str__(self):
        return f"{super().__str__()} - Brand: {self.brand}, Warranty: {self.warranty_months} months"


class Clothing(Product):
    def __init__(self, name, price, product_id, quantity, size, color):
        super().__init__(name, price, product_id, quantity)
        self.size = size
        self.color = color
    
    def calculate_value(self):
        # Sample seasonal discount logic (can be expanded)
        current_month = datetime.now().month
        # Summer discount (June-August)
        if 6 <= current_month <= 8:
            return self.price * self.quantity * 0.9
        # Winter discount (December-February)
        elif current_month == 12 or 1 <= current_month <= 2:
            return self.price * self.quantity * 0.85
        return super().calculate_value()
    
    def __str__(self):
        return f"{super().__str__()} - Size: {self.size}, Color: {self.color}"


class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def remove_product(self, product_id):
        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                return self.products.pop(i)
        return None
    
    def get_total_value(self):
        return sum(product.calculate_value() for product in self.products)
    
    def find_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
    
    def get_products_by_type(self, product_type):
        return [p for p in self.products if isinstance(p, product_type)]
    
    def get_low_stock_products(self, threshold):
        return [p for p in self.products if p.quantity <= threshold]
    
    def __str__(self):
        return f"Inventory with {len(self.products)} products, total value: ${self.get_total_value():.2f}"


def test_inventory_system():
    # Create products
    apple = Perishable("Apple", 0.50, "P001", 100, "2023-06-15")
    tv = Electronics("Smart TV", 499.99, "E001", 5, 24, "Samsung")
    shirt = Clothing("T-Shirt", 19.99, "C001", 50, "M", "Blue")
    
    # Create inventory
    inventory = Inventory()
    inventory.add_product(apple)
    inventory.add_product(tv)
    inventory.add_product(shirt)
    
    # Print inventory information
    print("Inventory Summary:")
    print(f"Total products: {len(inventory.products)}")
    print(f"Total value: ${inventory.get_total_value():.2f}")
    
    # Check specific product types
    print("\nElectronics products:")
    for product in inventory.get_products_by_type(Electronics):
        print(product)
    
    # Check product stock
    print("\nLow stock products (threshold=10):")
    for product in inventory.get_low_stock_products(10):
        print(product)
    
    # Test expiry method
    current_date = "2023-06-10"
    print(f"\nIs apple expired on {current_date}? {apple.is_expired(current_date)}")
    future_date = "2023-06-20"
    print(f"Is apple expired on {future_date}? {apple.is_expired(future_date)}")
    
    # Update quantities
    apple.update_quantity(-20)
    tv.update_quantity(2)
    print("\nAfter quantity updates:")
    print(f"Apples in stock: {apple.quantity} (Value: ${apple.calculate_value():.2f})")
    print(f"TVs in stock: {tv.quantity} (Value: ${tv.calculate_value():.2f})")

##############################
# Solution 9: Binary Search Tree (Continued)
##############################

class Node:
    """
    A node in a binary search tree.
    
    Attributes:
        value: The value stored in the node
        left: Reference to the left child node
        right: Reference to the right child node
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.value)


class BinarySearchTree:
    """
    A binary search tree data structure.
    
    Attributes:
        root: Reference to the root node
    """
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insert a new value into the tree"""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Recursively insert a value at the correct position"""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        """Search for a value in the tree"""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """Recursively search for a value in the tree"""
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
    def in_order_traversal(self):
        """Perform in-order traversal of the tree"""
        result = []
        self._in_order_recursive(self.root, result)
        return result
    
    def _in_order_recursive(self, node, result):
        """Helper method for in-order traversal"""
        if node:
            self._in_order_recursive(node.left, result)
            result.append(node.value)
            self._in_order_recursive(node.right, result)
    
    def pre_order_traversal(self):
        """Perform pre-order traversal of the tree"""
        result = []
        self._pre_order_recursive(self.root, result)
        return result
    
    def _pre_order_recursive(self, node, result):
        """Helper method for pre-order traversal"""
        if node:
            result.append(node.value)
            self._pre_order_recursive(node.left, result)
            self._pre_order_recursive(node.right, result)
    
    def post_order_traversal(self):
        """Perform post-order traversal of the tree"""
        result = []
        self._post_order_recursive(self.root, result)
        return result
    
    def _post_order_recursive(self, node, result):
        """Helper method for post-order traversal"""
        if node:
            self._post_order_recursive(node.left, result)
            self._post_order_recursive(node.right, result)
            result.append(node.value)
    
    def find_min(self):
        """Find the minimum value in the tree"""
        if self.root is None:
            return None
        return self._find_min_recursive(self.root)
    
    def _find_min_recursive(self, node):
        """Helper method to find the minimum value"""
        if node.left is None:
            return node.value
        return self._find_min_recursive(node.left)
    
    def find_max(self):
        """Find the maximum value in the tree"""
        if self.root is None:
            return None
        return self._find_max_recursive(self.root)
    
    def _find_max_recursive(self, node):
        """Helper method to find the maximum value"""
        if node.right is None:
            return node.value
        return self._find_max_recursive(node.right)
    
    def get_height(self):
        """Get the height of the tree"""
        return self._get_height_recursive(self.root)
    
    def _get_height_recursive(self, node):
        """Helper method to calculate the height"""
        if node is None:
            return -1
        left_height = self._get_height_recursive(node.left)
        right_height = self._get_height_recursive(node.right)
        return max(left_height, right_height) + 1
    
    def delete(self, value):
        """Delete a value from the tree"""
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        """Helper method to recursively delete a value"""
        # Base case: If the tree is empty
        if node is None:
            return None
        
        # Find the node to be deleted
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Case 1: Node with no children (leaf node)
            if node.left is None and node.right is None:
                return None
            
            # Case 2: Node with only one child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Case 3: Node with two children
            # Find the inorder successor (smallest value in right subtree)
            node.value = self._find_min_recursive(node.right)
            
            # Delete the inorder successor
            node.right = self._delete_recursive(node.right, node.value)
        
        return node


def test_binary_search_tree():
    """Test the Binary Search Tree implementation"""
    # Create BST
    bst = BinarySearchTree()
    
    # Insert values
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        bst.insert(value)
    
    # Print tree traversals
    print("In-order traversal:", bst.in_order_traversal())
    print("Pre-order traversal:", bst.pre_order_traversal())
    print("Post-order traversal:", bst.post_order_traversal())
    
    # Test search
    print("\nSearch tests:")
    print(f"Search for 40: {bst.search(40)}")
    print(f"Search for 55: {bst.search(55)}")
    
    # Find min and max
    print(f"\nMinimum value: {bst.find_min()}")
    print(f"Maximum value: {bst.find_max()}")
    
    # Get height
    print(f"\nTree height: {bst.get_height()}")
    
    # Delete nodes
    print("\nAfter deleting 20:")
    bst.delete(20)
    print("In-order traversal:", bst.in_order_traversal())
    
    print("\nAfter deleting 30:")
    bst.delete(30)
    print("In-order traversal:", bst.in_order_traversal())
    
    print("\nAfter deleting 50 (root):")
    bst.delete(50)
    print("In-order traversal:", bst.in_order_traversal())


##############################
# Solution 10: Game Character System
##############################

class Character:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level
    
    def attack(self):
        return 5 * self.level  # Base attack power
    
    def take_damage(self, amount):
        if amount < 0:
            raise ValueError("Damage amount cannot be negative")
        self.health -= amount
        if self.health < 0:
            self.health = 0
    
    def heal(self, amount):
        if amount < 0:
            raise ValueError("Heal amount cannot be negative")
        self.health += amount
    
    def is_alive(self):
        return self.health > 0
    
    def level_up(self):
        self.level += 1
        self.health += 20  # Base health increase per level
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} (Level {self.level}) - Health: {self.health}"


class Warrior(Character):
    def __init__(self, name, health, level, strength, armor):
        super().__init__(name, health, level)
        self.strength = strength
        self.armor = armor
    
    def attack(self):
        return self.strength * self.level
    
    def take_damage(self, amount):
        # Armor reduces damage taken
        reduced_damage = max(0, amount - self.armor)
        super().take_damage(reduced_damage)
    
    def rage_attack(self):
        # Stronger attack that costs health
        damage = self.strength * 2
        self.take_damage(10)  # Costs 10 health
        return damage
    
    def level_up(self):
        super().level_up()
        self.strength += 3
        self.armor += 2
    
    def __str__(self):
        return f"{super().__str__()}, Strength: {self.strength}, Armor: {self.armor}"


class Mage(Character):
    def __init__(self, name, health, level, mana, intelligence):
        super().__init__(name, health, level)
        self.mana = mana
        self.intelligence = intelligence
    
    def attack(self):
        # Basic attack using intelligence
        return self.intelligence * self.level
    
    def cast_spell(self, spell_name):
        spells = {
            "fireball": {"damage": self.intelligence * 1.5, "mana_cost": 30},
            "ice_spike": {"damage": self.intelligence * 1.2, "mana_cost": 20},
            "thunder": {"damage": self.intelligence * 2, "mana_cost": 50}
        }
        
        if spell_name not in spells:
            return 0
        
        spell = spells[spell_name]
        if self.mana < spell["mana_cost"]:
            return 0
        
        self.mana -= spell["mana_cost"]
        return spell["damage"]
    
    def restore_mana(self, amount):
        if amount < 0:
            raise ValueError("Restore amount cannot be negative")
        self.mana += amount
    
    def level_up(self):
        super().level_up()
        self.intelligence += 4
        self.mana += 20
    
    def __str__(self):
        return f"{super().__str__()}, Mana: {self.mana}, Intelligence: {self.intelligence}"


class Archer(Character):
    def __init__(self, name, health, level, dexterity, arrows):
        super().__init__(name, health, level)
        self.dexterity = dexterity
        self.arrows = arrows
    
    def attack(self):
        # Basic attack using dexterity
        if self.arrows <= 0:
            return self.level * 2  # Weak attack if out of arrows
        self.arrows -= 1
        return self.dexterity * self.level
    
    def aimed_shot(self):
        # Stronger attack that uses more arrows
        if self.arrows < 3:
            return 0
        self.arrows -= 3
        return self.dexterity * 2
    
    def craft_arrows(self, amount):
        if amount < 0:
            raise ValueError("Craft amount cannot be negative")
        self.arrows += amount
    
    def level_up(self):
        super().level_up()
        self.dexterity += 4
        self.arrows += 10
    
    def __str__(self):
        return f"{super().__str__()}, Dexterity: {self.dexterity}, Arrows: {self.arrows}"


def test_game_character_system():
    # Create characters
    warrior = Warrior("Aragorn", 100, 1, 15, 10)
    mage = Mage("Gandalf", 80, 1, 100, 20)
    archer = Archer("Legolas", 90, 1, 18, 30)
    
    # Print initial stats
    print("Initial character stats:")
    print(warrior)
    print(mage)
    print(archer)
    
    # Test basic attacks
    print("\nBasic attacks:")
    print(f"{warrior.name} attacks for {warrior.attack()} damage")
    print(f"{mage.name} attacks for {mage.attack()} damage")
    print(f"{archer.name} attacks for {archer.attack()} damage")
    
    # Test special abilities
    print("\nSpecial abilities:")
    print(f"{warrior.name} rage attacks for {warrior.rage_attack()} damage (Health: {warrior.health})")
    print(f"{mage.name} casts fireball for {mage.cast_spell('fireball')} damage (Mana: {mage.mana})")
    print(f"{archer.name} uses aimed shot for {archer.aimed_shot()} damage (Arrows: {archer.arrows})")
    
    # Test damage taking
    print("\nTaking damage:")
    warrior.take_damage(20)
    mage.take_damage(30)
    archer.take_damage(25)
    print(f"{warrior.name} health after damage: {warrior.health}")
    print(f"{mage.name} health after damage: {mage.health}")
    print(f"{archer.name} health after damage: {archer.health}")
    
    # Test leveling up
    print("\nAfter leveling up:")
    warrior.level_up()
    mage.level_up()
    archer.level_up()
    print(warrior)
    print(mage)
    print(archer)

"""
Solutions for Additional Python Exercises:
- Lambda Functions and Functional Programming
- Bit Operations
- Linked Lists
- Loop Logic and Recursive Algorithms
"""

##############################
# Solution 11: Lambda Functions and Functional Programming
##############################

def map_values(func, values):
    """
    Apply a function to all items in an input list and return a new list
    without using Python's built-in map().
    
    Args:
        func: A function that takes a single argument
        values: A list of values to apply the function to
    
    Returns:
        A new list with the function applied to each value
    """
    return [func(value) for value in values]


def filter_values(predicate, values):
    """
    Filter a list to include only values that satisfy a predicate
    without using Python's built-in filter().
    
    Args:
        predicate: A function that returns True/False for a given value
        values: A list of values to filter
    
    Returns:
        A new filtered list
    """
    return [value for value in values if predicate(value)]


def string_processor():
    """
    Returns a dictionary of lambda functions for string processing.
    
    Returns:
        Dictionary mapping operation names to lambda functions
    """
    return {
        "uppercase": lambda s: s.upper(),
        "lowercase": lambda s: s.lower(),
        "capitalize": lambda s: ' '.join(word.capitalize() for word in s.split()),
        "reverse": lambda s: s[::-1],
        "word_count": lambda s: len(s.split()),
        "remove_spaces": lambda s: s.replace(" ", "")
    }


def compose(f, g):
    """
    Creates a function composition f(g(x)).
    
    Args:
        f: Outer function
        g: Inner function
    
    Returns:
        A new function that applies g and then f
    """
    return lambda x: f(g(x))


def process_pipeline(functions):
    """
    Creates a pipeline from a list of functions, applying them in sequence.
    
    Args:
        functions: A list of functions
    
    Returns:
        A function that applies all the functions in sequence
    """
    def pipeline(x):
        result = x
        for func in functions:
            result = func(result)
        return result
    
    return pipeline


def test_lambda_functions():
    """Test the lambda functions and functional programming utilities"""
    # Test map_values
    numbers = [1, 2, 3, 4, 5]
    squared = map_values(lambda x: x**2, numbers)
    print("Squared numbers:", squared)
    
    # Test filter_values
    even_numbers = filter_values(lambda x: x % 2 == 0, numbers)
    print("Even numbers:", even_numbers)
    
    # Test string_processor
    processors = string_processor()
    text = "hello world"
    for name, processor in processors.items():
        print(f"{name}: {processor(text)}")
    
    # Test compose
    double = lambda x: x * 2
    add_one = lambda x: x + 1
    double_then_add_one = compose(add_one, double)
    print("double_then_add_one(5):", double_then_add_one(5))
    
    # Test process_pipeline
    pipeline = process_pipeline([
        lambda x: x + 10,
        lambda x: x * 2,
        lambda x: x - 5
    ])
    print("pipeline(5):", pipeline(5))


##############################
# Solution 12: Bit Operations
##############################

def count_set_bits(n):
    """
    Count the number of '1' bits in the binary representation of n.
    
    Args:
        n: A non-negative integer
    
    Returns:
        Number of set bits
    """
    count = 0
    while n:
        count += n & 1  # Check if least significant bit is 1
        n >>= 1         # Shift right by 1
    return count


def is_power_of_two(n):
    """
    Check if n is a power of 2.
    
    Args:
        n: A non-negative integer
    
    Returns:
        True if n is a power of 2, False otherwise
    """
    # A power of 2, and only a power of 2, has exactly one bit set
    # Corner case: n=0 is not a power of 2
    return n > 0 and (n & (n - 1)) == 0


def get_bit(n, position):
    """
    Get the bit value at the specified position in n.
    
    Args:
        n: A non-negative integer
        position: The position to get (0-indexed from right)
    
    Returns:
        0 or 1, the bit value at the specified position
    """
    # Shift 1 to the position then AND with n
    return (n >> position) & 1


def set_bit(n, position):
    """
    Set the bit at the specified position to 1.
    
    Args:
        n: A non-negative integer
        position: The position to set (0-indexed from right)
    
    Returns:
        New integer with bit set
    """
    return n | (1 << position)


def clear_bit(n, position):
    """
    Clear the bit at the specified position (set to 0).
    
    Args:
        n: A non-negative integer
        position: The position to clear (0-indexed from right)
    
    Returns:
        New integer with bit cleared
    """
    # Create a mask with a 0 at the position and 1s elsewhere
    mask = ~(1 << position)
    return n & mask


def toggle_bit(n, position):
    """
    Toggle (flip) the bit at the specified position.
    
    Args:
        n: A non-negative integer
        position: The position to toggle (0-indexed from right)
    
    Returns:
        New integer with bit toggled
    """
    return n ^ (1 << position)


def test_bit_operations():
    """Test the bit operation functions"""
    # Test count_set_bits
    print("count_set_bits(0):", count_set_bits(0))
    print("count_set_bits(1):", count_set_bits(1))
    print("count_set_bits(5):", count_set_bits(5))  # 101 in binary
    print("count_set_bits(15):", count_set_bits(15))  # 1111 in binary
    
    # Test is_power_of_two
    print("\nis_power_of_two(0):", is_power_of_two(0))
    print("is_power_of_two(1):", is_power_of_two(1))
    print("is_power_of_two(2):", is_power_of_two(2))
    print("is_power_of_two(4):", is_power_of_two(4))
    print("is_power_of_two(5):", is_power_of_two(5))
    print("is_power_of_two(8):", is_power_of_two(8))
    
    # Test get_bit, set_bit, clear_bit, toggle_bit
    n = 42  # Binary: 101010
    print("\nBinary representation of 42:", bin(n))
    
    for i in range(6):
        print(f"get_bit(42, {i}):", get_bit(n, i))
    
    print("\nset_bit(42, 0):", set_bit(n, 0), "Binary:", bin(set_bit(n, 0)))
    print("set_bit(42, 3):", set_bit(n, 3), "Binary:", bin(set_bit(n, 3)))
    
    print("\nclear_bit(42, 1):", clear_bit(n, 1), "Binary:", bin(clear_bit(n, 1)))
    print("clear_bit(42, 5):", clear_bit(n, 5), "Binary:", bin(clear_bit(n, 5)))
    
    print("\ntoggle_bit(42, 0):", toggle_bit(n, 0), "Binary:", bin(toggle_bit(n, 0)))
    print("toggle_bit(42, 1):", toggle_bit(n, 1), "Binary:", bin(toggle_bit(n, 1)))


##############################
# Solution 13: Linked Lists
##############################

class LLNode:
    """
    A node in a linked list.
    
    Attributes:
        data: The value stored in the node
        next: Reference to the next node
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)


class LinkedList:
    """
    A singly linked list.
    
    Attributes:
        head: Reference to the first node
        size: Number of nodes in the list
    """
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Check if the list is empty"""
        return self.head is None
    
    def append(self, data):
        """Add a new node with data at the end of the list"""
        new_node = LLNode(data)
        
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            # Traverse to the last node
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def prepend(self, data):
        """Add a new node with data at the beginning of the list"""
        new_node = LLNode(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert(self, data, position):
        """Insert a new node at the specified position"""
        if position < 0 or position > self.size:
            raise IndexError("Position out of range")
        
        # Prepend if position is 0
        if position == 0:
            self.prepend(data)
            return
        
        new_node = LLNode(data)
        current = self.head
        
        # Traverse to the node just before the insertion point
        for _ in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def remove(self, data):
        """Remove the first node with the specified data"""
        if self.is_empty():
            raise ValueError("List is empty")
        
        # Special case: remove head
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        
        # Search for the node to remove
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        # If data was not found
        if not current.next:
            raise ValueError("Value not found in the list")
        
        # Remove the node
        current.next = current.next.next
        self.size -= 1
    
    def find(self, data):
        """Check if data exists in the list"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def get_at(self, position):
        """Get the data at the specified position"""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of range")
        
        current = self.head
        for _ in range(position):
            current = current.next
        
        return current.data
    
    def __len__(self):
        """Return the number of nodes in the list"""
        return self.size
    
    def __str__(self):
        """Return a string representation of the list"""
        if self.is_empty():
            return "[]"
        
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        
        return "[" + " -> ".join(result) + "]"


def test_linked_list():
    """Test the LinkedList class"""
    # Create an empty linked list
    linked_list = LinkedList()
    print("Is empty:", linked_list.is_empty())
    print("List:", linked_list)
    
    # Append elements
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    print("\nAfter appending 10, 20, 30:")
    print("List:", linked_list)
    print("Size:", len(linked_list))
    
    # Prepend elements
    linked_list.prepend(5)
    print("\nAfter prepending 5:")
    print("List:", linked_list)
    
    # Insert at position
    linked_list.insert(15, 2)
    print("\nAfter inserting 15 at position 2:")
    print("List:", linked_list)
    
    # Get element at position
    print("\nElement at position 2:", linked_list.get_at(2))
    try:
        print("Element at position 10:", linked_list.get_at(10))
    except IndexError as e:
        print("Error:", e)
    
    # Find elements
    print("\nFind 15:", linked_list.find(15))
    print("Find 25:", linked_list.find(25))
    
    # Remove elements
    linked_list.remove(15)
    print("\nAfter removing 15:")
    print("List:", linked_list)
    
    linked_list.remove(5)
    print("\nAfter removing 5:")
    print("List:", linked_list)
    
    linked_list.remove(30)
    print("\nAfter removing 30:")
    print("List:", linked_list)
    
    # Try to remove a non-existent element
    print("\nTrying to remove 100:")
    try:
        linked_list.remove(100)
    except ValueError as e:
        print("Error:", e)

"""
Solutions for Recursive Algorithms
"""

##############################
# Solution 14: Loop Logic and Recursive Algorithms
##############################

def factorial_iterative(n):
    """
    Calculate factorial of n using iteration.
    
    Args:
        n: A non-negative integer
    
    Returns:
        n!
    """
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """
    Calculate factorial of n using recursion.
    
    Args:
        n: A non-negative integer
    
    Returns:
        n!
    """
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial_recursive(n - 1)


def fibonacci_iterative(n):
    """
    Calculate the nth Fibonacci number using iteration.
    
    Args:
        n: A non-negative integer
    
    Returns:
        The nth Fibonacci number
    """
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers")
    
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
        n: A non-negative integer
    
    Returns:
        The nth Fibonacci number
    """
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers")
    
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive case
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def sum_digits_iterative(n):
    """
    Calculate the sum of digits in n using iteration.
    
    Args:
        n: A non-negative integer
    
    Returns:
        Sum of digits in n
    """
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    total = 0
    while n > 0:
        total += n % 10  # Add the last digit
        n //= 10         # Remove the last digit
    return total


def sum_digits_recursive(n):
    """
    Calculate the sum of digits in n using recursion.
    
    Args:
        n: A non-negative integer
    
    Returns:
        Sum of digits in n
    """
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    # Base case
    if n < 10:
        return n
    
    # Recursive case: add last digit + sum of remaining digits
    return n % 10 + sum_digits_recursive(n // 10)


def gcd_iterative(a, b):
    """
    Calculate greatest common divisor of a and b using iteration (Euclidean algorithm).
    
    Args:
        a, b: Integers
    
    Returns:
        The greatest common divisor of a and b
    """
    a, b = abs(a), abs(b)
    
    # Handle special case
    if a == 0:
        return b
    if b == 0:
        return a
    
    while b:
        a, b = b, a % b
    
    return a


def gcd_recursive(a, b):
    """
    Calculate greatest common divisor of a and b using recursion (Euclidean algorithm).
    
    Args:
        a, b: Integers
    
    Returns:
        The greatest common divisor of a and b
    """
    a, b = abs(a), abs(b)
    
    # Base case
    if b == 0:
        return a
    
    # Recursive case
    return gcd_recursive(b, a % b)


def binary_search_iterative(arr, target):
    """
    Perform binary search for target in sorted array using iteration.
    
    Args:
        arr: A sorted list
        target: The value to search for
    
    Returns:
        Index of the target if found, otherwise -1
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Perform binary search for target in sorted array using recursion.
    
    Args:
        arr: A sorted list
        target: The value to search for
        left: The left index of the current search range
        right: The right index of the current search range
    
    Returns:
        Index of the target if found, otherwise -1
    """
    if right is None:
        right = len(arr) - 1
    
    # Base case: target not found
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def test_recursive_algorithms():
    """Test all recursive and iterative algorithm implementations"""
    # Test factorial
    print("Testing factorial functions:")
    for n in range(6):
        print(f"factorial_iterative({n}) = {factorial_iterative(n)}")
        print(f"factorial_recursive({n}) = {factorial_recursive(n)}")
        print()
    
    # Test Fibonacci
    print("Testing Fibonacci functions:")
    for n in range(10):
        print(f"fibonacci_iterative({n}) = {fibonacci_iterative(n)}")
        print(f"fibonacci_recursive({n}) = {fibonacci_recursive(n)}")
        print()
    
    # Test sum of digits
    print("Testing sum of digits functions:")
    test_numbers = [123, 45678, 9]
    for num in test_numbers:
        print(f"sum_digits_iterative({num}) = {sum_digits_iterative(num)}")
        print(f"sum_digits_recursive({num}) = {sum_digits_recursive(num)}")
        print()
    
    # Test GCD
    print("Testing GCD functions:")
    test_pairs = [(48, 18), (101, 103), (36, 120)]
    for a, b in test_pairs:
        print(f"gcd_iterative({a}, {b}) = {gcd_iterative(a, b)}")
        print(f"gcd_recursive({a}, {b}) = {gcd_recursive(a, b)}")
        print()
    
    # Test binary search
    print("Testing binary search functions:")
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    targets = [7, 11, 20]
    for target in targets:
        print(f"binary_search_iterative(arr, {target}) = {binary_search_iterative(arr, target)}")
        print(f"binary_search_recursive(arr, {target}) = {binary_search_recursive(arr, target)}")
        print()


##############################
# Main function to run all tests
##############################

# def main():
    


##############################
# Main function to run all tests
##############################

def main():
    print("=" * 60)
    print("Testing Book Collection:")
    print("=" * 60)
    test_book_collection()
    
    print("\n" + "=" * 60)
    print("Testing Shape Hierarchy:")
    print("=" * 60)
    test_shape_hierarchy()
    
    print("\n" + "=" * 60)
    print("Testing Playlist Manager:")
    print("=" * 60)
    test_playlist_manager()
    
    print("\n" + "=" * 60)
    print("Testing Weather Station:")
    print("=" * 60)
    test_weather_station()
    
    print("\n" + "=" * 60)
    print("Testing Bank Account Hierarchy:")
    print("=" * 60)
    test_bank_account_hierarchy()
    
    print("\n" + "=" * 60)
    print("Testing Event Registration System:")
    print("=" * 60)
    test_event_registration_system()
    
    print("\n" + "=" * 60)
    print("Testing Library System:")
    print("=" * 60)
    test_library_system()
    
    print("\n" + "=" * 60)
    print("Testing Store Inventory System:")
    print("=" * 60)
    test_inventory_system()
    
    print("\n" + "=" * 60)
    print("Testing Binary Search Tree:")
    print("=" * 60)
    test_binary_search_tree()
    
    print("\n" + "=" * 60)
    print("Testing Game Character System:")
    print("=" * 60)
    test_game_character_system()

    print("=" * 60)
    print("Testing Lambda Functions and Functional Programming:")
    print("=" * 60)
    test_lambda_functions()
    
    print("\n" + "=" * 60)
    print("Testing Bit Operations:")
    print("=" * 60)
    test_bit_operations()
    
    print("\n" + "=" * 60)
    print("Testing Linked Lists:")
    print("=" * 60)
    test_linked_list()
    
    print("\n" + "=" * 60)
    print("Testing Recursive Algorithms:")
    print("=" * 60)
    test_recursive_algorithms()


if __name__ == "__main__":
    main()