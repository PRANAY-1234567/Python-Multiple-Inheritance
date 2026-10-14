# Python Multiple Inheritance

## 📌 Overview

This project demonstrates **Multiple Inheritance in Python** using simple examples and real-world scenarios.

Multiple inheritance allows a child class to inherit properties and methods from two or more parent classes.

This project explores how Python handles multiple parent classes, constructors, method overriding, and the `super()` function.

## 🎯 Concepts Covered

* Multiple Inheritance
* Classes and Objects
* Constructors (`__init__`)
* The `super()` Function
* Method Overriding
* Accessing Parent Class Methods
* Initializing Multiple Parent Classes

## 📚 Examples Included

### 1. Basic Multiple Inheritance

The first example introduces three classes:

* `Parent_1`
* `Parent_2`
* `Child`

The `Child` class inherits from both `Parent_1` and `Parent_2`.

```python
class Child(Parent_1, Parent_2):
    pass
```

**Key concept:** A child class can inherit functionality from multiple parent classes.

### 2. Real-World Example: Family Inheritance

This example demonstrates inheritance using a family scenario.

**Classes:**

* `Dad`: Defines the `Property()` method.
* `Mom`: Defines the `Food()` method.
* `Child`: Inherits from both `Dad` and `Mom` and defines its own `Happy()` method.

The child object can access methods from both parents.

```python
c = Child()
c.Property()
c.Food()
c.Happy()
```

**Learning outcome:** Understand how one child class can use methods from two parent classes.

### 3. Method Overriding and `super()`

This example contains three classes: `A`, `B`, and `C`.

Both `A` and `B` define a method called `one()`.

The class `C` inherits from both classes and overrides the same method.

```python
class C(A, B):
    def one(self):
        super().one()
        B.one(self)
        print("@+#")
```

**Key concepts:**

* `super().one()` calls the next implementation according to Python's Method Resolution Order (MRO).
* `B.one(self)` explicitly calls the method defined in class `B`.
* The final `print()` statement executes after both method calls.

Because `C` inherits from `A` first, `super().one()` calls `A.one()` in this example.

### 4. Constructors in Multiple Inheritance

This example explores constructors in classes `x`, `y`, and `Z`.

Both parent classes define their own `__init__()` methods.

The child class `Z` can initialize parent classes to access their functionality.

**Important:** The original example contains incomplete syntax (`y.`), so it needs correction before it can execute.

When working with multiple inheritance, you can explicitly call each parent constructor or use cooperative inheritance with `super()` and a consistent constructor structure.

### 5. Person, Teacher, and Employee

This example demonstrates multiple inheritance in a professional environment.

**Classes:**

**`Person`**

* Stores a person's name, age, and location.
* Displays personal details.

**`Teacher`**

* Stores the teacher's name, subject, and total teaching hours.
* Displays teaching information.

**`Employee`**

* Inherits from both `Person` and `Teacher`.
* Stores employee salary, ID, and role.
* Displays combined information from both parent classes.

Example:

```python
class Employee(Person, Teacher):
    pass
```

The `Employee` class combines personal details, teaching information, and employment information.

**Learning outcome:** Understand how multiple inheritance can combine related information from different classes.

### 6. Bike and Car Showroom

This example demonstrates multiple inheritance using a vehicle showroom scenario.

**Classes:**

* `Showroom1`: Stores bike information.
* `Car_Showroom`: Stores car information.
* `Both_Information`: Inherits from both showroom classes and stores additional details such as color, model, and engine type.

The child class combines information about bikes and cars.

The example also demonstrates method overriding because all three classes define a method called `show()`.

**Important:** The original example uses `super().show()` and `Car_Showroom.show(self)` to call the parent implementations explicitly.

### 7. Constructors in Bike and Car Showrooms

This example extends the showroom scenario by using constructors.

Both parent classes define their own `__init__()` methods.

The child class attempts to initialize both parent classes and then display combined information.

**Important:** The original code has incorrect constructor calls:

```python
super().__init__(self, name, type)
Car_Showroom(self, name1, type1)
```

These calls are incorrect because `super().__init__()` already passes `self` automatically, and `Car_Showroom(...)` creates a new object rather than initializing the current child object.
For explicit parent initialization, the calls should follow this pattern:

```python
Showroom1.__init__(self, name, type)
Car_Showroom.__init__(self, name1, type1)
```

This is suitable for demonstrating explicit constructor calls, although cooperative inheritance with `super()` is preferable for more complex inheritance hierarchies.

### 8. Student and Gamer: ProGamer

The final example demonstrates multiple inheritance through a gaming scenario.

**Classes:**

#### `Student`

Stores the student's name and displays it using the `display()` method.

#### `Gamer`

Stores the game name and game level and displays them using the `show()` method.

#### `ProGamer`

Inherits from both `Student` and `Gamer`.

It initializes both parent classes and adds a rank attribute.

```python
class ProGamer(Student, Gamer):
    def __init__(self, name, game_name, level, Rank):
        Student.__init__(self, name)
        Gamer.__init__(self, game_name, level)
        self.rank = Rank
```

The `ProGamer` class combines student information, gaming information, and player rank.

**Learning outcome:** Understand how a class can combine features from multiple parent classes to represent a more specific entity.

## 💻 Sample Code

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Student name is {self.name}")


class Gamer:
    def __init__(self, game_name, level):
        self.gn = game_name
        self.l = level

    def show(self):
        print(f"Game name is {self.gn}")
        print(f"Game level is {self.l}")

class ProGamer(Student, Gamer):
    def __init__(self, name, game_name, level, Rank):
        Student.__init__(self, name)
        Gamer.__init__(self, game_name, level)
        self.rank = Rank

    def Final(self):
        print(f"Game Rank is {self.rank}")


x = ProGamer("Pranay", "FreeFire", "Gold", 1)

x.display()
x.show()
x.Final()
```

## 📤 Sample Output

```text
Student name is Pranay
Game name is FreeFire
Game level is Gold
Game Rank is 1
```

**Note:** The original object creation was:

```python
x = ProGamer("FreeFire", "Bronze", "Gold", 1)
```

This is valid Python, but the arguments do not clearly represent the intended values. The corrected example uses `"Pranay"` as the student name, `"FreeFire"` as the game name, `"Gold"` as the game level, and `1` as the rank.

## 🛠️ Technologies Used

* Python 3
* Object-Oriented Programming (OOP)

## ▶️ How to Run

1. Install Python 3.
2. Copy the desired example into a Python file.
3. Save the file as `multiple_inheritance.py`.
4. Open a terminal in the file's directory.
5. Execute:

```bash
python multiple_inheritance.py
```

**Note:** Some earlier examples contain incomplete or incorrect code. Correct those examples before running them.

## 📈 Learning Outcomes

After completing these examples, you should understand:

* How multiple inheritance works in Python.
* How to inherit methods from two or more parent classes.
* How to override methods in child classes.
* How to initialize multiple parent classes.
* How `super()` works with Python's Method Resolution Order.
* How multiple inheritance can represent real-world scenarios.

## 👨‍💻 Author

**Pranay Jadhao**

Learning Python, Object-Oriented Programming, and software development.
