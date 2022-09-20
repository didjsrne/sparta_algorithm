s = "(())()"


def is_correct_parenthesis(string):
    stack = []

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)  # 스택에 ( 저장
        elif string[i] == ")":
            if len(stack) == 0:  # 닫는게 나왔는데 스택에 (가 없다? 바로 False
                return False
            stack.pop()  # 스택에서 ( 빼서 () 완성

    if len(stack) != 0:  # 스택에 (가 남아있다? 바로False
        return False
    else:
        return True



print(is_correct_parenthesis(s))