#slicing Lab


#def main():
     #input_string = input ('Enter a Sentence: ')
    #input_string = 'this is a string'
    #the_thirds(input_string)

def first_last_exchage(input_string):
    '''It takes input_string and returns the first and last items exchanged'''
    #I decided to save my input_string into a different varibable because I want to check the data type on line 26 and I am planning on turning this into a list

    split_firstlast_input = input_string
    #make it into a list to easly change the first and last items
    list_first_last= list(split_firstlast_input)
    #savenice  the first and last letters of the string
    first = split_firstlast_input [0]
    last = split_firstlast_input [-1]
    #removes the last and first letters of the string
    list_first_last.pop()
    list_first_last.pop(0)
    #We append the first letters to the list
    list_first_last.append(first)
    list_first_last.insert(0, last)

    #First check what type of item it is
    data_type = type(input_string)

    if data_type == str:
        convert_to_string = "".join(list_first_last)
        return convert_to_string

    if data_type == tuple:
        convert_to_tuple =tuple(list_first_last)
        return convert_to_tuple

    if data_type == list:
        return list_first_last


def every_other(input_string):
    '''It takes input_string and returns every other item'''
    #removes every other item
    every_other_final = input_string[::2]
    return every_other_final

def the_four(input_string):
    '''It takes input_string and returns the first 4 and the last 4 items removed, and then every other item in the remaining sequence'''
    #check what type of item it is
    data_type = type(input_string)

    if data_type == str:
        split_four_input = input_string.split()
        list_four_last= list(split_four_input)
        del list_four_last[:4]
        del list_four_last[-4:]
        final_four = list_four_last[::2]
        convert_to_string = " ".join(final_four)
        return convert_to_string
    else:
        the_four_list_tuple = input_string[4:-4:2]
        return the_four_list_tuple


def reversed_items(input_string):
    '''It takes input_string and returns  the elements reversed (just with slicing)'''
    string_length=len(input_string)
    reversed_seq = input_string[string_length::-1]
    return reversed_seq

def the_thirds(input_string):
    '''It takes input_string and returns  the last third, then first third, then the middle third in the new order.'''
    thirds_size = len(input_string) // 3

    # first is going to be from 0 to thirds_size
    first = input_string[0:thirds_size]
    second = input_string[thirds_size:thirds_size * 2]
    third = input_string[thirds_size * 2:]
    the_third_final = third + first + second
    return the_third_final


if __name__ == "__main__":
    # run some tests against exchange_fist_last()
    a_string = 'this is a string'
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_list = [12,45, 'osito', 'ilsse']

    #Need a longer sequences to test the_four
    a_string_longer = 'this is a string that we will remove the first four and the last four and then every other word'
    a_tuple_longer = (12,34,56,78,90,3,4,5,6,7,8,9)
    a_list_longer = [12,45, 'osito', 'ilsse', 34, 78, 89, 'Damien', 'mantra', 88, 63, 89, 56]


    assert first_last_exchage(a_string) == 'ghis is a strint'
    assert first_last_exchage(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert first_last_exchage(a_list) == ['ilsse', 45, 'osito', 12]
    print('First function passed')

    assert every_other(a_string) == 'ti sasrn'
    assert every_other(a_tuple) == (2, 13, 5)
    assert every_other(a_list) == [12, 'osito']
    print('Second function passed')

    assert the_four(a_string_longer) =='that will the four the four'
    assert the_four(a_tuple_longer) == (90,4)
    assert the_four(a_list_longer) == [34, 89, 'mantra']
    print('Third function passed')

    assert reversed_items(a_string) =='gnirts a si siht'
    assert reversed_items(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert reversed_items(a_list) == ['ilsse', 'osito', 45, 12]
    print('Fourth function passed')

    assert the_thirds(a_string) == 'stringthis is a '
    assert the_thirds(a_tuple) == (5, 32, 2, 54, 13, 12)
    assert the_thirds(a_list_longer) == ['mantra', 88, 63, 89, 56, 12, 45, 'osito', 'ilsse', 34, 78, 89, 'Damien']
    print('ALL PASSED!')

#main()