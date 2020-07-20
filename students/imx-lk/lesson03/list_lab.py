#!/usr/bin/env python3

print('\n----Series 1 ----')
fruit =['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)
response = input("Enter your favorite fruit and we will add it to the list: ")
fruit.append(response.capitalize())
print(fruit)

#Display the fruit according to the index
response_num = int(input("Enter a number and I will display the fruit (1st item is # 1): "))
print("You selected: ", response_num, " which is fruit: ", fruit[response_num-1])

#Adding two more fruits to the front of the list
print('\n')
fruit2 = ["PineApple"]
fruit = fruit2 + fruit
print(fruit)
fruit.insert(0, 'Banana')
print(fruit)

#I am printing out only the ones that start with the letter P
for x in fruit:
    if x[0].capitalize() == 'P':
        print(x)


print('\n----Series 2 ----')
fruit_series2 = fruit
print(fruit_series2)
#remove the last fruit from the list
fruit_series2 .pop()

#Duplicate original list
fruit2 = fruit_series2 *2

print(fruit_series2)
response_remove = input('Please Enter the name of the fruit that you want to remove as it appears on the list: ')
while response_remove not in fruit_series2:
    response_remove = input('Does not exists, Enter the name of the fruit that you want to remove: ')

fruit_series2.remove(response_remove.capitalize())
print('\n Here is the list without ', response_remove," : ",fruit_series2)

print("\nHere is the original list duplicated: ", fruit2)

#removing response from duplicated list
while response_remove in fruit2:
    fruit2.remove(response_remove)
print('Here is the duplicated list without ', response_remove, " ", fruit2)



print('\n----Series 3 ----')
#Using the list we created in Series1 I am assuming it should include the items we added?
fruit_series3 = fruit
available_responses= ['Yes', 'yes', 'No', 'no']
new_fruit_list = []

for x in fruit_series3:
    response_likes = input('Enter yes or no, do you like '+ x.lower() + ' ?: ')
    while response_likes not in available_responses:
        response_likes = input('WRONG! Enter yes or no, do you like '+ x.lower() + ' ?: ')

    if response_likes.lower() == 'yes':
        new_fruit_list.append(x)
    else:
        continue

print("Here is a lit of items you like", new_fruit_list)


print('\n----Series 4 ----')
#Using the list we created in Series1 I am assuming it should include the items we added?
fruit_series4 = fruit
reversed_string = []
for item in fruit_series4:
    string_length=len(item)
    reversed_string.append(item[string_length::-1])

print("\nHere are the contents of the original, but with all the letters in each item reversed", reversed_string)

fruit.pop()
print("\nHere is the original list with the last item removed", fruit)







