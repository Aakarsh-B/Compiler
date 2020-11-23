outPut = ('string accepted', 'string rejected')
index = 0
def checkAndPass(function, out):
    global index
    index += 1
    if(index < boundary):
        # print(value[index])
        function(value[index])
    elif index >= boundary:
        print(out)


def q0(charactor):
    # print("on Q0")
    if charactor == '0':
        checkAndPass(q0, outPut[0])
    elif charactor == '1':
        checkAndPass(q1, outPut[1])


def q1(charactor):
    # print("on Q1")
    if charactor == '0':
        checkAndPass(q2, outPut[1])
    elif charactor == '1':
        checkAndPass(q3, outPut[1])


def q2(charactor):
    # print("on Q2")
    if charactor == '0':
        checkAndPass(q4, outPut[1])
    elif charactor == '1':
        checkAndPass(q0, outPut[0])


def q3(charactor):
    # print("on Q3")
    if charactor == '0':
        checkAndPass(q1, outPut[1])
    elif charactor == '1':
        checkAndPass(q2, outPut[1])


def q4(charactor):
    # print("on Q4")
    if charactor == '0':
        checkAndPass(q3, outPut[1])
    elif charactor == '1':
        checkAndPass(q4, outPut[1])


if '__main__' == __name__:
    print("Enter the string")
    value = input()
    value = str(value).strip()
    boundary = len(value)
    q0(value[index])
