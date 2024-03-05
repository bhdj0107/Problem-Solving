from collections import deque
def infix_to_postfix(data):
    output = []
    stack = []
    # data_queue = deque(map(str, data.split()))
    data_queue = deque()
    for i in data:
        data_queue.append(i)

    while data_queue:
        value = data_queue.popleft()

        # 값이 여는 괄호인 경우
        # 스택에 그냥 추가
        if value == '(': stack.append(value)

        # 값이 닫는 괄호인 경우
        # 스택에 있는 연산자들을 여는 괄호를 만날때 까지 pop 하여 output에 넣는다.
        elif value == ')':
            while stack:
                tmp = stack.pop()
                if (tmp == '('):
                    break
                else: output.append(tmp)


        # 값이 +또는 -일 경우, 여는 괄호 앞까지의 연산자를 모두 pop 하여 output에 넣고
        # stack에 자신을 push 한다.
        elif value in '+-':
            while stack:
                tmp = stack.pop()
                if (tmp == '('):
                    stack.append(tmp)
                    break
                else: output.append(tmp)
            stack.append(value)

        # 값이 * 또는 / 일 경우, 여는괄호 또는 -+ 앞까지의 연산자를 모두 pop 하여 output에 넣고
        # stack에 자신을 push 한다.
        elif value in '*/':
            while stack:
                tmp = stack.pop()
                if tmp in '(+-':
                    stack.append(tmp)
                    break
                else: output.append(tmp)
            stack.append(value)

        # 그 외의 경우는 피연산자이므로 그냥 output에 추가한다.
        else: output.append(value)

    # 위의 처리가 완료된 후 stack 에 남은 연산자들을 output에 넣어준다.
    while stack:
        output.append(stack.pop())
    return output

print("".join(infix_to_postfix(input())))