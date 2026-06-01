# Bank Management System using Python

A console-based banking application developed in Python that demonstrates Object-Oriented Programming (OOP), file handling, data persistence, and exception handling concepts. The system allows users to create and manage bank accounts through a simple menu-driven interface.

## Features

- Create new bank accounts
- View account details
- Deposit money
- Withdraw money
- Store multiple accounts using dictionaries
- Data persistence using JSON files
- Error handling for invalid inputs
- Menu-driven console interface

## Technologies Used

- Python 3.x
- Object-Oriented Programming (OOP)
- JSON File Handling
- Exception Handling
- Dictionaries for Data Storage

## Project Structure

```text
BankManagementSystem/
│
├── bank_management.py
├── accounts.json
└── README.md
```

## Classes

### BankAccount

Represents an individual bank account.

#### Attributes

- `account_number`
- `name`
- `balance`

#### Methods

```python
deposit(amount)
withdraw(amount)
display()
to_dict()
from_dict()
```

### BankSystem

Manages multiple bank accounts and handles user interactions.

#### Responsibilities

- Account creation
- Account lookup
- Deposit and withdrawal operations
- Loading data from JSON file
- Saving data to JSON file

## Data Storage

Accounts are stored in a JSON file named:

```text
accounts.json
```

The application:

- Loads account data when the program starts.
- Saves updated account information automatically after transactions.
- Maintains data even after the application is closed.

### Example JSON Format

```json
{
  "1001": {
    "account_number": "1001",
    "name": "John Doe",
    "balance": 5000
  }
}
```

## How to Run

### Prerequisites

- Python 3.8 or later

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/bank-management-system.git
```

2. Navigate to the project directory:

```bash
cd bank-management-system
```

3. Run the application:

```bash
python bank_management.py
```

## Sample Menu

```text
===== BANK MANAGEMENT SYSTEM =====

1. Create Account
2. View Account
3. Deposit Money
4. Withdraw Money
5. Exit

Enter your choice:
```

## OOP Concepts Demonstrated

### Encapsulation

Each `BankAccount` object manages its own data and operations.

### Constructors

```python
__init__()
```

Used to initialize account details during object creation.

### Objects and Classes

- `BankAccount`
- `BankSystem`

### Instance Methods

- Deposit funds
- Withdraw funds
- Display account information

## Error Handling

The system uses `try-except` blocks to handle:

- Invalid menu selections
- Incorrect account numbers
- Non-numeric input values
- Insufficient balance during withdrawals

## Future Enhancements

- Password-protected accounts
- Transaction history tracking
- Interest calculation
- GUI using Tkinter or PyQt
- Web application using Flask or Django
- Database integration (MySQL/PostgreSQL)

## Learning Outcomes

This project demonstrates:

- Object-Oriented Programming in Python
- File Handling and JSON Persistence
- Data Serialization and Deserialization
- Exception Handling
- Menu-Driven Application Development

## Author

**Vaidik Reddy**

## License

This project is open-source and intended for educational and learning purposes.
