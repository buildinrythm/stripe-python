from abc import ABC, abstractmethod

# -----------------------------
# Abstract Base Class
# -----------------------------
class PaymentMethod(ABC):
    def __init__(self, custName, amount):
        self.custName = custName
        self.amount = amount

    def getCustName(self):
        return self.custName

    def getAmount(self):
        return self.amount

    @abstractmethod
    def printDetails(self):
        # Provide shared behavior: name and amount
        print("=== Summary ===")
        print(f"Customer: {self.custName}")
        print(f"Amount:   {self.amount}")

# -----------------------------
# Subclasses
# -----------------------------
class CreditCard(PaymentMethod):
    def __init__(self, custName, amount, cardNumber):
        super().__init__(custName, amount)
        self.cardNumber = cardNumber

    def getCardNumber(self):
        return self.cardNumber

    def printDetails(self):
        super().printDetails() 
        print(f"Card:     {self.cardNumber}")
        print("=" * 20)

class Paypal(PaymentMethod):
    def __init__(self, custName, amount, email):
        super().__init__(custName, amount)
        self.email = email

    def getEmail(self):
        return self.email

    def printDetails(self):
        super().printDetails()  
        print(f"Email:    {self.email}")
        print("=" * 20)

# -----------------------------
# Unit Tests
# -----------------------------

# Test CreditCard
cc = CreditCard("Paul McCartney", 100, "1234-5678-9012-3456")
assert cc.getCustName() == "Paul McCartney", "CreditCard getCustName failed"
assert cc.getAmount() == 100, "CreditCard getAmount failed"
assert cc.getCardNumber() == "1234-5678-9012-3456", "CreditCard getCardNumber failed"

# Test Paypal
pp = Paypal("Ringo Starr", 200, "ringo@example.com")
assert pp.getCustName() == "Ringo Starr", "Paypal getCustName failed"
assert pp.getAmount() == 200, "Paypal getAmount failed"
assert pp.getEmail() == "ringo@example.com", "Paypal getEmail failed"

print("All tests passed!")

# -----------------------------
# Optional Simulation
# -----------------------------
def main():
    print("=== Payment Simulation ===")
    
    name = input("Enter customer name: ")
    amount = float(input("Enter amount: "))
    
    payment_type = input("Payment method (C/P)? ").strip().lower()
    
    if payment_type == "c":
        card = input("Enter card number: ")
        cc = CreditCard(name, amount, card)
        cc.printDetails()
        
    elif payment_type == "p":
        email = input("Enter PayPal email: ")
        pp = Paypal(name, amount, email)
        pp.printDetails()
        
    else:
        print("Invalid payment type")

if __name__ == "__main__":
    main()
