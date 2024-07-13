def convert(number, base):
    def tenToTwo(num):
        sum = []
        while (True):
            sum.append(num % 2)
            num = num // 2
            if (num == 0):
                break
        sum = (sum[::-1])
        newSum = ""
        for num in sum:
            newSum += str(num)
        return (newSum)

    def twoToTen(num):
        number = list(str(num))
        place = []
        for index in range(0, (len(str(num)))):
            place.append(2**index)
        place = place[::-1]
        sum = 0
        for index in range(0, (len(str(num)))):

            if ((int(number[index])) == 1):
                sum += int(place[index])
        return (sum)

    def sixteenToTen(num):
        num = num.upper()
        newNum = []
        for number in num:
            if (type(number) == str):
                if (number == "A"):
                    number = "10"
                elif (number == "B"):
                    number = "11"
                elif (number == "C"):
                    number = "12"
                elif (number == "D"):
                    number = "13"
                elif (number == "E"):
                    number = "14"
                elif (number == "F"):
                    number = "15"
            newNum.append(list(number))

        place = []
        for index in range(0, (len(str(num)))):
            place.append(16**index)
        place = place[::-1]

        i = 0
        sum = 0
        for item in newNum:
            number = ""
            for numbers in item:
                number += str(numbers)

            sum += int(number) * (int(place[i]))
            i += 1
        return (sum)

    def twoToSixteen(num):
        num = list(str(num))[::-1]
        s = ""
        i = 0
        newNum = []
        for item in num:
            if (i % 4 == 0):
                newNum.append(s[::-1])
                s = ""
            s += item
            i += 1
        newNum.append(s[::-1])
        newNum.remove("")
        newNum = newNum[::-1]
        sum = ""
        for item in newNum:
            item = twoToTen(item)
            if (item == 10):
                item = "A"
            elif (item == 11):
                item = "B"
            elif (item == 12):
                item = "C"
            elif (item == 13):
                item = "D"
            elif (item == 14):
                item = "E"
            elif (item == 15):
                item = "F"
            else:
                item = str(item)
            sum += item

        return (sum)

    def sixteenToTwo(num):
        num = sixteenToTen(num)
        num = tenToTwo(num)
        return (num)

    def eightToTen(num):
        newNum = list(str(num))
        place = []
        for index in range(0, (len(str(num)))):
            place.append(8**index)
        place = place[::-1]

        i = 0
        sum = 0
        for item in newNum:
            number = ""
            for numbers in item:
                number += str(numbers)

            sum += int(number) * (int(place[i]))
            i += 1
        return (sum)

    def twoToEight(num):
        num = list(str(num))[::-1]
        s = ""
        i = 0
        newNum = []
        for item in num:
            if (i % 3 == 0):
                newNum.append(s[::-1])
                s = ""
            s += item
            i += 1
        newNum.append(s[::-1])
        newNum.remove("")
        newNum = newNum[::-1]
        sum = ""
        for item in newNum:
            sum += str(twoToTen(item))

        return (sum)

    if (base == 2):
        try:
            return [number, twoToEight(number), twoToTen(number), twoToSixteen(number)]
        except:
            raise TypeError("The number is incorrect")
    elif (base == 8):
        try:
            ten = eightToTen(number)
            two = tenToTwo(ten)
            sixteen = twoToSixteen(two)
            return [two, number, ten, sixteen]
        except:
            raise TypeError("The number is incorrect")
    elif (base == 10):
        try:
            eight = twoToEight(tenToTwo(number))
            sixteen = twoToSixteen(tenToTwo(number))
            return [tenToTwo(number), eight, number, sixteen]
        except:
            raise TypeError("The number is incorrect")
    elif (base == 16):
        try:
            eight = twoToEight(sixteenToTwo(number))
            return [sixteenToTwo(number), eight, sixteenToTen(number), number]
        except:
            raise TypeError("The number is incorrect")
    else:
        raise ValueError("The base is incorrect")


def start():
    def show(two, eight, ten, sixteen):
        show = f"""
        |------------------------------------>                                  
        |   HEX : {sixteen                   }   
        |   DEC : {ten                       }       
        |   OCT : {eight                     }    
        |   BIN : {two                       }     
        |------------------------------------>
        """
        print(show)
    while (True):
        number = int(input("Please enter number : "))
        base = int(input("Please enter base : "))
        answer = convert(number, base)
        show(answer[0], answer[1], answer[2], answer[3])
        while (True):
            continue_convert = input("run program again ? [Y or N] : ")
            continue_convert = continue_convert.upper()
            if (continue_convert == "Y" or continue_convert == "N"):
                break
        if (continue_convert == "Y"):
            continue
        else:
            break

start()