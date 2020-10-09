# Start Your Code here

class Garage():
    '''
        - tickets -> list
        - parkingSpaces -> list
        - currentTicket -> dictionary
    '''
    def __init__(self,tickets,parkingSpaces,currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket   
        
    def takeTicket(self):
        self.currentTicket[self.tickets[0]] = ''
        del self.tickets[0]
        del self.parkingSpaces[0]
        print(self.parkingSpaces)
        print(self.tickets)
        print(self.currentTicket)
        
    def payForParking(self):
        paid = int(input("What's your ticket number?  "))
        self.currentTicket[paid] = 'paid' 
        print('Your ticket has been paid and you have 15 mins to leave!')
        print(self.currentTicket)
        
    def leaveGarage(self):
        answer = int(input("What's your ticket number?  "))
        if self.currentTicket[answer] != 'paid':
            print('Pay Ticket!!')
        elif self.currentTicket[answer] == 'paid':
            print('Thank you, have a nice day!')
        del self.currentTicket[answer]
        self.tickets.append(answer)
        self.parkingSpaces.append(answer)
            
parkingGarage = Garage([1,2,3,4,5],[1,2,3,4,5],{})      
def run():
    while True:
        response = input('What do you want to do take/pay ticket or leave?')
        
        if response.lower() == 'take':
            parkingGarage.takeTicket()
        if response.lower() == 'pay':            
            parkingGarage.payForParking()
        if response.lower() == 'leave':
            parkingGarage.leaveGarage()
run()

# We pretty much collaborated on the whole project the entire time
# Monica set up the leaveGarage method
# Denise  set up all the responses for run method as well as the payForParking method
# Angelica set up the takeTicket method and input logic for leaveGarage method