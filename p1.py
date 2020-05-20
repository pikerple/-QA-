
#1.(A)
def reverse_char(input):
    return input[::-1]
    
#1.(B)
def reverse_item(input):
    split = input.split(" ")
    answer = ""
    for i in range(len(split)-1):
        answer += (reverse_char(split[i])+" ")
    answer += reverse_char(split[-1])
    return str(answer)
