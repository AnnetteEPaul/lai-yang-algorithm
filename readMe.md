# Lai-Yang's Algorithm

## Introduction
 The Algorithm is written to calculate the global state for a given 2 proccesses. The Algorithm takes as input the values of the proccesses at each timestamp along with the details regarding the sent events, receive events and snapshot taking events of the processes.

## Steps
 - The Algorithm first takes the value of process P1 at each timestamp along with initialising the process P1 as a white process. 
 - The Algorithm then takes the details of send event, receive event or snapshot taking event  of process P1.
     - If it's a send or receive event, the Algorithm takes the message value as the input along with the colour of the message sent. 
     - If its a snapshot taking event, the Algorithm takes the value of the timestamps between which then snapshot is taken. 
        - If a snapshot is taken the process P1 becomes RED. 
 - The above steps are repeated for process P2. 
 - The Algorithm then segegrates the required white  sent/received messages for the channel states along with the value of the processes while the 
    snapshots was taken using which the values of P1, P2, Channel12, Channel21 are calculated. 
 - Using the above calculated values the global state is calculated. 
 - The Algorithm also provides us with the provision to reset the values and restart if needed. 


 ## Working with the script
  - The script can be run from any platform like any other normal py file.
     -  It can be run from the command prompt of the directory using ` py LaiYang.py ` or `python LaiYang.py` or `python3 LaiYang.py` command. 


 ## Sample execution for Reference
 ```
    Welcome to Lai-Yang Algorithm!
    ----Getting the Process details for P1----
    Enter the number of timeslots : 4
    Enter the value of the processor P1 at timestamp t1: 500
    Enter the value of the processor P1 at timestamp t2: 480
    Enter the value of the processor P1 at timestamp t3: 510
    Enter the value of the processor P1 at timestamp t4: 510

    ----Getting the Event details for P1----
    Please enter the events in the order of occurence
    Is it a snapshot message? Please Enter Y for Yes or N for No : n
    Is it a WHITE or RED msg? Please Enter W for White or R for Red : w
    Is it a send or receive msg? Please Enter S for Send or R for Receive : s
    Enter the message value : 20
    Do you want to continue[Y/N]?

    Is it a snapshot message? Please Enter Y for Yes or N for No : y
    Enter the first value of the timeslot between which the message is sent : t2
    Enter the second value of the timeslot between which the message is sent : t3
    Do you want to continue[Y/N]?

    Is it a snapshot message? Please Enter Y for Yes or N for No : n
    Is it a WHITE or RED msg? Please Enter W for White or R for Red : w
    Is it a send or receive msg? Please Enter S for Send or R for Receive : r
    Enter the message value : 30
    Do you want to continue[Y/N]?n

    ----Getting the Process details for P2----
    Enter the number of timeslots : 4
    Enter the value of the processor P2 at timestamp t1: 500
    Enter the value of the processor P2 at timestamp t2: 500
    Enter the value of the processor P2 at timestamp t3: 490
    Enter the value of the processor P2 at timestamp t4: 490

    ----Getting the Event details for P2----
    Please enter the events in the order of occurence
    Is it a snapshot message? Please Enter Y for Yes or N for No : n
    Is it a WHITE or RED msg? Please Enter W for White or R for Red : w
    Is it a send or receive msg? Please Enter S for Send or R for Receive : s
    Enter the message value : 30
    Do you want to continue[Y/N]?

    Is it a snapshot message? Please Enter Y for Yes or N for No : n
    Is it a WHITE or RED msg? Please Enter W for White or R for Red : w
    Is it a send or receive msg? Please Enter S for Send or R for Receive : r
    Enter the message value : 20
    Do you want to continue[Y/N]?

    Is it a snapshot message? Please Enter Y for Yes or N for No : y
    Enter the first value of the timeslot between which the message is sent : t3
    Enter the second value of the timeslot between which the message is sent : t4
    Do you want to continue[Y/N]?n

    ---Calculating the Global State---
    Evaluating.............
    Value of P1 = 480
    Value of Channel 1-2 : 20 - 20 = 0
    Value of P2 = 490
    Value of Channel 2-1 : 30
    Global State = 1000
    Do you want to reset the values? Enter Y for yes or N for No : y
    The values have been reset, Would you like to start again? Please enter Y for Yes or N for No : n
    Thankyou for using Lai Yang Algorithm
```

# Assumptions 
 - Snapshot has been recorded atleast once by the processes. 

# NOTE
 - For the YES/NO inputs, default value is YES hence we can simply press enter in case of YES.
 - Inputs for all other types of inputs should be specified for seemless working of the algorithm.
 - The inputs for the questions can be typed in both uppercase or lowercase. 



