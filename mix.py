"""
E-commerce shopping system with customer orders and payment processing.
Demonstrates composition (has-a relationship) and inheritance (is-a relationship).
"""


class Customer:
    """
    Base customer class that manages shopping cart and orders.
    Uses composition: Customer HAS-A Cart and HAS-A Products list.
    """
    
    def __init__(self, money):
        """
        Initialize a customer with a cart and empty order list.
        
        Args:
            money: Initial balance to load into the cart
        """
        self.card = Cart(money)
        self.orders = Products()
    
    def Order(self, goods):
        """
        Create a new order with specified product IDs.
        
        Args:
            goods: List of product IDs to order
        """
        self.orders = Products(goods)
    
    def Pay(self):
        """
        Process payment for current orders.
        Prints success or failure message based on available balance.
        """
        result = self.card.Pay(self.orders)
        if result == -1:
            print("Payment failed: Insufficient balance!")
        else:
            print("Payment successful!")

    def ShowBalance(self):
        """Display current cart balance."""
        print(f"Balance: {self.card.balance}")


class Admin:
    """Admin class for managing the system (placeholder for future functionality)."""
    
    def __init__(self):
        pass
    

class Products:
    """
    Product catalog and order management.
    Stores product prices and calculates total cost for selected items.
    """
    
    def __init__(self, goods: list = []):
        """
        Initialize product catalog and order list.
        
        Args:
            goods: List of product IDs in the current order (default: empty)
        """
        # Product catalog: ID -> Price mapping
        self.prices = {
            1: 1000,
            2: 500,
            3: 45000,
            4: 1000.500,
            5: 200000,
            6: 10000
        }
        self.goods = goods
    
    def TotolCost(self):
        """
        Calculate total cost of all items in the order.
        
        Returns:
            Total cost as a float
        """
        cost = 0
        for i in self.goods:
            cost += self.prices[i]
        return cost
    

class Cart:
    """
    Shopping cart that manages customer balance and processes payments.
    """
    
    def __init__(self, balance):
        """
        Initialize cart with starting balance.
        
        Args:
            balance: Initial amount of money in the cart
        """
        self.balance = balance
    
    def Pay(self, prod: Products):
        """
        Process payment for products with 1% tax.
        Deducts total cost + tax from balance if sufficient funds available.
        
        Args:
            prod: Products object containing the order
            
        Returns:
            -1 if insufficient balance, None if payment successful
        """
        totalcost = prod.TotolCost()
        tax = (totalcost / 100)  # 1% tax
        
        if self.balance >= (totalcost + tax):
            self.balance -= (totalcost + tax)
        else:
            return -1  # Insufficient funds
        

class User(Customer):
    """
    User class that inherits from Customer.
    Demonstrates inheritance (is-a relationship): User IS-A Customer.
    """
    
    def __init__(self, money):
        """
        Initialize user with starting money.
        
        Args:
            money: Initial balance for the user's cart
        """
        super().__init__(money=money)


# Example usage
C1 = User(100000)  # Create user with 100,000 balance
C1.ShowBalance()

# First order: items 2, 4, 1, 2, 6
C1.Order([2, 4, 1, 2, 6])
C1.Pay()
C1.ShowBalance()

# Second order: items 3, 4
C1.Order([3, 4])
C1.Pay()
C1.ShowBalance()
