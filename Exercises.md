Hritvik JV
Winter 2025

# Python Exercises for CS211


## Exercise 1: Book Collection

**Concepts:** Basic class definition, constructor, string representation methods

Create a Python class named 'Book' to represent book information.
Implement the following methods:
1. `__init__`
2. `__str__`
3. `__repr__`
4. `add_review`
5. `get_average_rating`
6. `is_recommended`

A Book has three attributes:
- title: a string
- author: a string
- reviews: a list of ratings (1-5)

The `add_review` method should add a new rating to the reviews list.
The `get_average_rating` method should return the average of all ratings.
The `is_recommended` method should return True if average rating is >= 4.0.

### Test Case:
```python
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
```

### Expected Output:
```
"The Hobbit" by J.R.R. Tolkien
Book("The Hobbit", "J.R.R. Tolkien")
The Hobbit average rating: 4.666666666666667
Harry Potter average rating: 3.3333333333333335
The Hobbit is recommended: True
Harry Potter is recommended: False
```

## Exercise 2: Shape Hierarchy

**Concepts:** Inheritance, method overriding

Create a Python class named 'Shape' (abstract base class).
Then create three subclasses: 'Rectangle', 'Circle', and 'Triangle'.

The Shape class should have:
- An abstract method 'area()' that returns the area of the shape
- An abstract method 'perimeter()' that returns the perimeter of the shape

Rectangle:
- Attributes: width, height
- Override area() and perimeter() for a rectangle

Circle:
- Attribute: radius
- Override area() and perimeter() for a circle (use math.pi)

Triangle:
- Attributes: side1, side2, side3 (the three sides of the triangle)
- Override area() (use Heron's formula) and perimeter()

### Test Case:
```python
import math

# Create shapes
rect = Rectangle(5, 3)
circle = Circle(4)
triangle = Triangle(3, 4, 5)

# Test area and perimeter
print(f"{rect} - Area: {rect.area()}, Perimeter: {rect.perimeter()}")
print(f"{circle} - Area: {circle.area():.2f}, Perimeter: {circle.perimeter():.2f}")
print(f"{triangle} - Area: {triangle.area()}, Perimeter: {triangle.perimeter()}")
```

### Expected Output:
```
Rectangle(width=5, height=3) - Area: 15, Perimeter: 16
Circle(radius=4) - Area: 50.27, Perimeter: 25.13
Triangle(sides=3, 4, 5) - Area: 6.0, Perimeter: 12
```

## Exercise 3: Playlist Manager

**Concepts:** Aggregation, list manipulation, custom methods

Create a Python class named 'Song' with attributes:
- title: string
- artist: string
- duration: integer (seconds)

Create a class 'Playlist' that manages a collection of Song objects:
- name: string (name of playlist)
- songs: list of Song objects
    
Implement methods:
- add_song(song): adds a Song to the playlist
- remove_song(title): removes a Song by title
- total_duration(): returns the sum of all song durations
- shuffle(): returns a new Playlist with songs in random order
- filter_by_artist(artist): returns a new Playlist with songs by the given artist

### Test Case:
```python
import random

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
```

### Expected Output (shuffle output will vary):
```
Playlist: Classic Rock (4 songs, 17:29)
1. "Bohemian Rhapsody" by Queen (5:54)
2. "Hotel California" by Eagles (6:30)
3. "We Will Rock You" by Queen (2:02)
4. "Imagine" by John Lennon (3:03)

Playlist: Queen songs from Classic Rock (2 songs, 7:56)
1. "Bohemian Rhapsody" by Queen (5:54)
2. "We Will Rock You" by Queen (2:02)

Total duration: 17:29

Removed: "Imagine" by John Lennon (3:03)
Playlist: Classic Rock (3 songs, 14:26)
1. "Bohemian Rhapsody" by Queen (5:54)
2. "Hotel California" by Eagles (6:30)
3. "We Will Rock You" by Queen (2:02)
```

## Exercise 4: Weather Station

**Concepts:** Data encapsulation, data processing

Create a Python class named 'WeatherData' to store a single weather reading:
- temperature: float (in Celsius)
- humidity: float (percentage)
- pressure: float (hPa)
- timestamp: string (in format "YYYY-MM-DD HH:MM")

Create a class 'WeatherStation' that collects WeatherData objects:
- location: string
- readings: list of WeatherData objects

Implement methods:
- add_reading(reading): adds a WeatherData object to readings
- avg_temperature(): returns the average temperature
- min_temperature(): returns the minimum temperature
- max_temperature(): returns the maximum temperature
- get_readings_by_date(date): returns readings from a specific date ("YYYY-MM-DD")

### Test Case:
```python
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
```

### Expected Output:
```
Weather Station at Portland (5 readings)
Temperature range: 18.7°C to 26.8°C
Average temperature: 23.3°C

Readings for 2023-06-10:
[2023-06-10 08:00] Temp: 23.5°C, Humidity: 65.0%, Pressure: 1013.2 hPa
[2023-06-10 12:00] Temp: 26.8°C, Humidity: 60.2%, Pressure: 1012.1 hPa
[2023-06-10 16:00] Temp: 25.1°C, Humidity: 62.5%, Pressure: 1011.8 hPa
```

## Exercise 5: BankAccount Hierarchy

**Concepts:** Inheritance, polymorphism, method overriding

Create a base class 'BankAccount' with:
- account_number: string
- holder_name: string
- balance: float
 
Methods:
- deposit(amount): adds to balance
- withdraw(amount): subtracts from balance if sufficient funds
- get_balance(): returns current balance

Create subclasses:
1. SavingsAccount (extends BankAccount)
   - interest_rate: float (percentage)
   - Add method apply_interest(): increases balance by interest rate

2. CheckingAccount (extends BankAccount)
   - transaction_fee: float
   - Override withdraw() to deduct the transaction fee

3. CreditAccount (extends BankAccount)
   - credit_limit: float
   - interest_rate: float
   - Override withdraw() to allow negative balance up to credit limit
   - Add method apply_interest(): applies interest only on negative balance

### Test Case:
```python
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
```

### Expected Output:
```
Initial state:
SavingsAccount (S123): Alice Smith, Balance: $1000.00
CheckingAccount (C456): Bob Johnson, Balance: $500.00
CreditAccount (R789): Charlie Brown, Balance: $0.00

After transactions:
SavingsAccount (S123): Alice Smith, Balance: $1575.00 (Interest earned: $75.00)
CheckingAccount (C456): Bob Johnson, Balance: $98.50
CreditAccount (R789): Charlie Brown, Balance: $-1800.00 (Interest charged: $300.00)
```

## Exercise 6: Event Registration System

**Concepts:** Classes with relationships, data management

Create a class 'Participant' with:
- name: string
- email: string
- phone: string

Create a class 'Event' with:
- name: string
- date: string
- venue: string
- max_participants: integer
- registered: list of Participant objects

Methods:
- register(participant): add participant if space available
- unregister(email): remove participant with matching email
- is_full(): returns True if event is at capacity
- get_available_spots(): returns number of available spots
- get_participant_list(): returns formatted list of participants

Create a class 'EventManager' with:
- events: list of Event objects

Methods:
- add_event(event): adds an Event
- remove_event(name): removes an Event by name
- get_events_by_date(date): returns events on a specific date
- register_participant(event_name, participant): registers participant for event

### Test Case:
```python
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
```

### Expected Output:
```
Event Manager (3 events)

All events:
Tech Conference on 2023-09-15 at Convention Center (0/200 participants)
Python Workshop on 2023-09-15 at University Lab (2/30 participants)
Developer Meetup on 2023-09-20 at Startup Hub (2/50 participants)

Events on 2023-09-15:
Tech Conference on 2023-09-15 at Convention Center (0/200 participants)
Python Workshop on 2023-09-15 at University Lab (2/30 participants)

Python Workshop participants:
1. John Doe (john@example.com)
2. Jane Smith (jane@example.com)

Removed: Jane Smith (jane@example.com)
Available spots in workshop: 29
```

## Exercise 7: Library System

**Concepts:** data management

Create a class 'Book' with:
- title: string
- author: string
- isbn: string
- published_year: integer
- available: boolean (True if book is available, False if checked out)

Create a class 'Member' with:
- name: string
- member_id: string
- books_checked_out: list of Book objects

Create a class 'Library' with:
- name: string
- books: list of Book objects
- members: list of Member objects

Methods:
- add_book(book): adds a Book
- add_member(member): adds a Member
- check_out_book(isbn, member_id): checks out a Book to a Member
- return_book(isbn): marks a Book as available
- search_by_title(title): returns Books with matching title
- search_by_author(author): returns Books by matching author
- get_available_books(): returns all available Books
- get_checked_out_books(): returns all checked out Books

### Test Case:
```python
# Create library
library = Library("Community Library")

# Create books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1925)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", 1960)
book3 = Book("1984", "George Orwell", "9780451524935", 1949)
book4 = Book("Pride and Prejudice", "Jane Austen", "9780141439518", 1813)
book5 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488", 1951)

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
```

### Expected Output:
```
Library: Community Library

Available books:
"Pride and Prejudice" by Jane Austen (1813) [ISBN: 9780141439518] - Available
"The Catcher in the Rye" by J.D. Salinger (1951) [ISBN: 9780316769488] - Available

Checked out books:
"The Great Gatsby" by F. Scott Fitzgerald (1925) [ISBN: 9780743273565] - Checked Out
"To Kill a Mockingbird" by Harper Lee (1960) [ISBN: 9780061120084] - Checked Out
"1984" by George Orwell (1949) [ISBN: 9780451524935] - Checked Out

Books by Jane Austen:
"Pride and Prejudice" by Jane Austen (1813) [ISBN: 9780141439518] - Available

After returning The Great Gatsby:
Books checked out by Alice: 1
Available books: 3
```

## Exercise 8: Store Inventory System

**Concepts:** Inheritance, polymorphism

Create a class 'Product' with:
- name: string
- price: float
- product_id: string
- quantity: integer

Methods:
- calculate_value(): returns price * quantity
- update_quantity(amount): increases or decreases quantity
- is_in_stock(): returns True if quantity > 0

Create derived classes:
1. Perishable (extends Product)
   - expiry_date: string
   - Add method is_expired(current_date): checks if product is expired
   - Override calculate_value() to return 0 if product is expired

2. Electronics (extends Product)
   - warranty_months: integer
   - brand: string
   - Override calculate_value() to include 10% markup

3. Clothing (extends Product)
   - size: string
   - color: string
   - Override calculate_value() with seasonal discounts

Create a class 'Inventory' with:
- products: list of Product objects

Methods:
- add_product(product): adds a Product
- remove_product(product_id): removes a Product by ID
- get_total_value(): returns sum of all product values
- find_product(product_id): finds a product by ID
- get_products_by_type(product_type): returns products of a specific type
- get_low_stock_products(threshold): returns products with quantity <= threshold

### Test Case:
```python
from datetime import datetime

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
```

### Expected Output:
```
Inventory Summary:
Total products: 3
Total value: $3574.94

Electronics products:
Smart TV (ID: E001) - $499.99 x 5 = $2749.95 - Brand: Samsung, Warranty: 24 months

Low stock products (threshold=10):
Smart TV (ID: E001) - $499.99 x 5 = $2749.95 - Brand: Samsung, Warranty: 24 months

Is apple expired on 2023-06-10? False
Is apple expired on 2023-06-20? True

After quantity updates:
Apples in stock: 80 (Value: $40.00)
TVs in stock: 7 (Value: $3849.92)
```

## Exercise 9: Binary Search Tree

**Concepts:** Tree data structure, recursion

Create a class 'Node' with:
- value: integer
- left: Node (or None)
- right: Node (or None)

Create a class 'BinarySearchTree' with:
- root: Node (or None)

Methods:
- insert(value): inserts a new value into the tree
- search(value): returns True if value exists in tree
- delete(value): removes a value from the tree
- in_order_traversal(): returns list of values in-order
- pre_order_traversal(): returns list of values pre-order
- post_order_traversal(): returns list of values post-order
- find_min(): returns smallest value in tree
- find_max(): returns largest value in tree
- get_height(): returns height of tree

### Test Case:
```python
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
```

### Expected Output:
```
In-order traversal: [20, 30, 40, 50, 60, 70, 80]
Pre-order traversal: [50, 30, 20, 40, 70, 60, 80]
Post-order traversal: [20, 40, 30, 60, 80, 70, 50]

Search tests:
Search for 40: True
Search for 55: False

Minimum value: 20
Maximum value: 80

Tree height: 2

After deleting 20:
In-order traversal: [30, 40, 50, 60, 70, 80]

After deleting 30:
In-order traversal: [40, 50, 60, 70, 80]

After deleting 50 (root):
In-order traversal: [40, 60, 70, 80]
```

## Exercise 10: Game Character System

**Concepts:** Inheritance, polymorphism

Create a base class 'Character' with:
- name: string
- health: integer
- level: integer

Methods:
- attack(): returns base attack power
- take_damage(amount): reduces health
- heal(amount): increases health
- is_alive(): returns True if health > 0
- level_up(): increases level and enhances stats

Create derived classes:
1. Warrior (extends Character)
   - strength: integer
   - armor: integer
   - Override attack() using strength
   - Override take_damage() to account for armor
   - Add rage_attack(): stronger attack that costs health

2. Mage (extends Character)
   - mana: integer
   - intelligence: integer
   - Override attack() using intelligence and mana
   - Add cast_spell(spell_name): different effects based on spell
   - Add restore_mana(amount): increases mana

3. Archer (extends Character)
   - dexterity: integer
   - arrows: integer
   - Override attack() using dexterity
   - Add aimed_shot(): stronger attack that uses more arrows
   - Add craft_arrows(amount): increases arrows

### Test Case:
```python
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
```

### Expected Output:
```
Initial character stats:
Warrior: Aragorn (Level 1) - Health: 100, Strength: 15, Armor: 10
Mage: Gandalf (Level 1) - Health: 80, Mana: 100, Intelligence: 20
Archer: Legolas (Level 1) - Health: 90, Dexterity: 18, Arrows: 30

Basic attacks:
Aragorn attacks for 15 damage
Gandalf attacks for 20 damage
Legolas attacks for 18 damage

Special abilities:
Aragorn rage attacks for 30 damage (Health: 90)
Gandalf casts fireball for 35 damage (Mana: 70)
Legolas uses aimed shot for 36 damage (Arrows: 27)

Taking damage:
Aragorn health after damage: 80
Gandalf health after damage: 50
Legolas health after damage: 65

After leveling up:
Warrior: Aragorn (Level 2) - Health: 120, Strength: 18, Armor: 12
Mage: Gandalf (Level 2) - Health: 70, Mana: 120, Intelligence: 24
Archer: Legolas (Level 2) - Health: 85, Dexterity: 22, Arrows: 30
```

## Exercise 11: Lambda Functions and Functional Programming

**Concepts:** Lambda functions, higher-order functions, functional programming

Create a module called `functional_tools.py` with the following functions:

1. `map_values(func, values)`: 
   - Takes a function and a list of values
   - Returns a new list with the function applied to each value
   - Implement this using a lambda function, not Python's built-in `map()`

2. `filter_values(predicate, values)`:
   - Takes a predicate function (returns True/False) and a list of values
   - Returns a new list containing only values for which the predicate returns True
   - Implement this using a lambda function, not Python's built-in `filter()`

3. `string_processor()`:
   - Returns a dictionary of lambda functions that process strings in various ways
   - The dictionary should have the following keys and functions:
     - "uppercase": converts a string to uppercase
     - "lowercase": converts a string to lowercase
     - "capitalize": capitalizes the first letter of each word
     - "reverse": reverses the string
     - "word_count": returns the number of words in the string
     - "remove_spaces": removes all spaces from the string

4. `compose(f, g)`:
   - Takes two functions f and g
   - Returns a new function that computes f(g(x)) for any input x
   - Use this to create a function `process_pipeline` that takes a list of functions and returns a single function that applies them in sequence

### Test Case:
```python
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
```

### Expected Output:
```
Squared numbers: [1, 4, 9, 16, 25]
Even numbers: [2, 4]
uppercase: HELLO WORLD
lowercase: hello world
capitalize: Hello World
reverse: dlrow olleh
word_count: 2
remove_spaces: helloworld
double_then_add_one(5): 11
pipeline(5): 25
```

## Exercise 12: Bit Operations

**Concepts:** Bitwise operations, binary representation, bit manipulation

Create a module called `bitwise_operations.py` with the following functions:

1. `count_set_bits(n)`:
   - Counts the number of '1' bits in the binary representation of integer n
   - Implement this using bitwise operations, not by converting to a string

2. `is_power_of_two(n)`:
   - Returns True if n is a power of 2, False otherwise
   - Implement this using bitwise operations
   - Handle the case where n is 0 correctly

3. `get_bit(n, position)`:
   - Returns the bit value at the given position (0-indexed from right) in integer n
   - Returns 0 or 1

4. `set_bit(n, position)`:
   - Sets the bit at the given position to 1 and returns the new number
   - Does not modify the original number

5. `clear_bit(n, position)`:
   - Sets the bit at the given position to 0 and returns the new number
   - Does not modify the original number

6. `toggle_bit(n, position)`:
   - Flips the bit at the given position and returns the new number
   - Does not modify the original number

### Test Case:
```python
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
```

### Expected Output:
```
count_set_bits(0): 0
count_set_bits(1): 1
count_set_bits(5): 2
count_set_bits(15): 4

is_power_of_two(0): False
is_power_of_two(1): True
is_power_of_two(2): True
is_power_of_two(4): True
is_power_of_two(5): False
is_power_of_two(8): True

Binary representation of 42: 0b101010
get_bit(42, 0): 0
get_bit(42, 1): 1
get_bit(42, 2): 0
get_bit(42, 3): 1
get_bit(42, 4): 0
get_bit(42, 5): 1

set_bit(42, 0): 43 Binary: 0b101011
set_bit(42, 3): 42 Binary: 0b101010

clear_bit(42, 1): 40 Binary: 0b101000
clear_bit(42, 5): 10 Binary: 0b1010

toggle_bit(42, 0): 43 Binary: 0b101011
toggle_bit(42, 1): 40 Binary: 0b101000
```

## Exercise 13: Linked Lists

**Concepts:** Linked data structures, references, traversal algorithms

Create a module called `simple_linked_list.py` with the following classes:

1. `Node` class:
   - Attributes: `data` (the value stored in the node) and `next` (reference to the next node)
   - Methods: `__init__(self, data, next=None)` and `__str__(self)`

2. `LinkedList` class:
   - Attributes: `head` (reference to the first node) and `size` (number of nodes)
   - Methods:
     - `__init__(self)`: Initialize an empty list
     - `is_empty(self)`: Return True if the list is empty
     - `append(self, data)`: Add a new node with the given data at the end of the list
     - `prepend(self, data)`: Add a new node with the given data at the beginning of the list
     - `insert(self, data, position)`: Insert a new node at the given position (0-indexed)
     - `remove(self, data)`: Remove the first node containing the given data
     - `find(self, data)`: Return True if the data exists in the list
     - `get_at(self, position)`: Return the data at the given position
     - `__len__(self)`: Return the number of nodes in the list
     - `__str__(self)`: Return a string representation of the list

### Test Case:
```python
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
print("List:", linked_list)
```

### Expected Output:
```
Is empty: True
List: []

After appending 10, 20, 30:
List: [10 -> 20 -> 30]
Size: 3

After prepending 5:
List: [5 -> 10 -> 20 -> 30]

After inserting 15 at position 2:
List: [5 -> 10 -> 15 -> 20 -> 30]

Element at position 2: 15
Error: Position out of range

Find 15: True
Find 25: False

After removing 15:
List: [5 -> 10 -> 20 -> 30]

After removing 5:
List: [10 -> 20 -> 30]

After removing 30:
List: [10 -> 20]

Trying to remove 100:
Error: Value not found in the list
List: [10 -> 20]
```

## Exercise 14: Loop Logic and Recursive Algorithms

**Concepts:** Iteration, recursion, algorithm design

Create a module called `recursive_algorithms.py` with the following functions. For each function, implement both iterative (using loops) and recursive solutions:

1. `factorial_iterative(n)` and `factorial_recursive(n)`:
   - Calculate the factorial of a non-negative integer n

2. `fibonacci_iterative(n)` and `fibonacci_recursive(n)`:
   - Return the nth Fibonacci number (where fibonacci(0) = 0 and fibonacci(1) = 1)

3. `sum_digits_iterative(n)` and `sum_digits_recursive(n)`:
   - Calculate the sum of digits of a non-negative integer n

4. `gcd_iterative(a, b)` and `gcd_recursive(a, b)`:
   - Calculate the greatest common divisor of integers a and b using Euclidean algorithm

5. `binary_search_iterative(arr, target)` and `binary_search_recursive(arr, target, left=0, right=None)`:
   - Perform binary search for target in a sorted array arr
   - Return the index if found, otherwise return -1

### Test Case:
```python
# Test factorial
for n in range(6):
    print(f"factorial_iterative({n}) = {factorial_iterative(n)}")
    print(f"factorial_recursive({n}) = {factorial_recursive(n)}")
    print()

# Test Fibonacci
for n in range(10):
    print(f"fibonacci_iterative({n}) = {fibonacci_iterative(n)}")
    print(f"fibonacci_recursive({n}) = {fibonacci_recursive(n)}")
    print()

# Test sum of digits
test_numbers = [123, 45678, 9]
for num in test_numbers:
    print(f"sum_digits_iterative({num}) = {sum_digits_iterative(num)}")
    print(f"sum_digits_recursive({num}) = {sum_digits_recursive(num)}")
    print()

# Test GCD
test_pairs = [(48, 18), (101, 103), (36, 120)]
for a, b in test_pairs:
    print(f"gcd_iterative({a}, {b}) = {gcd_iterative(a, b)}")
    print(f"gcd_recursive({a}, {b}) = {gcd_recursive(a, b)}")
    print()

# Test binary search
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
targets = [7, 11, 20]
for target in targets:
    print(f"binary_search_iterative(arr, {target}) = {binary_search_iterative(arr, target)}")
    print(f"binary_search_recursive(arr, {target}) = {binary_search_recursive(arr, target, 0, len(arr)-1)}")
    print()
```

### Expected Output:
```
factorial_iterative(0) = 1
factorial_recursive(0) = 1

factorial_iterative(1) = 1
factorial_recursive(1) = 1

factorial_iterative(2) = 2
factorial_recursive(2) = 2

factorial_iterative(3) = 6
factorial_recursive(3) = 6

factorial_iterative(4) = 24
factorial_recursive(4) = 24

factorial_iterative(5) = 120
factorial_recursive(5) = 120

fibonacci_iterative(0) = 0
fibonacci_recursive(0) = 0

fibonacci_iterative(1) = 1
fibonacci_recursive(1) = 1

fibonacci_iterative(2) = 1
fibonacci_recursive(2) = 1

fibonacci_iterative(3) = 2
fibonacci_recursive(3) = 2

fibonacci_iterative(4) = 3
fibonacci_recursive(4) = 3

fibonacci_iterative(5) = 5
fibonacci_recursive(5) = 5

fibonacci_iterative(6) = 8
fibonacci_recursive(6) = 8

fibonacci_iterative(7) = 13
fibonacci_recursive(7) = 13

fibonacci_iterative(8) = 21
fibonacci_recursive(8) = 21

fibonacci_iterative(9) = 34
fibonacci_recursive(9) = 34

sum_digits_iterative(123) = 6
sum_digits_recursive(123) = 6

sum_digits_iterative(45678) = 30
sum_digits_recursive(45678) = 30

sum_digits_iterative(9) = 9
sum_digits_recursive(9) = 9

gcd_iterative(48, 18) = 6
gcd_recursive(48, 18) = 6

gcd_iterative(101, 103) = 1
gcd_recursive(101, 103) = 1

gcd_iterative(36, 120) = 12
gcd_recursive(36, 120) = 12

binary_search_iterative(arr, 7) = 3
binary_search_recursive(arr, 7) = 3

binary_search_iterative(arr, 11) = 5
binary_search_recursive(arr, 11) = 5

binary_search_iterative(arr, 20) = -1
binary_search_recursive(arr, 20) = -1