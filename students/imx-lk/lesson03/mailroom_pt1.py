#!/usr/bin/env python3
#The original list of donors will sit outside the main function because if it stays inside the fucntion it will replace the names appended in thankyou_new_donor
donor_list = [['Damien Leake', 1000, 3000, 500], ['Andrew Foreman', 375, 2900], ['David Altman', 20, 30000, 54678.50], ['Alex Haldin', 1.75, 123678,],['Osito Castaneda', 123456.75, 34567.12, 35]]

#I orinally had a def main function to
# def main ():

#     #Prompting User for his options
#     responses_available = ['1','2','q','Q']
#     response = input('Hello, What would you like to do: Send a Thank You (1), Create a Report(2) or quit(q): ')
#     while response not in responses_available:
#         response = input('No, enter one of the following: Send a Thank You (1), Create a Report(2) or quit(q): ')

#     #Call the function according to which option in the menu they picked
#     if response == '1':
#         thankyou_note(donor_list)
#     elif response == '2':
#         create_report(donor_list)
#     else:
#         print('\nGoodbye thank you for using the mailroom!')


def thankyou_note(donor_list):
    #new list where donor data picked will be saved
    new_donor_list = []
    #If the user types "list" show them a list of donors, if the user types a name add that name to the data structure and use it.
    response_thankyou = input('\nEnter the first and last name of a new donor or type "list" to view our current list of donors: ')
    if response_thankyou == 'list':
        new_donor_list = thankyou_list(donor_list)
    else:
        new_donor_list = thankyou_new_donor(response_thankyou,donor_list)

        #since were only saving 2 items on the new_donor_list list then we can index  both of those itemsm
    print('--------------------------------------')
    print(f'\nThank you {new_donor_list[0]:s} for your donation of ${new_donor_list[1]:,.2f} we really appreciate your contribution!')
    print('--------------------------------------')
    print(end= '\n')


def thankyou_list(donor_list):
    #New list to save picked donor information
    new_donor_list= []

    #Prints an enumerated list of names so we later on we can select by number
    for i, name in enumerate(donor_list):
    #took the lenght to use for the while loop to ensure the input falls within the number in the list, added one since range starts at 0
        donorlength = len(donor_list)+1
        print(f'{i+1} : {name[0]}')

    #Created a range of the lenght to ensure numbers fall within
    donorlenght_int = range(donorlength)
    #Asks which name by number
    response_pickname = int(input("Who should the thank you letter be for, select by number: "))
    while response_pickname not in donorlenght_int:
        response_pickname = int(input("That number is not on th list, Who should the thank you letter be for, select by number: "))
    #Remove 1 from the index since we added 1 on the for loop previously so the first number wouldnt be zero
    name_index = response_pickname - 1
    #donor_picked saves the information of the donor that was picked accorind to index
    donor_picked = donor_list[name_index]

       #Added the name of the donor picked to the new list
    new_donor_list.append(donor_picked[0])

    #print donor information accorind to the list : print(donor_list[name_index]) or
    #This find the lenght of the donor that was chosen so we can use it to create the number of  {} for formatting
    length_donors = len(donor_list[name_index])

    #remove one because we don't want to include the name index only the donations
    donations = '${:,.2f}   '*(length_donors-1)
    donors_info = '\nThe name of the donor is : {:}, and the donations are ' + donations
    #Displays the data for that specific donor:
    print(donors_info.format(*donor_picked))
    #Ask which donation amount they want to use
    response_donation = int(input("Choose a donation amount(Ex: if $1,000.00 enter 1000): "))
    #Check if donation is in list if not re-ask
    while response_donation not in donor_picked[1:]:
        response_donation = int(input("NOT FOUND! Choose a donation amount(Ex: if $1,000.00 enter 1000): "))

    #Add amount to new list
    new_donor_list.append(response_donation)

    return new_donor_list

def thankyou_new_donor(response_thankyou,donor_list):
    #Create a new list to save new information
    new_donor_list = []
    #Format the string to make sure its capitalized properly and append it to the new list
    new_name=response_thankyou.title()
    new_donor_list.append(new_name)

    #Get the donation amount and append it to the new_donor_list
    response_donation = int(input("\nEnter a donation amount(Ex: if $1,000 enter 1000): "))
    new_donor_list.append(response_donation)

    #append to donor_list so it can be added to the master list
    donor_list.append(new_donor_list)

    return new_donor_list


def create_report(donor_list):
#this list will capture the total, average, and number of gifts
    list_total_avg = []

#This for loop grabs the first list within donor_list
    for donor_entry in donor_list:
        #Need to clear out the total and average everytime or it adds up donations continuesly
        total_donations= 0
        average_donations = 0
        #this temp list is to append my current items and then append it to a master list so I can create a list within a list
        temporary_list = []
        #get length to conpute the average and number of gifts
        length_entry = (len(donor_entry)-1)
        #accesing the first list  within donor_list I sliced and started at index 1. because I want to only access the donations amount

        #sum all the donations
        for donation in donor_entry[1:]:
            total_donations +=donation

        #calculate the average
        average_donations = total_donations/length_entry
        #append all the items to a temporary list
        temporary_list.append(donor_entry[0])
        temporary_list.append(total_donations)
        temporary_list.append(length_entry)
        temporary_list.append(average_donations)

        #append the temporarly list to the master list to create a list within a list
        list_total_avg.append(temporary_list)

    print(end = '\n\n')
    print('{:<20} {:^50} {:^5} {:>25}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('---------------------------------------------------------------------------------------------------------')
    #for name in list_total_avg:
        #print('{:<10} {:^45f} {:^5} {:>30f}'.format(*name))
    for x in list_total_avg:
        task=f'{x[0]:<20} {x[1]:^50.2f} {x[2]:} {x[3]:>30.2f}'
        print(task)


if __name__ == '__main__':
    while True:
        responses_available = ['1','2','q','Q']
        response = input('Hello, What would you like to do: Send a Thank You (1), Create a Report(2) or quit(q): ')
        while response not in responses_available:
            response = input('No, enter one of the following: Send a Thank You (1), Create a Report(2) or quit(q): ')

        #Call the function according to which option in the menu they picked
        if response == '1':
            thankyou_note(donor_list)
        elif response == '2':
            create_report(donor_list)
        else:
            print('\nGoodbye thank you for using the mailroom!')
            break
        continue
