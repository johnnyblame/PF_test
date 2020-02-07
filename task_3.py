def parentheses_checker(inc_str):
    stack = []
    open_list = ["(", "[", "{"]
    close_list = [")", "]", "}"]
    for i in inc_str:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            index = close_list.index(i)
            if len(stack) > 0 and open_list[index] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return False
    if len(stack) != 0:
        return False
    else:
        return True


print(parentheses_checker("((5+3)*2+1)"))
print(parentheses_checker("{[(3+1)+2]+}"))
print(parentheses_checker("(3+{1-1)}"))
print(parentheses_checker("[1+1]+(2*2)-{3/3}"))
print(parentheses_checker("(({[(((1)-2)+3)-3]/3}-3)"))
print(parentheses_checker("2+3"))



