def int_to_reverse_binary(user_num):
    binary_val = ''
#write your while loop here
    while user_num > 0:
        binary_val = binary_val + str(int(user_num % 2))
        user_num = (user_num - (user_num % 2))/2
    if binary_val == '':
        binary_val = '0'
    return binary_val


def string_reverse(input_string):

    reverse_input = ''
    if input_string == '0':
        return '0'
   #write your for loop here
    n = len(input_string)
    j = 1
    while j < n + 1:
        reverse_input = reverse_input + input_string[-j]
        j = j +1
    
    return reverse_input

if __name__ == '__main__':
    user_input = int(input())

    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)