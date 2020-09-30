#array that contains strings and subStrings
#1: my name is farhan.
#2: i live in lahore.
#3: govt central model school
#4: long live pakistan
result = []
array_contain_strings = ["my","my name","my name is","my name is farhan","i","i live","i live in","i live in lahore","govt","govt central","govt central model","govt central model school","long","long live","long live pakistan"]
final_str = ""
i = 0
j = 0
for child in array_contain_strings:
    
    while i<15:
        if child in array_contain_strings[j+1]:
            if len(array_contain_strings[j+1]) > len(child):
                temp = array_contain_strings[j+1]
        else:
            result.append(array_contain_strings[j+1])
            break
        j = j + 1
        i = i + 1





"""for x in range(len(array_contain_strings)):
    temp = array_contain_strings[i]
    if str(x) in temp:
        if len(temp) > len(x):
            final_str = array_contain_strings[i+1]
            print(final_str)
        else:
            result.append(final_str)
    i = i + 1
for child in result:
    print(child)"""






#for child in array_contain_strings:
#    temp = len(child)
#    print(f"The length of the string is {temp}. \n")
