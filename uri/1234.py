
while True:
    try:
        string = list(input())
        sentenca = []

        for i in string:
            if i.isalpha():
                sentenca.append(i)

        vdd = True
        for j in range(len(sentenca)):
            if vdd:
                sentenca[j] = sentenca[j].upper()
                vdd = False
            else:
                sentenca[j] = sentenca[j].lower()
                vdd = True

        l = 0
        for k in range(len(string)):
            if string[k].isalpha():
                string[k] = sentenca[l]
                l += 1
        
        print(''.join(string))
    except EOFError:
        break
