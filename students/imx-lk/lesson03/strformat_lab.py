#!/usr/bin/env python3

filename = 2
floating_number = 123.4567
integer_scientific_number = 10000
floating_scientific_number = 12345.67


print('\n ----TASK 1------')
task_one = 'file_{:03}, {:.2f}, {:.2e}, {:.2e}'.format(filename, floating_number, integer_scientific_number, floating_scientific_number  )
print(task_one)

print('\n ----TASK 2------')
task_two = f'file_{filename:03}, {floating_number:.2f}, {integer_scientific_number:.2e}, {floating_scientific_number :.2e}'
print(task_two)



print('\n ----TASK 3------')
def formatter(in_tuple):
    '''This takes in_tuple and creates a string which will format according to the lenght of the tuple'''
    length = len(in_tuple)
    tuple_needed = '{:d}    ' *length
    form_string = 'The '+ str(length)+ ' numbers are: '+ tuple_needed
    return form_string.format(*in_tuple)


##Takes in the tuple
input_list= input("Enter as many numbers as you like with a comma: ")
list_made=input_list.split(',')

#Turn the list of strings into an integer before making it a tuple
list_integer = []
for x in list_made:
    list_integer.append(int(x))

in_tuple = tuple(list_integer)

form_string = formatter(in_tuple)
print(form_string)



print('\n ----TASK 4------')
tuple_task4 = ( 4, 30, 2017, 2, 27)
#use string formating to print:'02 27 2017 04 30'
new_tuple_task4=f'{tuple_task4[3]:02d}, {tuple_task4[4]:02d}, {tuple_task4[2]}, {tuple_task4[0]:02d}, {tuple_task4[1]:2d}'
print(new_tuple_task4)

print('\n ----TASK 5-----')
list_task5 = ['oranges', 1.3, 'lemons', 1.1]
#Write an f-string that will display: The weight of an orange is 1.3 and the weight of a lemon is 1.1
#Now see if you can change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher).
string_task5 =f'The weight of {list_task5[0].upper()} is {list_task5[1]*1.20} and the weight of the {list_task5[2].upper()} is {list_task5[3]*1.2}'
print(string_task5)

print('\n ----TASK 6-----')
#Print a table of several rows, e/a with a name, age and cost.Some of the costs are in the hundreds and thousands to test your alignment specifiers.
task6 = [['Damien', 30, '1000'], ['Osito',6,'12'], ['Teddy', 5, '100']]
base = 100
width = 100
print('{:<10} {:^20} {:>0}'.format('Name', 'Age', 'Price'))
print('---------------------------------------')

for item in task6:
    print('{:<10} {:^20} {:>0}'.format(*item))
    print('---------------------------------------')

#tuple with 10 consecutive numbers, quickly print the tuple in columns that are 5 charaters wide? It can be done on one short line!
tuple_extra6 = (10,34,678,45,1234,1,90,78,11111,909090)
length6 = len(tuple_extra6)
print(('{:^5d}'*length6).format(*tuple_extra6))











