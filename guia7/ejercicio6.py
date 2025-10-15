def rango10() -> None:
    i:int = 1
    while(i < 11):
        print(i)
        i +=1

def rango40() -> None:
    string:str = ""
    i:int = 10
    while(i < 41):
        string+=str(i) + " "
        i +=2
    print(string)

def eco() -> None:
    print("eco "*10)

eco()