try :
        main_input=int(input("""
1.Shift Booking
2.Go Online
3.Earnings
4.Help
5.Exit
Enter the Number (1-4) : """))
        
        if main_input==1 :
            SM.sleep(0.5)
            shift_booking()

        elif main_input==2:
            SM.sleep(0.5)
            go_online()

        elif main_input==3:
            SM.sleep(0.5)
            earnings()

        elif main_input==4:
            SM.sleep(0.5)
            help()

        elif main_input==5:
            print("Thank You For Using\n\n")
            print("Close the terminal to close.")
            
        else:
            print ("Soming Thing Went Wrong Please Try Again.")
            SM.sleep(1)
            main()

    except ValueError:
        print("You Entered Invalid Input, Please Try Again. ")
        SM.sleep(1)
        main()





elif earnings_input==2:
            earnings_increase=0
            for j in range (order_page.order_earnings):
                print(order_page.order_detail_earnings[earnings_increase])
                earnings_increase+=1
            print("\nYour Total Earnings =",sum(order_page.order_detail_earnings))
            SM.loading(5)
            main()
        