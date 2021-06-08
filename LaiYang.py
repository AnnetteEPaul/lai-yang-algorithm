import utils

def main():
    print("Welcome to Lai-Yang Algorithm!")

    print("----Getting the Process details for P1----")
    utils.addDetails(1)
    print("----Getting the Event details for P1----")
    utils.eventDetails(1)

    print("----Getting the Process details for P2----")
    utils.addDetails(2)
    print("----Getting the Event details for P2----")
    utils.eventDetails(2)

    print("---Calculating the Global State---")
    utils.calculateGlobalState()

    reset = input("Do you want to reset the values? Enter Y for yes or N for No : ")
    if(reset == 'Y' or reset == 'y'):
        utils.reset()
        restart = input("The values have been reset, Would you like to start again? Please enter Y for Yes or N for No : ")
        if(restart == 'Y' or restart == 'y'):
            main()
    print("Thankyou for using Lai Yang Algorithm")



    
if __name__ == '__main__':
    main()
