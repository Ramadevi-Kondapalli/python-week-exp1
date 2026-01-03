base=int(input("enter the base number:"))
exponent=int(input("enter the exponent:"))
result=1
if exponent>0:
    for i in range(exponent):
        result*=base
elif exponent==0:
    result=1
else:
    for i in range(-exponent):
        result*=base
        result=1/result
print("result:",result)
