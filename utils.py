import logging


global processes, timestamp_values_P1, timestamp_values_P2, send_events_P1, send_events_P2, receive_events_P1, receive_events_P2, snapshot_messages
processes, timestamp_values_P1, timestamp_values_P2, send_events_P1, send_events_P2, receive_events_P1, receive_events_P2, snapshot_messages, events_P1, events_P2 = [], {}, {}, [], [], [], [], {}, [], []
def addDetails(process_number):
    global processes, timestamp_values_P1, timestamp_values_P2
    process = {}
    process['name'] = 'P'+str(process_number)
    process['type'] = 'WHITE'
    processes.append(process)
    timeslots =  int(input("Enter the number of timeslots : ")) 

    if(process_number == 1):
        for timeslot in range(1,timeslots+1):
            try:
                timestamp_values_P1['t'+str(timeslot)] = int(input("Enter the value of the processor P1 at timestamp t"+str(timeslot)+": "))
            except Exception as e:
                logging.info('Error while trying to add Details of processor ' + str(process_number))
    if(process_number == 2):
        for timeslot in range(1,timeslots+1):
            try:
                timestamp_values_P2['t'+str(timeslot)] = int(input("Enter the value of the processor P2 at timestamp t"+str(timeslot)+": "))
            except Exception as e:
                logging.info('Error while trying to add Details of processor ' + str(process_number))


def eventDetails(process_number):
    global events_P1, events_P2, processes
    print("Please enter the events in the order of occurence")
    continue_loop=True
    while(continue_loop):
        single_dict={}
        snapshot_msg = input("Is it a snapshot message? Please Enter Y for Yes or N for No : ")
        if(snapshot_msg == 'Y' or snapshot_msg == 'y'):
            first_timeslot_value = input("Enter the first value of the timeslot between which the message is sent : ")
            second_timeslot_value = input("Enter the second value of the timeslot between which the message is sent : ")
            single_dict['first timeslot']=first_timeslot_value
            single_dict['second timeslot']=second_timeslot_value
            single_dict['msg type'] = 'SNAPSHOT'
            for i in processes:
             if i['name'] == 'P'+str(process_number):
                i['type'] == 'RED'
        else:
            msg_colour = input("Is it a WHITE or RED msg? Please Enter W for White or R for Red : ")
            msg_type = input("Is it a send or receive msg? Please Enter S for Send or R for Receive : ")
            message_value = int(input("Enter the message value : "))

            if(msg_colour == 'W' or msg_colour == 'w'):
                single_dict['msg colour'] = "WHITE"
            elif(msg_colour == 'R' or msg_colour == 'r'):
                single_dict['msg colour'] = "RED"

            single_dict['message value']=message_value
            if(msg_type == 'S' or msg_type == 's'):
                single_dict['msg type'] = "SEND"
            elif(msg_type == 'R' or msg_type == 'r'):
                single_dict['msg type'] = "RECEIVE"

        if(process_number == 1):
            events_P1.append(single_dict)
        else:
           events_P2.append(single_dict)

        to_continue = input("Do you want to continue[Y/N]?")
        if(to_continue=='N' or to_continue == 'n'):
            continue_loop=False
    

def segregateDetails():
    global events_P1, events_P2, send_events_P1, send_events_P2, receive_events_P1, receive_events_P2, snapshot_messages
    for event in events_P1:
        if(event['msg type'] != 'SNAPSHOT'):
            if(event['msg colour'] == 'WHITE'):
                if(event['msg type'] == "SEND"):
                    send_events_P1.append(event)
                elif(event['msg type'] == "RECEIVE"):
                    receive_events_P1.append(event)
        else:
            snapshot_messages['P1'] = event
            break
    for event in events_P2:
        if(event['msg type'] != 'SNAPSHOT'):
            if(event['msg colour'] == 'WHITE'):
                if(event['msg type'] == "SEND"):
                    send_events_P2.append(event)
                elif(event['msg type'] == "RECEIVE"):
                    receive_events_P2.append(event)
        else:
            snapshot_messages['P2'] = event
            break

def calculateGlobalState():
    global send_events_P1, send_events_P2, receive_events_P1, receive_events_P2, red_messages, timestamp_values_P1, timestamp_values_P2
    global sent_white_msg_P1, received_white_msg_P1, sent_white_msg_P2, received_white_msg_P2, value_P1, value_P2, channel_12_value, channel_21_value,global_state

    sent_white_msg_P1, received_white_msg_P1, sent_white_msg_P2, received_white_msg_P2, value_P1, value_P2, channel_12_value, channel_21_value,global_state = 0, 0, 0, 0, 0, 0, 0, 0, 0
    
    segregateDetails()

    for send_event in send_events_P1:
        sent_white_msg_P1 = sent_white_msg_P1 + send_event['message value']
    for send_event in send_events_P2:
        sent_white_msg_P2 = sent_white_msg_P2 + send_event['message value']
    for receive_event in receive_events_P1:
        received_white_msg_P1 = received_white_msg_P1 + receive_event['message value']
    for receive_event in receive_events_P2:
        received_white_msg_P2 = received_white_msg_P2 + receive_event['message value']
    
    print("Evaluating.............")
    try:
        value_P1 = int(timestamp_values_P1[snapshot_messages['P1']['first timeslot']])
    except Exception as e:
        print("Errorr! process P1 has not recorded the snapshot")
    try:
        value_P2 = int(timestamp_values_P2[snapshot_messages['P2']['first timeslot']])
    except Exception as e:
        print("Errorr! process P2 has not recorded the snapshot")
  
    channel_12_value=sent_white_msg_P1-received_white_msg_P2
    channel_21_value=sent_white_msg_P2-received_white_msg_P1

    global_state = value_P1 + value_P2 + channel_12_value + channel_21_value


    print("Value of P1 = " + str(value_P1))
    print("Value of Channel 1-2 : " + str(sent_white_msg_P1) + " - " + str(received_white_msg_P2) + " = " + str(channel_12_value))
    print("Value of P2 = " + str(value_P2))
    print("Value of Channel 2-1 : " + str(sent_white_msg_P2) + " - " + str(received_white_msg_P1)  + " =  " + str(channel_21_value))
    print("Global State = " + str(global_state))

    
def reset():
    try:
        global processes, timestamp_values_P1, timestamp_values_P2, send_events_P1, send_events_P2, receive_events_P1, receive_events_P2, snapshot_messages
        global sent_white_msg_P1, received_white_msg_P1, sent_white_msg_P2, received_white_msg_P2, value_P1, value_P2, channel_12_value, channel_21_value,global_state
        processes, timestamp_values_P1, timestamp_values_P2, send_events_P1, send_events_P2, receive_events_P1, receive_events_P2, snapshot_messages, events_P1, events_P2 = [], {}, {}, [], [], [], [], {}, [], [] 
        sent_white_msg_P1, received_white_msg_P1, sent_white_msg_P2, received_white_msg_P2, value_P1, value_P2, channel_12_value, channel_21_value,global_state = 0, 0, 0, 0, 0, 0, 0, 0, 0
    except Exception as e:
        print("Error while trying to reset the values")

    


    






