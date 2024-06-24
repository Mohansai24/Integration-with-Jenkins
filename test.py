str="babac"
for i in range(len(str)):
    for j in range (i+1,len(str)+1):
            s=str[i:j]
            print(s)
            if(s[::-1] == s):
                if (len(s)>1):
                    print("palindrone is :",s)
