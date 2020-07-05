#(i)assigning elements to different lists
#I didnt understand the question
#I did contact captain aviral multiple times in multiple platfoms
#but couldnt find the response i needed
#I also reminded him in the live(on 3rd july) but in vain
#anyways, this is what I understood
#and am finally writing this code because
#I waited for almost 48 hours and am still waiting for the responce
def i():
    l1=list(input("enter the elements to be assigned to the 1st list ").split())
    l2=list(input("enter the elements to be assigned to the 2nd list ").split())
    print("elements of 1st list ",l1)
    print("elements of 2nd list ",l2)

#(ii)accessing elements from tuple 
def ii():
    t=tuple(input("enter the elements of the tuple ").split())
    index=int(input("enter index of the element to be accessed"))
    print("you have accessed the element ",t[index])

#(iii)deleting different dictionary elements
def iii():
    i=0
    dictionary={}
    keys=list(input("enter the keys to be entered in the dictionary ").split())
    values=list(input("enter the values to be entered in the dictionary ").split())
    if len(keys) != len(values):
        print("length of values not equal with lenght of keys ")
        return
    for key in keys:
        dictionary[key]=values[i]
        i+=1
    delete=input("enter the key at which the value will be deleted ")
    if delete in keys:
        del dictionary[delete]
    else:
        print("invalid key")
    print("the present dictionary is ",dictionary)

decision=input("enter i for assigning elements to different lists\nii for accessing elements from tuple\niii for deleting different dictionary elements ")
if decision == "i":
    i()
elif decision == "ii":
    ii()
elif decision == "iii":
    iii()
else:
    print("invalid option")
