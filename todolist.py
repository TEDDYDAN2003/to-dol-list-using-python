import random 


def todolist():
    listtask=[];
    listtime=[];
    name=("BANCUSHI ");
    print((f"HEY {name} this is a todolist program... "));
    def append_list():
        upperlimit=int(input("Enter the number of tasks you are going to do:  "))

        for i in range(0,upperlimit):
        
            task=input(f"enter task{i+1}:")
            listtask.append(task)
    append_list()        
    removal_option=input("do you want to REMOVE any item in the list: ")

    if removal_option=="true":
        listtask.pop()
    upperlimit=listtask.__len__() # this would update the value of upperlimit to the number of tasks after removal since len return list size
    print("below is the list of the task you are to do today: ")

    for i in range(0,upperlimit):
        print(f" {i+1}. {listtask[i]} ")

    update_option=input(" do you wish to update your list: ")
    if update_option=="true":
        num1=random.randint(1,8)
        num2=random.randint(1,8)
        result=num1*num2
        while True:
            user_result=int(input((f"SOLVE THE BELOW MATHEMATICAL QUIZ TO UPDATE: {num1} x {num2} =  ")))
            if result==user_result:
                print("YOU ARE A GENIUS")
                append_list()
                for i in range(0,upperlimit):
                    print(f" {i+1}. {listtask[i]} ")
                break
            else :
                print("failed !!      ---> try agian")  
        


            
    

todolist()