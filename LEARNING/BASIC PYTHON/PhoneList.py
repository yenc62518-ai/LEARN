contacts = {}
n = True
while (n) :
    button = input("nhap viec muon lam ")
    if (button == "add") :
        contacts.update({input("Ten ") : int(input("SDT "))})
    elif (button == "remove") :
        name = input("Ten ")
        contacts.pop(name)
    elif (button == "find") :
        name = input("Ten ")
        if name in contacts :
            print(contacts[name])
        else :
            print("Nguoi dung khong ton tai")
    elif (button == "watch") :
        print(contacts) 
    elif (button == "exit") :
        print("Dang thoat chuong trinh")
        n=False