class CoffeMachine:

    def __init__(self):
        self.water_amount = 400
        self.milk_amount = 540
        self.coffe_amount = 120
        self.cups_amount = 9
        self.money_amount = 550

    def corent_state(self):
        print(f"""The coffee machine has:
        {self.water_amount} of water
        {self.milk_amount} of milk
        {self.coffe_amount} of coffee beans
        {self.cups_amount} of disposable cups
        {self.money_amount} of money""")

    def fill(self):
        self.water_amount += int(input("Write how many ml of water do you want to add:"))
        self.milk_amount += int(input("Write how many ml of milk do you want to add:"))
        self.coffe_amount += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups_amount += int(input("Write how many disposable cups of coffee do you want to add:"))

    def order(self, coffe):
        if coffe == "1":
            self.water_amount -= 250
            self.coffe_amount -= 16
            self.money_amount += 4
            self.cups_amount -= 1
        elif coffe == "2":
            self.water_amount -= 350
            self.milk_amount -= 75
            self.coffe_amount -= 20
            self.cups_amount -= 1
            self.money_amount += 7
        else:
            self.water_amount -= 200
            self.milk_amount -= 100
            self.coffe_amount -= 12
            self.cups_amount -= 1
            self.money_amount += 6
    def check_inventory(self, x):
        if self.cups_amount < 1:
            print("Sorry, not enough cups")
        elif x == "1":
            if self.water_amount < 250:
                print("Sorry, not enough water!")
            elif self.coffe_amount < 16:
                print("Sorry, not enough coffe!")
            else:
                print("I have enough resources, making you a coffee!")
                self.order("1")
        elif x == "2":
            if self.water_amount < 350:
                print("Sorry, not enough water!")
            elif self.milk_amount < 75:
                print("Sorry, not enough milk!")
            elif self.coffe_amount < 20:
                print("Sorry, not enough coffe!")
            else:
                print("I have enough resources, making you a coffee!")
                self.order("2")
        else:
            if self.water_amount < 200:
                print("Sorry, not enough water!")
            elif self.milk_amount < 100:
                print("Sorry, not enough milk!")
            elif self.coffe_amount < 12:
                print("Sorry, not enough coffe!")
            else:
                print("I have enough resources, making you a coffee!")
                self.order("3")

    def run(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):")
            if action == "exit":
                break
            elif action == "buy":
                user_coffe = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back")
                if user_coffe == "back":
                    continue
                self.check_inventory(user_coffe)
            elif action == "fill":
                self.fill()
            elif action == "remaining":
                self.corent_state()
            else:
                print("I gave you", self.money_amount)
                self.money_amount = 0
coffe = CoffeMachine()
coffe.run()