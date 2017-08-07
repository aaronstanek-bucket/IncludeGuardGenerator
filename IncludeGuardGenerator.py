import sys

if sys.version_info.major!=3:
    raise Exception("This is python 3 code. Please use a python 3 interpreter.")

def saveToFile(filename,data):
    bdata = bytes(data)
    outfile = open(filename,"wb")
    outfile.truncate(0)
    outfile.seek(0,0)
    outfile.write(bdata)
    outfile.close()

def makeLda(s):
    ou = list(s.encode("utf8"))
    return ou

def merge(ou,n):
    for x in n:
        ou.append(x)

def cop(lda):
    ou = []
    merge(ou,makeLda("__"))
    for x in lda:
        if ((x>=65) and (x<=90)):
            ou.append(x)
        elif ((x>=97) and (x<=122)):
            ou.append(x-32)
        elif x>127:
            ou.append(x)
        else:
            ou.append(95)
    merge(ou,makeLda("_INCLUDED__"))
    return ou

def getName():
    inp = input("HEADER FILE NAME: ")
    if len(inp)==0:
        raise Exception("The specified name is empty.")
    return inp

def main():
    name = getName()
    nlda = cop(makeLda(name))
    ou = []
    merge(ou,makeLda("#ifndef "))
    merge(ou,nlda)
    merge(ou,[13,10])
    merge(ou,makeLda("#define "))
    merge(ou,nlda)
    merge(ou,[13,10,13,10,13,10])
    merge(ou,makeLda("#endif"))
    merge(ou,[13,10])
    saveToFile(name,ou)

main()
