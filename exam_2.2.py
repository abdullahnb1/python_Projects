a,b,c = str(input()),str(input()),str(input())
password = ""
if len(a)< 4:password += a
else:password += a[:4]
    
if len(b) % 2 == 0: mid = int((len(b)-2)/2); password += b[mid:mid+2]
else: mid = int((len(b)-1)/2); password += b[mid]

if len(c) <= 3: password += "ceng240"
elif 4 <= len(c) and len(c) < 7: password += "ceng"
else: password += "ce"
print(password)