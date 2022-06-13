class Banker:
    pass
    ###################
    # Shelf method -  Mohammad
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
