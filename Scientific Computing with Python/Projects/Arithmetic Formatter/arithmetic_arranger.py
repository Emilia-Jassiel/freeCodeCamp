def arithmetic_arranger(Array_of_Strings, Answer=False): 
    if (type(Array_of_Strings) is list): 
        if (len(Array_of_Strings) > 5): 
            return "Error: Too many problems."
        elif (len(Array_of_Strings) == 0): 
            return "Error: No elements in the array."
        else: 
            First_Operand = ""
            Second_Operand = ""
            Lines = ""
            if Answer:
                Sum = ""
            arranged = ""
            for i in Array_of_Strings:
                part = i.split()
                if (len(part[0]) > 4 or len(part[0]) < 1 or len(part[-1]) > 4 or len(part[-1]) < 1): 
                    return "Error: Numbers cannot be more than four digits."
                elif (part[1] != '+' and part[1] != "-"):
                    return "Error: Operator must be '+' or '-'."
                else:
                    lines = "-"
                    First_Row = str(part[0]).rjust(max(len(part[0]), len(part[-1])) + 2)
                    Second_Row = part[1] + " " + str(part[-1]).rjust(max(len(part[0]), len(part[-1])))
                    for j in range(max(len(part[0]), len(part[-1])) + 1):
                        lines += "-"
                    
                    if i != Array_of_Strings[-1]: 
                        First_Operand += First_Row + "    "
                        Second_Operand += Second_Row + "    "
                        Lines += lines + "    "
                        if Answer: 
                            if part[1] == "+": 
                                Sum += str(int(part[0]) + int(part[-1])).rjust(max(len(part[0]), len(part[-1])) + 2)
                            else: 
                                Sum += str(int(part[0]) - int(part[-1])).rjust(max(len(part[0]), len(part[-1])) + 2)
                            Sum += "    "
                    else: 
                        First_Operand += First_Row
                        Second_Operand += Second_Row
                        Lines += lines
                        if Answer: 
                            if part[1] == "+": 
                                Sum += str(int(part[0]) + int(part[-1])).rjust(max(len(part[0]), len(part[-1])) + 2)
                            else: 
                                Sum += str(int(part[0]) - int(part[-1])).rjust(max(len(part[0]), len(part[-1])) + 2)
                    if Answer: 
                        arranged = First_Operand + "\n" + Second_Operand + "\n" + Lines + "\n" + Sum
                    else: 
                        arranged = First_Operand + "\n" + Second_Operand + "\n" + Lines
            return arranged
    else: 
        return "The array inserted is not a list"