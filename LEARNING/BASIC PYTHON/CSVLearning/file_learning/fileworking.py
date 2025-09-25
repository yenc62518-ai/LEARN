with open('file.txt', 'w') as f :
    for i in range(5) :
        f.writelines(input("nhap "))
with open('file.txt', 'r') as f :
    lst = f.readlines()
lst.reverse()
with open('file.txt', 'w') as f : 
    for i in lst :
        f.writelines(i)
with open('file.txt', 'r') as f :
    print (f.readlines())