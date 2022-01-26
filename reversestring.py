def reversestr(strval: str) -> str:
    totallen = len(strval)
    newstr = ""
    index = -1
    for x in range(totallen):
        newstr += strval[index]
        index -= 1
    return newstr


print(reversestr("desrever eb ot sdeen gnirtS YM"))

str1 = "dlroW olleH"
txt = str1[::-1]
print(txt) 