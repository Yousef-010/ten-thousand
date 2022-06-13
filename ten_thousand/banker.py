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
    ###################

    ###################
    # Clear Shelf method - Hamad
    ###################
