# write a class Train which has methods to book a ticket , get status (no seats) and get fare
# information of the trains running under Indian Railway.

class Train:
    def __init__(self):
        self.seats = 78
        self.fare = 175
    def bookTicket(self):
        self.seats -=1

    def getStatus(self):
        print(self.seats)

    def getFareInfo(self):
        print(self.fare)

obj = Train()
obj.getFareInfo()
print(obj.seats)
obj.bookTicket()
obj.getStatus()
