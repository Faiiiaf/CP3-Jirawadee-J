class Customer:
    name = ""
    lastname = ""
    age = ""

    def addCart(self):
        print("Add product to",self.name,self.lastname,"'s cart")


customer1 = Customer()
Customer.name = "Hello"
Customer.lastname = "Kitty"
customer1.addCart()

customer2 = Customer()
Customer.name = "Kungfu"
Customer.lastname = "Panda"
customer2.addCart()

customer3 = Customer()
Customer.name = "Flap"
Customer.lastname = "Jack"
customer3.addCart()

customer4 = Customer()
Customer.name = "Kan"
Customer.lastname = "Kluay"
customer4.addCart()