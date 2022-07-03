def find_broken_bracket(stmt):
    queue = []

    for char in stmt:
        if char == '(':
            queue.append(')')

        elif char == '[':
            queue.append(']')

        elif char == '{':
            queue.append('}')

        else:
            pass

        if len(queue) > 0 and char == queue[-1]:
            queue.pop(len(queue) - 1)

    return 1 if len(queue) > 0 else 0


