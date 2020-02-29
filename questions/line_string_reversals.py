line = 'hello, my name is abc. I am good, but this is better.'
#out =  better, is this but good. am I abc, is name my hello.

def toList(Line):
    array = []
    curr_word = ''

    for i in range(len(Line)):
        if(Line[i].isalpha() is True):
            curr_word = curr_word + Line[i]
        elif(Line[i-1].isalpha() is True and Line[i].isalpha() is False):
            array.append(curr_word)
            if(Line[i] != ' '):
                array.append(Line[i])
            curr_word = ''
            i = i + 1
        else:
            if(Line[i] == ' '):
                pass
            else:
                array.append(Line[i])
    return array


def toString(LIST):
    result = ''
    for i in range(len(LIST)):
        if(LIST[i].isalpha() is False):
            result = result + LIST[i]
            #result = result + ' '
        else:
            if(i != 0):
                result = result + ' '
            result = result + LIST[i]
    return result



arr = toList(line)

left = 0
right = len(arr) - 1

while(left < right):
    if(arr[left].isalpha() is True and arr[right].isalpha() is True):
        arr[left] , arr[right] = arr[right], arr[left]
        left = left + 1
        right = right - 1
    elif(arr[left].isalpha() is False):
        left = left + 1
    elif(arr[right].isalpha() is False):
        right = right - 1
    else:
        pass

print(toString(arr))





# reverse a string
reverse_String = 'abc!@345cde!fg'

def stringToList(string):
    array = []

    for i in range(len(string)):
        array.append(string[i])
    return array


def revtoString(LIST):
    result = ''
    for i in LIST:
        result = result + i
    return result


#reverse_String_array = stringToList(reverse_String)
arr = stringToList(reverse_String)
left = 0
right = len(arr) - 1

while(left < right):
    if(arr[left].isalpha() is True and arr[right].isalpha() is True):
        arr[left] , arr[right] = arr[right], arr[left]
        left = left + 1
        right = right - 1
    elif(arr[left].isalpha() is False):
        left = left + 1
    elif(arr[right].isalpha() is False):
        right = right - 1
    else:
        pass

print(revtoString(arr))
