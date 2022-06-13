class Banker:

    def __init__(self, balance=0, shelved=0):
        self.balance = balance
        self.shelved = shelved
    ###################
    # Shelf method -  Mohammad
    def shelf(self, score):
        # store unbanked points
        self.shelved += score
        return self.shelved
    ###################

    ###################
    # Bank method -  Hamad
    def bank(self):
        self.balance = 0
        self.balance += self.shelved
        self.shelved = 0
        return self.balance
    ###################

    ###################
    # Clear Shelf method - Hamad
    def clear_shelf(self):
        self.shelved = 0
        return self.shelved

    ###################
