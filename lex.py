lines = []
print("Enter the input")
while True:
    try:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    except EOFError:
        break
text = '\n'.join(lines)
print(text)
text = text.split()


def returnType(value):
    if value == '+':
        print("+ : operator PLUS")
    elif value == '-':
        print("+ : operator PLUS")
    elif value == 'int':
        print("int : keyword")
    elif value == 'char':
        print("char : keyword")
    elif value == '=':
        print("= : operator EQ")
    elif value == '-':
        print("+ : operator PLUS")
    elif value.isdigit():
        print(value + " : number")
    else:
        print(value + " : identifier")


print(text)
for i in text:
    if "+" in i:
        i=i.split('+')
        i.insert(1,'+')
        print(i)
        for j in i:
            returnType(j)
    else:
        returnType(i)
