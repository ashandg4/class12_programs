a=eval(input("Enter a list : "))
print("The original list is : ",a)
while True:
    print("Main menu")
    print("1. Insertion in list")
    print("2. Deletion from list")
    print("3. Exit")
    choice=int(input("Enter ur choice(1,2,3) : "))
    if choice==1:
        item=eval(input("Enter the value to be inserted: "))
        pos=int(input("Enter at which position value to be inserted: "))
        index=pos-1
        a.insert(index,item)
        print("List after insertion is: ",a)
    elif choice==2:
        print("Deletion menu")
        print("1. Deletion using value")
        print("2. Deletion using index")
        print("3. Delete sublist")
        dch=int(input("Enter your choice(1,2,3) : "))
        if dch==1:
            item=int(input("Enter the value to be deleted: "))
            a.remove(item)
            print("List after deletion : ",a)
        elif dch==2:
            index=int(input("Enter the index value whose value is to be deleted: "))
            a.pop(index)
            print("List after deletion : ",a)
        elif dch==3:
            l=int(input("Enter the lower limit of the list slices to be deleted: "))
            u=int(input("Enter the upper limit of the list slices to be deleted: "))
            del a[l:u]
            print("List after deletion : ",a)
        else:
            print("Invalid choice")
    elif choice==3:
        break
else:
    print("Valid choices are 1,2,3 only")
