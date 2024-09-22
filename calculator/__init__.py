'''
So from what I understand the @staticmethod does not need self or class.
It also cannot modifiy object state or class state
Its kind of like a regular function

@classmethod is similar but needs cls to pass in a variable etc
This can change the class state unlike the static one

Instance Method (self): 
### (a function that passes self basically)
This is a regular method that takes self as its first parameter.
It operates on an instance of the class, meaning it can access and modify instance attributes.
Use it when you need to work with data specific to that instance.

Class Method (cls): 
### (works with entire class making code more adjustable)
This method uses @classmethod and takes cls as its first parameter.
It operates on the class itself, not on instances. You can use it to access or modify class attributes.
Use it when you need to work with data shared across all instances (like a count of all instances).

Static Method: 
### (relate to the class but dont need to interact with its data.)
This method uses @staticmethod and doesnt take self or cls.
It behaves like a regular function that belongs to the class but doesnt access instance or class data.
Use it for utility functions that are related to the class but dont need any context from it.

### in the example below @staticmethod is used for the overall functions 
# while the @classmethod was used for the the history that records things that the overall class tracks

Another good example chatgpt gave me that helped me for future reference is bank account
__init__ for self.owner and self.balance as the account

deposit function would be an instance because it puts money into an account for the self.owner

withdraw is another instance because it takes money out of account 

TransactionHistory is a class method because it is a historical use of the entire class

ValidAmount is a static method to check if balance will be negative. 

Basically instance are literally instances a person can use 
Class are things to check historcal things 
Static are things to check validation 



### 
In part 3 the goal was 
'''
# calculator/__init__.py
from calculator.operations import add, subtract, multiply, divide
from calculator.transactions import Transactions

class Calculator:
    '''Calculator class to perform basic operations and track history.'''

    @staticmethod
    def _perform_operation(a: float, b: float, operation) -> float:
        """Create and perform a calculation, then return the result."""
        result = operation(a, b)
        Transactions.add_to_history(operation.__name__, a, b, result)
        return result

    @staticmethod
    def add(a: float, b: float) -> float:
        '''Performs addition and stores the result in the history.'''
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: float, b: float) -> float:
        '''Performs subtraction and stores the result in the history.'''
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: float, b: float) -> float:
        '''Performs multiplication and stores the result in the history.'''
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: float, b: float) -> float:
        '''Performs division using the operation defined in operations.'''
        return Calculator._perform_operation(a, b, divide)

    @classmethod
    def get_history(cls) -> list:
        '''Returns the history of calculations.'''
        return Transactions.get_history()

    @classmethod
    def clear_history(cls) -> None:
        '''Clears the history of calculations.'''
        Transactions.clear_history()
