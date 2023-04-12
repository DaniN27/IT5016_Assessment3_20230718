# Create a ticket class
"""
Using attributes
constructor: __init__
initialise values

"""
class ticket:
    x = 5

t1 = ticket()
print(t1.x)

# Simple class, not practical ^
# It is better to execute __init__ function to assign values


class Ticket:
    def __init__(self, staffID, tnumber, name):
        self.staffID = staffID
        self.tnumber = tnumber 
        self.name = name 

ticket1 = Ticket("smith67" "#4501" "John Smith")
ticket2 = Ticket("doe69" "4502" "Jane Doe")



