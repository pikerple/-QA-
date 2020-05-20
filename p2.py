def p2(input):
    answer = 0
    for i in range(1,input+1):
        if((i % 3 == 0 and i % 5 == 0) or (i % 3 != 0 and i % 5 != 0)):
            # print(i)
            answer +=1
    return answer
# print(p2(15))