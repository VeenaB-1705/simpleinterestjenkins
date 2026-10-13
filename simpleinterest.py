def simInt(principal,interest,time):
    return(principal*interest*time)/100

if __name__ =="__main__":
    p = int(input("enter principal amount"))
    i = int(input("enter interestt"))
    t = int(input("enter time"))

    print("simple interest:",simInt(p,i,t))