print("***********************************************");
print("WELCOME TO NOKIA 3310-THE HARDEST IN THE WORLD")
print("***********************************************")
print("********************")
print("MAIN MENU")
print("********************")
print("1: PHONE BOOK")
print("2: MESSAGES")
print("3: CHAT")
print("4: CALL REGISTER")
print("5: TONES")
print("6: SETTINGS")
print("7: CALL DIVERT")
print("8: GAMES")
print("9: CALCULATOR")
print("10: REMINDERS")
print("11: CLOCK")
print("12: PROFILES")
print("13: SIM SERVICES")
print("*********************")
print("*********************")
options = int(input("ENTER"))
match (options) :
    case 1 :
        print("*********************");
        print("PHONE BOOK")
        print("*********************");
        print("1: Search")
        print("2: Service Nos")
        print("3: Add name")
        print("4: Erase")
        print("5: Edit")
        print("6: Assign tone")
        print("7: Send b'card")
        print("8: Options")
        print("9: Speed dials")
        print("10: Voice tags")
        phone = (int(input("Select option 1 to 10: ")))
        match (phone) :
            case 1 :
                print("> Search")
            case 2 :
                print("> Service Nos")
            case 3 :
                print("> Add name")
            case 4 :
                print("> Erase")
            case 5 :
                print("> Edit")
            case 6 :
                print("> Assign tone")
            case 7 :
                print("> Send b'card")
            case 8 :
                print("= Options =")  
                print("1: Type of view")  
                print("2: Memory status")    
                option_eight = (int(input("Choose option 1 or 2: ")))
                match (option_eight) :
                    case 1:
                        print("> Type of view")
                    case 2:
                        print("> Memory status")

            case 9 :
                print("> Speed dails")
            case 10 :
                print("> Voice tags")
            case _ :
                print("> Invalid input try again")    
    case 2 :    
         print("*********************")
         print("MESSAGES")
         print("*********************")
         print("1: Write messages")
         print("2: Inbox")
         print("3: Outbox")
         print("4: Picture messages")
         print("5: Template")
         print("6: Smileys")
         print("7: Message Settings")
         print("8: Info service")
         print("9: Voice mailbox number")
         print("10: Service command editor")

         message = (int(input("Select option 1 to 10: ")))
         match (message) :
            case 1 :
                print("> Write messages")
            case 2 :
                print("> Inbox")
            case 3 :
                print("> Outbox")
            case 4 :
                print("> Picture messages")
            case 5 :
                print("> Template")
            case 6 :
                print("> Smileys")
            case 7 :
                
                print("Messages Settings")
                print("1: Set")  
                print("2: Common")    
                option_seven = (int(input("Choose option 1 or 2: ")))
                match (option_seven) :
                    case 1:
                        print("> Set <")
                        print("1: Message centre number")  
                        print("2: Messages sent as") 
                        print("3: Message validity")
                        seven = (int(input("Choose option 1 or 2: ")))
                        match (seven) : 
                            case 1 :
                                print("> Message centre number")  
                            case 2 :
                                print("> Messages sent as") 
                            case 3 :
                                print("> Message validity")     
                            case _ :
                                print("Invalid input try again")                   
                    case 2:
                        print("> Common <")
                        print("1: Delivery reports")  
                        print("2: Reply via same centre") 
                        print("3: Character support")
                        common = (int(input("Choose option 1 or 2: ")))
                        match (common) :
                            case 1 :
                                print("> Delivery reports")  
                            case 2 :
                                print("> Reply via same centre") 
                            case 3 :
                                print("> Character support")
                            case _ :
                                print("Invalid input try again") 

            case 8 :
                print("> Info services")  
            case 9 :
                print("> Voice mailbox number")
            case 10 :
                print("> Service command editor")
            case _ :
                print("> Invalid input try again")                                 
    case 3 :
        print("*********************")
        print('CHAT')
        print("*********************")
    case 4:                 
        print('CALL REGISTER')
        print("1: Missed calls")
        print("2: Recieve calls")
        print("3: Dialled numbers")
        print("4: Erase recent call lists")
        print("5: Show call duration")
        print("6: Show call costs")
        print("7: Call cost Settings")
        print("8: Prepaid credit")
        call_register = int(input("> Select option 1 to 8: "))
        match(call_register) :
            case 1 :
                print("> Missed calls")
            case 2 :
                print("> Recieve calls")
            case 3 :
                print("> Dailed numbers")
            case 4 :
                print("> Erase recent call lists")
            case 5 :
                print("*********************")
                print("Show call duration")
                print("*********************")
                print("1: Last call duration")
                print("2: All calls duration")
                print("3: Recieved calls duration")
                print("4: Dialled calls duration")
                print("5: Clear timers")
                duration = int(input("Choose from 1 to 5: "))
                match (duration) :
                    case 1 :
                        print("> Last call duration")
                    case 2 :
                        print("> All calls duration")
                    case 3 :
                        print("> Recieved calls duration")
                    case 4 :
                        print("> Dialled calls duration")
                    case 5 :
                        print("> Clear timers")
                    case _ :
                        print("> Invalid input try again")   

            case 6 :
                print("*********************")
                print("Call cost settings")
                print("*********************")
                print("1: Last call cost")
                print("2: All calls' cost")
                print("3: Clear counters")
                call_cost = int(input("Choose from 1 to 3: "))
                match (call_cost) :
                    case 1 :
                        print("> Last call cost")
                    case 2 :
                        print("> All calls' cost")
                    case 3 :
                        print("> Clear counters")
                    case _ :
                        print("> Invalid input try again")   
            case 7 :
                print("*********************")
                print("Send b'card")
                print("*********************")
                print("1: Call cost limit")
                print("2: Show cost in")
                send = int(input("Choose from 1 to 3: "))
                match (send) :
                    case 1 :
                        print("> Call cost limit")
                    case 2 :
                        print("> Show cost in")
                    case _ :
                        print("> Invalid input try again")
            case 8 :
                print("> Prepaid credi")  
            case _ :
                print("> Invalid input try again")    
    case 5:
        print("*********************") 
        print('TONES')
        print("*********************") 
        print("1: Ringing tone")
        print("2: Ringing volume")
        print("3: Incoming call alert")
        print("4: Composer")
        print("5: Message alert tone")
        print("6: Keypad tones")
        print("7: Warning and game tones")
        print("8: Vibrating alert")
        print("9. Screen saver")
        tone = int(input("Select from 1 to 9: "))
        match (tone) :
            case 1 :
                print("> RInging tone")
            case 2 :
                print("> Ringing volume")
            case 3 :
                print("> Incoming call alert")
            case 4 :
                print("> Composer")
            case 5 :
                print("> Message alert tone")
            case 6 :
                print("> Keypad tones")
            case 7 :
                print("> Warning and games tones")
            case 8 :
                print("> Vibrating alert")  
            case 9 :
                print("> Screen saver")  
            case _ :
                print("> Invalid input try again")    
    case 6:
        print("*********************")
        print('SETTINGS')
        print("*********************")
        print('1: Call settings')
        print('2: Phone settings')
        print('3: Security settings')
        print('4: Restore factory settings')
        set = int(input('Enter option: '))
        match(set):
            case 1 :
                print('> Call settings <')
                print('1: Automatic redail')
                print('2: Speed dialling')
                print('3: Call waiting options')
                print('4: Own number sending')
                print('5: Phone line in use')
                print('6: Automatic answer')
                call_setting = int(input('Select options: '))
                match(call_setting):
                    case 1 :
                        print('> Automatic redail')
                    case 2 :
                        print('> Speed dialling')
                    case 3 :
                        print('> Call waiting options')
                    case 4 :
                        print('> Own number sending')
                    case 5 :
                        print('> Phone line in use')
                    case 6 :
                        print('> Automatic answer')
                    case _:
                        print('> Invalid input try again')
            case 2 :
                print('> Phone settings <')
                print('1: Language')
                print('2: Cell info display')
                print('3: Welcome note')
                print('4: Network selection')
                print('5: Lights')
                print('6: Confirm SIM service actions')
                phone_set = int(input('Enter option: '))
                match(phone_set):
                    case 1 :
                        print('> Language')
                    case 2 :
                        print('> Cell info display')
                    case 3 :
                        print('> Welcome note')
                    case 4 :
                        print('> Network selection')
                    case 5 :
                        print('> Lights')
                    case 6 :
                        print('> Confirm SIM service actions')
                    case _:
                        print('> Invalid input')

            case 3 :
                print('> Security settings <')
                print('1: PIN code request')
                print('2: Call baring service')
                print('3: Fixed dialling')
                print('4: Closed user group')
                print('5: Phone security')
                print('6: Change access codes')
                secure = int(input('Select option: '))
                match(secure):
                    case 1 :
                        print('> PIN code request')
                    case 2 :
                        print('> Call baring service')
                    case 3 :
                        print('> Fixed dialling')
                    case 4 :
                        print('> Closed user group')
                    case 5 :
                        print('> Phone security')
                    case 6 : 
                        print('> Change access codes')
                    case _:
                        print('> Invalid input try again')
            case 4 :
                print('> Restore factory settings')

    case 7 :
        print("*********************")
        print('PHONE SETTINGS')
        print("*********************")
    case 8 :
        print("*********************")
        print('GAMES')
        print("*********************")
    case 9 :
        print("*********************")
        print('CALCULATOR ')
        print("*********************")
    case 10 :
        print("*********************")
        print('REMINDERS')
        print("*********************")
    case 11 :
        print("*********************")
        print('CLOCK')
        print("*********************")
        print('1: Alarm clock')
        print('2: Clock settings')
        print('3: Date setting')
        print('4: Stopwatch')
        print('5: Countdown timer')
        print('6: Auto update of date and time')
        clock = int(input('Enter option: '))
        match(clock):
            case 1 :
                print('> Alarm clock')
            case 2 :
                print('> Clock settings')
            case 3 :
                print('> Date setting')
            case 4 :
                print('> Stopwatch')
            case 5 :
                print('> Countdown timer')
            case 6 :
                print('> Auto update of date and time')
            case _:
                print('> Invalid input try again')

    case 12 :
        print("*********************")
        print('PROFILES')
        print("*********************")
    case 13 :
        print("*********************")
        print('SIM SERVICES')
        print("*********************")
    case _ :
        print("*********************")
        print("Invalid input try again")
        print("*********************")
