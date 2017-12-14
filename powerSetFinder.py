#THIS FUNCTION RETURN THE POWER SET BY N
#THE ACTION- CONVERT EACH VARIABE TO A BINARY NUMBER WHEN 1 IS TRUE AND 0 FALSE.
#FOR EXAMPLE- IF YOUR SET IS {"A","B","C"} --> {A}=001 , {C}=100 , {AB}=011 , {ABC}=111
def powerSetInit(n):
    if n<0:
        return [""]
    if n==0:
        return ["0"]
    if n==1:
        return ["0","1"]
    
    values=["00","01","10","11"]

    addedvalues=[]
    i=0
    numOfIterations=0
    while(i<n-2):
        for value in values:
            numOfIterations+=1
            addedvalues.append("0"+value)
            addedvalues.append("1"+value)
        values=addedvalues
        addedvalues=[]
        i+=1
    lenOf=len(values)
    return values

#THIS FUNCTION RETURN ARRAY OF NUMBERS BY A STRING of number
def stringToArrayOfInts(num):
    dig = list(int(d) for d in str(num))
    return dig
    
#THIS FUNCTION RETRUN ARRAY OF ARRAYS OF NUMBER BY A LIST OF STRINGS
def stringToArrayConverter(values):
    array=[]
    for v in values:
        array.append(stringToArrayOfInts(v))
        
    print(array)
    
      
#MAIN RUN PROGRAM
stringToArrayConverter(powerSetInit(5))
