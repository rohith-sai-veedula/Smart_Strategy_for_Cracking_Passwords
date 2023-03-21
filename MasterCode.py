# importing required libraries
import hashlib
import time

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
file1 = open('dictionary.txt', encoding='utf-8-sig')
file2 = open('dictionary.txt',encoding='utf-8-sig')
data = file2.read()
file2_list = data.split("\n")

#function for combination 1
def combination1():
    count = 0
    n = 0
    while (n < 5579):
        hashReturn = str((file1.readline()).strip())
        result1 = hashfun(hashReturn)
        for i in passList:
            status = stringCompare(i, result1)
            if (status == True):
                count += 1
                print(hashReturn, " := ", result1, " ? ", i, " = ", status)
                passList.pop(passList.index(i))
        n += 1
    file1.close()
    return count

#function for combination 2
def combination2():
    file1 = open('dictionary.txt', encoding='utf-8-sig')
    count2=0
    for i in range(0,5579):
        string1=str((file1.readline()).strip())
        for j in range(0,5579):
            string2=file2_list[j]
            stringCombined=string1+string2
            result2=hashfun(stringCombined)
            for i in passList: 
                status=stringCompare(i,result2)
                if (status==True):
                    count2+=1
                    print(stringCombined," := ",result2," ? ",i," = ",status) 
                    passList.pop(passList.index(i))
    file1.close()
    return count2




#function calling
count=combination1()
count2=combination2()
print(count2+count)

#print statement to calculate the amount of run time
print("--- %s seconds ---" % (time.time() - start_time))

