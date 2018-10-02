#program to find how many wovels inn given word
vowels=['a','e','i','o','u']
word=input("Enter some word")
l=[]
for letter in word:
    if letter in vowels:
        if letter not in l:
            l.append(letter)
print("Vowels found in word are %s ",l)
print("The number of vowels: ",len(l))
