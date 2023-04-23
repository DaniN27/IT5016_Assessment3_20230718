import re
from time import sleep

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    ITALICS = '\033[1;3m'

class Ticket:
    def __init__(self, number):
        self.number = number
        self.status = 'Open'
        self.responses = []
        self.tickets = []
        self.f_name = ''
        self.email = ''
        self.description = ''

    def add_response(self, response):
        self.responses.append(response)
        self.status = 'Pending'

    def update_status(self, feedback):
        if feedback == 'solved':
            self.status = 'Closed'
        elif feedback == 'ignore':
            self.status = 'Not yet provided'
        else:
            self.status = 'Open'

class ITResponse:
    def __init__(self):
        self.tickets = []

    def generate_number(self):
        ITResponse.counter = getattr(ITResponse, 'counter', 1)
        ticket_number = ITResponse.counter + 2000
        ITResponse.counter += 1
        return ticket_number

    def submit_ticket(self):
        staffID = input("             Enter your Staff ID to begin: ")
        while len(staffID) < 2:
           print("")
           print("             Staff ID must contain minimum", color.CYAN + " 2 characters" + color.END , "or more")
           print("")
           staffID = input("             Enter staff ID containing more than 2 characters: ")
           
        print("")
        f_name = input (str("             Please enter your first name: "))
        print("")
        while not re.match(r'^[A-Za-z -]+$', f_name):
          print("             Please enter a name containing only " + color.RED + "letters" + color.END + "." + color.CYAN + " Numbers" + color.END ,"and", color.BOLD + "most" + color.END, color.CYAN + "special characters" + color.END ,"are not permitted.")
          print("")
          f_name = input (str("             Please enter your first name: "))
          print("")

        while len(f_name)  < 3:
           print("             Please ensure your name has a minimum of", color.CYAN + " 3 characters" + color.END , "or more")
           print("")
           f_name = input (str("             Enter your first name: "))
           print("")

        while True:
          email = input("             Please enter a contact email: ")
          print("")

          if "@" not in email:
             print("             Make sure you enter an", color.CYAN + "@" + color.END, "symbol when typing an email address.")
             print("")

          else:
             break

        while True:
         description = input("             Please let us know the problem you would like help with: ")
    
         def selection_loop():
             new_selection = (input("             Type "+ color.RED + "2" + color.END + " to reset password: "))

             try:
                 new_selection = int(new_selection)

                 if new_selection == 1:
                  print("")
                  print(color.BOLD + "             Please type " + color.RED + "2 " + color.END + color.BOLD + "to change password." + color.END)
                  sleep(2)
                  print_menu()
                  selection_loop()

                 elif new_selection == 2:
                  print("")
                  print("             You have opted to", color.RED + "change password" + color.END + ".")
                  new_password = staffID[:2] + f_name[:3]
                  print("")
                  print("             Your", color.BOLD + "new password" + color.END ,"will be the first", color.CYAN +"2" + color.END ,"letters of your", color.BOLD + "StaffID" + color.END ,"and the first", color.CYAN + "3" + color.END ,"letters of your", color.BOLD + "Name" + color.END +".")
                  sleep(4)
                  print("")
                  print(color.ITALICS + "             Your new password is", color.RED + new_password + color.END , color.ITALICS + "write this down and don't share it with anyone else." + color.END)
                  print("")

                 elif new_selection == 3:
                  print("")
                  print(color.BOLD + "             Please type " + color.RED + "2 " + color.END + color.BOLD + "to change password." + color.END)
                  sleep(2)
                  print_menu()
                  selection_loop()

                 elif new_selection == 4:
                  print("")
                  print(color.BOLD + "             Please type " + color.RED + "2 " + color.END + color.BOLD + "to change password." + color.END)
                  sleep(2)
                  print_menu()
                  selection_loop()

                 else:
                  print("")
                  print("             You have entered an invalid selection, please try again selecting number", color.RED, color.BOLD + "2" + color.END)
                  sleep(2)
                  print_menu()
                  selection_loop()

             except ValueError:
                print("")
                print("             You have entered an invalid selection, please try again selecting number", color.RED, color.BOLD + "2" + color.END)
                sleep(2)
                print_menu()
                selection_loop()

         if "password change" in description.lower():
             print("")
             print(color.RED + "             Need to change password? " + color.END + "Please refer to section " + color.RED + "2" + color.END ,"in the following menu:")
             print("")
             sleep(2)
             print_menu()
             selection_loop()
             sleep(1)
             response = "        New password generated"
             print("")
             break

         if "reset password" in description.lower():
             print("")
             print(color.RED + "             Need to reset password? " + color.END + "Please refer to section " + color.RED + "2" + color.END ,"in the following menu:")
             print("")
             sleep(2)
             print_menu()
             selection_loop()
             sleep(1)
             response = "        New password generated"
             print("")
             break

         if "forgot password" in description.lower():
             print("")
             print(color.RED + "             Forgot password? " + color.END + "Please refer to section " + color.RED + "2" + color.END ,"in the following menu:")
             print("")
             sleep(2)
             print_menu()
             selection_loop()
             sleep(1)
             response = "        New password generated"
             print("")
             break

         else:
           ticket_number = self.generate_number()
           ticket = Ticket(ticket_number)
           ticket.f_name = f_name
           ticket.email = email
           ticket.description = description
           self.tickets.append(ticket)
           print("")
           print("             Thanks", color.BOLD + f_name + color.END, "for your input.\n" "             We will contact you at", color.BOLD + email + color.END, "at our earliest convenience.")
           print("")
           sleep(2)
           print("             Your ticket number is:", "#" + color.CYAN + str(ticket_number) + color.END, "please hold on to this number for future reference.")
           print(" ")
           break
         
        while True:
            feedback = input("             Anything else to add or information that has changed?" + color.ITALICS + " (hint: Type " + color.RED + "'exit'" + color.END + color.ITALICS + " to skip): " + color.END)
            if feedback.lower() == 'exit':
                break
            ticket.add_response(feedback)
            ticket.update_status(feedback)
            print("             Thanks for your feedback!")
            break 
        print("                     ")
        sleep(1)
        self.display_tickets()

    def display_ticket(self, f_name, email, description, staffID):
      if not self.tickets:
        print("             There are no tickets to display.")
      else:
        for ticket in self.tickets:
            if ticket.status == 'Open':
                status_color = color.YELLOW
            elif ticket.status == 'Pending':
                status_color = color.BLUE
            else:
                status_color = color.GREEN

        ticket_number = input("\n             Enter the ticket number you want to view: ")
        found = False
        for ticket in self.tickets:
            if str(ticket.number) == ticket_number:
                found = True
                print("\n             Ticket Number:", "#" + color.CYAN + str(ticket.number) + color.END + ", Status:", status_color + ticket.status + color.END)
                print("")
                print("             Submitted by:", color.BOLD + ticket.f_name+ color.END)
                print("")
                print("             Email address:", color.BOLD + ticket.email + color.END)
                print("")
                print("             Ticket description:")
                for description in ticket.description:
                    print("             - " + description)
                break

        if not found:
            print("             Ticket number not found.")

def print_menu():
    print("")
    print("                             (1.)   Submit a new ticket        ")
    print("")
    print(color.RED + color.BOLD + "                             (2.)   Forgot or Reset password   " + color.END )
    print("")
    print("                             (3.)   View previous tickets      ")
    print("")
    print("                             (4.)   Exit", color.UNDERLINE +  "menu" + color.END)
    print("")

def first_menu():
    print("")
    print(color.BOLD +"             Need help? Choose an option below:" + color.END)
    print("")
    print("                             (1.)   Submit a new ticket        ")
    print("")
    print("                             (2.)   Forgot or Reset password   ")
    print("")
    print("                             (3.)   View previous tickets      ")
    print("")
    print("                             (4.)   Display tickets            ")
    print("")
    print("                             (5.)   Exit", color.UNDERLINE +  "menu" + color.END)
    print("")

first_menu()
while True:
    try:
        selection = int(input("             Enter relevant number here to begin: "))
        if selection == 1:
            print("             You have selected option", color.RED + "submit a new ticket" + color.END + ".")
            print("")
            break

        elif selection == 2:
            print("             You have chosen", color.CYAN + "forgot or reset password" + color.END + ".")
            print("")
            break

        elif selection == 3:
            print("             You have chosen to", color.YELLOW + "view previous tickets" + color.END + ".")
            print("")
            break

        elif selection == 4:
            print("             You have selected to", color.GREEN + "display ticket statistics." + color.END)
            print("")
            break

        elif selection == 5:
            print("             You have selected to", color.BLUE + "exit the menu." + color.END, "Thanks for using our Help desk.")
            print("")
            break

        else:
            sleep(1)
            print("")
            print("             You have entered an invalid selection, please try again selecting a number from", color.PURPLE, color.BOLD + "1 - 4" + color.END)
            print("")

    except ValueError:
        print("             You have entered invalid input, please try again selecting a number from", color.PURPLE, color.BOLD + "1 - 4" + color.END)
        print("")

 
match selection:

   case 1:
       it_response = ITResponse()
       it_response.submit_ticket()

       response = ITResponse()
       response.display_tickets()

         
   case 2:
      print("             To change password please enter the following details: ")
      print("")
      staffID = input("             Enter your Staff ID : ")
      print("")

      while len(staffID) < 2:
           print("             Staff ID must contain minimum", color.CYAN + " 2 characters" + color.END , "or more")
           print("")
           staffID = input("             Enter staff ID containing more than 2 characters: ")
           print("")

      f_name = input (str("             Please enter your first name: "))
      print("")

      while not re.match(r'^[A-Za-z -]+$', f_name):
             print("             Please enter a name containing only " + color.RED + "letters" + color.END + "." + color.CYAN + " Numbers" + color.END ,"and", color.BOLD + "most" + color.END, color.CYAN + "special characters" + color.END ,"are not permitted.")
             print("")
             f_name = input (str("             Please enter your first name: "))
             print("")

      while len(f_name)  < 3:
           print("             Please ensure your name has a minimum of", color.CYAN + " 3 characters" + color.END , "or more")
           print("")
           f_name = input (str("             Enter your first name: "))
           print("")

      new_password = staffID[:2] + f_name[:3]
      print("             Your", color.BOLD + "new password" + color.END ,"will be the first", color.CYAN +"2" + color.END ,"letters of your", color.BOLD + "StaffID" + color.END ,"and the first", color.CYAN + "3" + color.END ,"letters of your", color.BOLD + "Name" + color.END +".")
      sleep(4)
      print("")
      print(color.ITALICS + "             Your new password is", color.RED + new_password + color.END + ".", color.ITALICS + "\n             Write this down and don't share it with anyone else!" + color.END)
      sleep(2)
      print("")
      print("             Thanks", color.BOLD + f_name + color.END, "for using our resolution centre.\n" "             Any questions contact us at", color.BOLD + "help@helpdesk.com" + color.END + ".")
      response = "        New password generated"
      print("")   

     
   case 3:
       it_response = ITResponse()
       it_response.display_tickets()
       


   case 4:
     print("")
