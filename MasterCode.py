# importing required libraries

import hashlib
import time
import itertools

# function to return the hexadecimal equivalent of SHA1

def hashfun(hashReturn):
    hash_result = hashlib.sha1(hashReturn.encode())
    return hash_result.hexdigest()

# function to compare two strings

def stringCompare(input1, input2):
    return (input1 == input2)


# creating a list of passwords to be deciphered
passList = [
    "7c4a8d09ca3762af61e59520943dc26494f8941b",
    "dd5fef9c1c1da1394d6d34b248c51be2ad740840",
    "0470f329d4cdde8d0f1e2b3271a1a7b45c65b104",
    "cbf307f96a3445446681f2a4050227c8c482d6ed",
    "fb96549631c835eb239cd614cc6b5cb7d295121a",
    "c1b89f8476a88e28ce442887a1cf20b5e91f3903",
    "ca67d9c2e761c54b3c4e4c728116215a50b75e0c",
    "7bcab7186dcec69d3f25cfe13e1ca6da6fd97bec",
    "95038fa46def5586d67e34fdad2114b231141e8b",
    "907f71f2de9430e340acca9f6257169509f3cf76",
    "822180141ebe398dee37d2fa34da4acd8edf3702",
    "955097395b07d7581550db81e7d0748e94714e7b",
    "27c4470db25a39ab137d1d38558f4e2a255e5ef6",
    "560f712240f6bc85ef67982df52bae70581a596d",
    "177080c8b8f44ea62c1a4baeeeb726ac1f9985ae",
    "808543b37169708c597e23c7adbe743be8e05ad7",
    "f0bd251b08338c230d420f33106faf13a12cace5",
    "916f39d2d8fa9f876bdd0a0871b88568ac3f49f0",
    "65abe9e1efbd6efbdf3d6ea3c4c2f6c0325cbb68",
    "64971e55e9e9709a7a167d9bdd19aa589fe2f3cd"
]

# code to read data from dictionary file

start_time = time.time()
file2 = open('dictionary.txt',encoding='utf-8-sig')
data = file2.read()
file2_list = data.split("\n")
file3_list = data.split("\n")

# code for creating list of values

combination_list = []
digit_counts = [1,2,3,4,5,6,7]
for n in digit_counts:
    digit_combinations = itertools.product(range(10), repeat=n)
    for digits in digit_combinations:
        digits = (''.join(map(str, digits)))
        combination_list.append(digits)

#function for combination 1
def combination1():
    file1 = open('dictionary.txt', encoding='utf-8-sig')
    count = 0
    n = 0
    Proc_count=0
    while (n < 5579):
        hashReturn = str((file1.readline()).strip())
        result1 = hashfun(hashReturn)
        for i in passList:
            status = stringCompare(i, result1)
            Proc_count+=1
            if (status == True):
                count += 1
                print(hashReturn, " := ", result1, " ? ", i, " = ", status)
                passList.pop(passList.index(i))
        n += 1
    file1.close()
    # print("combination1: ",Proc_count)
    return count

#function for combination 2
def combination2():
    file1 = open('dictionary.txt', encoding='utf-8-sig')
    count2=0
    Proc_count=0
    for i in range(0,5579):
        string1=str((file1.readline()).strip())
        for j in range(0,5579):
            string2=file2_list[j]
            stringCombined=string1+string2
            result2=hashfun(stringCombined)
            for i in passList: 
                status=stringCompare(i,result2)
                Proc_count+=1
                if (status==True):
                    count2+=1
                    print(stringCombined," := ",result2," ? ",i," = ",status) 
                    passList.pop(passList.index(i))
    file1.close()
    # print("combination2: ",Proc_count)
    return count2

#function for combination 3

def combination3():
    count3=0
    for i in range(1900,3000):   
        stringY=str(i)
        for j in range(1,13):
            stringM=str('{0:0>2}'.format(j))
            for k in range(1,32):
                stringD=str('{0:0>2}'.format(k))
                stringDate1=stringY+stringM+stringD
                stringDate2=stringD+stringM+stringY
                #print(stringDate)
                result3a=hashfun(stringDate1)
                result3b=hashfun(stringDate2)
                #count+=1
                for i in passList: 
                    status1=stringCompare(i,result3a)
                    status2=stringCompare(i,result3b)
                    if (status1==True or status2==True):
                        count3+=1
                        print(stringDate1," := ",result3a," ? ",i," = ",status1) 
                        passList.pop(passList.index(i))
    return count3   

#function for combination 4

def combination4():
    count4=0
    for digits in combination_list:
        result4=hashfun(digits)
        for i in passList:
            status = stringCompare(i,result4)
            if (status == True):
                count4 += 1
                print(digits, " := ", result4, " ? ",i," = ",status)
                passList.pop(passList.index(i))
    return count4

#function for combination 5

def combination5():
    count5 = 0
    for digits in combination_list:
        for j in range(0, 5579):
            string2 = file2_list[j]
            passw = string2 + digits
            result = hashfun(passw)
            for i in passList:
                status = stringCompare(i, result)
                if (status == True):
                    count5 += 1
                    print(passw, " := ", result, " ? ", i, " = ", status)
                    passList.pop(passList.index(i))
    return count5

#function for combination 6
 
def combination6():
    count6=0
    for i in range(100):
        num=str('{:09d}'.format(i))
        hres=hashfun(num)
        for j in passList:
            status = stringCompare(j,hres)
            if (status == True):
                count6+=1
                print(num, " := ", i, " ? ",j," = ",status)
                passList.pop(passList.index(j))
    return count6 

#funciton for combination 7

def combination7():
    file1 = open('dictionary.txt', encoding='utf-8-sig')
    count7=0
    Proc_count=0
    for i in range(0,5579):
        string1=str((file1.readline()).strip())
        for j in range(0,5579):
            string2=file2_list[j]
            for k in range(0,5579):
                string3=file3_list[k]
                stringCombined=string1+string2+string3
                # print(stringCombined)
                result7=hashfun(stringCombined)
                for l in passList:
                    status=stringCompare(l,result7)
                    Proc_count+=1
                    if (status==True):
                        count7+=1
                        print(stringCombined," := ",result7," ? ",l," = ",status)
                        passList.pop(passList.index(i))
    file1.close()
    print("combination7: ",Proc_count)
    return count7

#function calling


count=combination1()
count2=combination2()
count3=combination3()
count4=combination4()
count5=combination5()
count6=combination6()
count7=combination7()

print(count+count2+count3+count4+count5+count6+count7)

#print statement to calculate the amount of run time
print("--- %s seconds ---" % (time.time() - start_time))