from abc import ABC, abstractmethod

class PaymentMethod: 
    def __init__(self, custName, amount):
        self.custName = custName
        self.amount = amount

    def getCustName(self):
        return self.custName

    def getAmount(self):
        return self.amount

    def printDetails(self):
        print(f"Customer Name:              {self.custName}")
        print(f"Amount                      {self.amount}")

class CreditCard(PaymentMethod):
    def __init__(self, custName, amount, cardNumber):
        super().__init__(custName, amount)

        self.cardNumber = cardNumber

    def getCardNumber(self):
            return self.cardNumber


class Paypal(PaymentMethod):
    def __init__(self, custName, amount, email):
        super().__init__(custName, amount)

        self.email = email

    def getEmail(self):
        return self.email

# -----------------------------
# Unit Tests
# -----------------------------

# Test 1: PaymentMethod.getCustName()
pm = PaymentMethod("John Lennon", 50)
assert pm.getCustName() == "John Lennon", "Test 1 failed: getCustName()"

# Test 2: PaymentMethod.getAmount()
assert pm.getAmount() == 50, "Test 2 failed: getAmount()"

# Test 3: CreditCard.getCardNumber()
cc = CreditCard("Paul McCartney", 100, "1234-5678-9012-3456")
assert cc.getCardNumber() == "1234-5678-9012-3456", "Test 3 failed: getCardNumber()"

# Test 4: Paypal.getEmail()
pp = Paypal("Ringo Starr", 200, "ringo@example.com")
assert pp.getEmail() == "ringo@example.com", "Test 4 failed: getEmail()"

print("All tests passed!")

def main():
    print("=== Payment Simulation ===")
    
    name = input("Enter customer name: ")
    amount = float(input("Enter amount: "))
    
    payment_type = input("Payment method (CreditCard/Paypal)? ").strip().lower()
    
    if payment_type == "creditcard":
        card = input("Enter card number: ")
        cc = CreditCard(name, amount, card)
        cc.printDetails()
        print(f"Card Number: {cc.getCardNumber()}")
        
    elif payment_type == "paypal":
        email = input("Enter PayPal email: ")
        pp = Paypal(name, amount, email)
        pp.printDetails()
        print(f"Email: {pp.getEmail()}")
        
    else:
        print("Invalid payment type")

# Standard Python idiom to run main
if __name__ == "__main__":
    main()

