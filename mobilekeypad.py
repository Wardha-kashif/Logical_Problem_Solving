# # Python3 implementation of the approach
#
# # Array to store how many times a button
# # has to be pressed for typing
# # a particular character
# arr = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1,
#        2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4];
#
#
# # Function to return the count of
# # buttons pressed to type the given string
# def countKeyPressed(string, length):
#     count = 0;
#
#     # Count the key presses
#     for i in range(length):
#         count += arr[ord(string[i]) - ord('a')];
#
#     # Return the required count
#     return count;
#
#
# # Driver code
# if __name__ == "__main__":
#     string = "abcdef";
#     length = len(string);
#
#     print(countKeyPressed(string, length));
#



key_lst = [
    {'a':(2,2)},
    {'b':(2,3)},
    {'c':(2,4)},
    {'d':(3,2)},
    {'e':(3,3)},
    {'f':(3,4)},
    {'g':(4,2)},
    {'h':(4,3)},
    {'i':(4,4)},
    {'j':(5,2)},
    {'k':(5,3)},
    {'l':(5,4)},
    {'m':(6,2)},
    {'n':(6,3)},
    {'o':(6,4)},
    {'p':(7,2)},
    {'q':(7,3)},
    {'r':(7,4)},
    {'s':(7,5)},
    {'t':(8,2)},
    {'u':(8,3)},
    {'v':(8,4)},
    {'w':(9,2)},
    {'x':(9,3)},
    {'y':(9,4)},
    {'z':(9,5)},
    {' ':(0,2)}

]

inp = "this is a message Hello\nbag"
print(inp)
inp = str(inp.lower())
char_list = [i for i in inp]

for char in char_list:
    for key in key_lst:
        if char == list(key.keys())[0]:
            print(list(key.values())[0], end=' ')
    if char == '\n':
        print(end='\n')