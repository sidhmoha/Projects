def swap_case(s):
    result = ""
    for char in s:
        if (char == char.upper()):
            result=result+char.lower()
        else:
            result=result+char.upper()

    return result


if __name__=='__main__':
    s=input()
    result=swap_case(s)
    print (result)