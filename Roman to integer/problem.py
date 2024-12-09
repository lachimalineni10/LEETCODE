def romanToInt(s):
    sum = 0
    d = {"I" : 1,"V" : 5,"X": 10,"L" : 50,"C" : 100,"D" : 500,"M" : 1000}
    for i in range(len(s)):
        if(i+1 < len(s)) and d[s[i]] < d[s[i+1]]:
            sum -= d[s[i]]
        else:
            sum += d[s[i]]
    return sum
    # d = {"I" : 1,"V" : 5,"X": 10,"L" : 50,"C" : 100,"D" : 500,"M" : 1000,"IV":4, "IX":9,"XL":40 ,"XC": 90 ,"CD":400 ,"CM": 900}
    # sum = 0
    # i = 0
    # while i < len(s):
    #     if i != len(s)-1:
    #         v = s[i] + s[i+1]
    #     else:
    #         v = s[i]
    #     if v in d:
    #         i += 1
    #         sum += d[v]
    #     else:
    #         sum += d[s[i]]
        
    #     i+=1
    # return sum
print(romanToInt(input("enter a string:")))


