
# Smart Strategy for Cracking Passwords

In this project, a program is designed to implement dictionary-based attacks along with a few other brute force techniques for Cracking Passwords that are ciphered using SHA1 encryption.

The information provided for the project includes the Passwords.txt file which has the Passwords to be cracked, a dictionary text file having a list of words, and an instruction file with few hints on possible combinations of the passwords. 

Python is used as the programming language for developing algorithms and each combination is written into a function for ease of development. Brief information regarding each of the functions is explained below:

_I have imported all the hashed passwords in the Password.txt file into a list in the code for faster access and pop each of the hash after it is found for efficiency_ 

**Hashfun**:  This function returns the hash of a string passed as an input.

**StringCompare**: This returns a 'True' or 'False' after comparing the hash of the combination string and the hash to be deciphered.

## **combination1**: 
In this, the given dictionary.txt file is read and each string in the file is hashed for comparison with the given ciphers.

Example: 
        
        wednesday
        increasing

## **combination2**: 
Each of the two strings of the dictionary text file is appended and tested for their presence in given hashed passwords.

Example: 
        
        investigation+saving
## **combination3**: 
Dates of varied ranges are tested for their presence in the passwords file.

Example: 
        
        20230322 (YYYYMMDD)
## **combination4**: 
A range of digits is tested with different permutations.

Example: 

        123456
        654321
## **combination5**: 
A range of digits appended to the words in the dictionary file are tested.

Example: 
        
        marching2023
        honour99999 


## **combination6** : 
The pattern of digits is tested in this function.
Example:

        000000001

## **combination7** : 
The hash of each of the three appended words of the dictionary file is tested for comparison in this function.
Example:

        financial+master+spoken


