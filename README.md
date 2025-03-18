<a id="top"></a>
# goit-pythonweb-hw-01

<a href="#1"><img src="https://img.shields.io/badge/Task 01-512BD4?style=for-the-badge"/></a> <a href="#2"><img src="https://img.shields.io/badge/Task 02-ECD53F?style=for-the-badge"/></a>

<a id="1"></a>
## Task 01
<img src="https://img.shields.io/badge/Task 01-512BD4?style=for-the-badge"/>

### Explanation:

#### 1. Abstract Base Classes (ABCs):

- Vehicle: Defines the common interface for all vehicles (cars and motorcycles). It has an abstract start_engine() method.
- VehicleFactory: Defines the common interface for vehicle factories, with abstract methods create_car() and create_motorcycle().

#### 2. Concrete Vehicle Classes:

- Car: Implements the Vehicle interface for cars.
- Motorcycle: Implements the Vehicle interface for motorcycles.
- Both classes provide concrete implementations of the start_engine() method, logging messages to indicate engine start.

#### 3. Concrete Vehicle Factory Classes:

- USVehicleFactory: Creates US-specific cars and motorcycles, adding "(US Spec)" to the make.
- EUVehicleFactory: Creates EU-specific cars and motorcycles, adding "(EU Spec)" to the make.

#### 4. Usage:

- Two factories are created: USVehicleFactory and EUVehicleFactory.
- Cars and motorcycles are created using each factory.
- The start_engine() method is called on each vehicle, demonstrating the factory pattern and polymorphism.

#### Key Concepts Demonstrated:

- Abstract Factory Pattern: The VehicleFactory and its subclasses provide a way to create families of related objects (cars and motorcycles) without specifying their concrete classes.
- Abstraction: The Vehicle and VehicleFactory ABCs define abstract interfaces.
- Polymorphism: The start_engine() method behaves differently for cars and motorcycles.
- Encapsulation: Vehicle creation is encapsulated within the factory classes.
- Logging: The logging module is used to display messages when the engines start.

[Top :arrow_double_up:](#top)

<a id="2"></a>
## Task 02
<img src="https://img.shields.io/badge/Task 02-ECD53F?style=for-the-badge"/>

### 1. Single Responsibility Principle (SRP):
- The Book class is now only responsible for storing information about a book.
- The Library class is responsible for operations with the book collection.
- The LibraryManager class is responsible for user interaction and library management.

### 2. Open/Closed Principle (OCP):
- The LibraryInterface interface allows you to add new library implementations without changing the LibraryManager code. For example, you can create an OnlineLibrary that stores books in a database.

### 3. Liskov Substitution Principle (LSP):
- The Library class implements the LibraryInterface interface, so it can be used instead of any other class that implements this interface.

### 4. Interface Separation Principle (ISP):
- The LibraryInterface interface defines only the methods necessary to work with the library.

### 5. Dependency Inversion Principle (DIP):
- The LibraryManager class depends on the LibraryInterface abstraction, not on the specific Library implementation.
- The Book class does not depend on any other classes.

These principles improve the structure of the code, making it more flexible, extensible, and easy to maintain.

[Top :arrow_double_up:](#top)