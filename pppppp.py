"""while j < 15:
    if array_contain_strings[j] in array_contain_strings[j+1] and len(array_contain_strings[j+1]) > len(array_contain_strings[j]):
        array_contain_strings.pop(j)
        j = j + 1
    else:
        result.append(array_contain_strings[j])
        print(f"this is the final string {array_contain_strings[j]}. ")
        array_contain_strings.pop(j)


        
while 1:
    if array_contain_strings[j] in array_contain_strings[j+1]:
        if len(array_contain_strings[j+1]) > len(array_contain_strings[j]):
            array_contain_strings.pop(j)
        j = j + 1
    else:
        break
        result.append(array_contain_strings[j])
        print(f"this is the final string {array_contain_strings[j]}. ")
        array_contain_strings.pop(j)

        

#for child in array_contain_strings:
#    temp = len(child)
#    print(f"The length of the string is {temp}. \n")
# for child in array_contain_strings:
    #get current index of array
    arr_index = array_contain_strings.index(child)
    next_index = int(arr_index + 1)
    print(f"Next index value is {next_index}.")
    print(array_contain_strings[next_index])
    print(child)
    print(arr_index)
    
    if child in array_contain_strings[next_index]:
        if len(array_contain_strings[array_contain_strings.index(child)+1]) > len(child):
            final_str = array_contain_strings[array_contain_strings.index(child)+1]
    else:
        result.append(final_str)

for ch in result:
    print(ch)"""