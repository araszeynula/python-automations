while True:
    choice = input("enter your choice(1 = append task ; 2 = read todolist ; 3 = exit) : ")
    if choice == "1":
        task = input("enter your task : ")
        with open("todolist.txt","a",encoding="utf-8")as file:
            file.write(task + "\n")
    elif choice == "2":
        try:
            with open("todolist.txt","r",encoding="utf-8")as file:
                data = file.read()
                if data.strip() == "":
                    print("your todolist is empty \n")
                else:
                    print("--yout to do list---")
                    print(data)
        except FileNotFoundError:
            print("No todolist found yet. Please add a task first.\n")
    elif choice == "3":
        print("goodbye")
        break
    else:
        print("invalid choice, please enter 1,2 or 3 \n")
