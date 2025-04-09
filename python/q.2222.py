def CountVCUL():
    f=open("C:/Users/lalkr/OneDrive/Desktop/sample.txt","r")
    data=f.read()
    U=L=V=C=0
    for i in data:
          if i.isalpha():
              if i.isupper():
                  U+=1
              if i.islower():
                  L+=1
              if i.lower() in 'aeiou':
                  V+=1
              else:
                  C+=1
    print("Vowels = ",V)
    print("Consonants = ",C)
    print("Lowercase = ", L)
    print("Uppercase = ", U)
    f.close()
CountVCUL()
