class passenger():
    users={}
    flights={
            101: {"seats": 5},
            102: {"seats": 6},
            103: {"seats": 4}
        }
    booking={}

    def main_menu(self):
        while True:
            print("---Flight Reservation System---")
            print("1.passenger")
            print("2.cashier")
            print("3.exit")

            main_option=input("Enter option:")
            
            if main_option == "1":
                print("1.signup")
                print("2.signin")
                sub_option=input("Enter option:")

                if sub_option == "1":
                    self.signup()
                elif sub_option == "2":
                    username = self.signin()

                    if username is None:
                        continue
                    
                    while True:
                        print("---passenger menu---")
                        print("1.check_availability")
                        print("2.book_ticket")
                        print("3.cancel_ticket")
                        print("4.check_status ")
                        print("5.exit")
                    
                        option=input("Enter option:")

                        if option  == "1":
                            self.check_availability()
                        elif option == "2":
                            self.book_ticket(username)
                        elif option == "3":
                            self.cancel_ticket(username)
                        elif option == "4":
                            self.check_status (username)
                        elif option == "5":
                            print("exit passenger menu...")
                            break
                        else:
                            print("Invalid option")
                            
            elif main_option =="2":
                 c=cashier()
                 c.main()

            elif main_option == "3":
                print("exiting main menu...")
                print("thank you")
                break
            else:
                print("invalid option")
            

    def signup(self):      
        username=input("Enter username:")
        if username in self.users:
            print("username already exsits")
        else:
            password=input("Enter password:")
            self.users[username]=password
            print("signup successfully!")   

     
    def signin(self):
        username=input("Enter username:")
        password=input("Enter password:")
        
        if username in self.users and self.users[username]==password:
            print("login successfully!")
            return username
        else:
            print("invalid")
            return None

    def check_availability(self):
        for flight_no in self.flights:
            print("Flight No:", flight_no,
                   "|Available Seats:",
              self.flights[flight_no]["seats"])
            
    def book_ticket(self,username):
        flight_no= int(input("Enter flight number:"))
                       
        if flight_no in self.flights and self.flights[flight_no]["seats"]>0:
            self.booking[username]={
                "flight": flight_no,
                "status":"pending"}
            self.flights[flight_no]["seats"] -=1
            print("ticket booked! waiting for approval.")
        else:
            print("flight seats are not available")
       
    def cancel_ticket(self,username):
        if username in self.booking:
            flight_no=self.booking[username]["flight"]
            self.flights[flight_no]["seats"] +=1
            del self.booking[username]
            print("ticket cancelled successfully!")
        else:
            print("no booking found")

    def check_status (self,username):
        if username in self.booking:
            print("Flight No:", self.booking[username]["flight"])
            print("Status:", self.booking[username]["status"])
        else:
            print("no booking found")
            
class cashier():
    def main(self):
        while True:
            print("---cashier menu---")
            print("1.approve_ticket")
            print("2.cashier_cancel")
            print("3.exit")
                                        
            option=input("Enter option:")
            if option  == "1":
                self.approve_ticket()
            elif option == "2":
                self.cashier_cancel()
            elif option == "3":
                print("exit cashier menu...")
                break
            else:
                print("Invalid option")
                     
    def approve_ticket(self):
        username=input("Enter username:")
        
        if username in passenger.booking:
            passenger.booking[username]["status"]="approved"
            print("ticket approved successfully!")
        else:
            print("booking not found")

    def cashier_cancel(self):
        username=input("Enter username:")
        
        if username in passenger.booking:
            flight_no=passenger.booking[username]["flight"]
            passenger.flights[flight_no]["seats"] +=1
            del passenger.booking[username]
            print("ticket cancelled by cashier")
        else:
            print("booking not found")
    
s=passenger()
s.main_menu()
