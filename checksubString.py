#array that contains strings and subStrings
#1: my name is farhan.
#2: i live in lahore.
#3: govt central model school
#4: long live pakistan

result = []
array_contain_strings = ["my","my name","my name is","my name is farhan","i","i live","i live in","i live in lahore","govt","govt central","govt central model","govt central model school","long","long live","long live pakistan"]
final_str = ""

for i in range(len(array_contain_strings)):
    if array_contain_strings[i] in array_contain_strings[i + 1]:
        if len(array_contain_strings[i + 1]) > len(array_contain_strings[i]):
            final_str = array_contain_strings[i + 1]
    else:
        result.append(final_str)
            











