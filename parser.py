def check_syntax(tokens):
    errors = []

    brace_stack = []
    for i, (kind, value) in enumerate(tokens):
        if value == '{':
            brace_stack.append(i)
        elif value == '}':
            if not brace_stack:
                errors.append("Unmatched closing brace '}'")
            else:
                brace_stack.pop()

    if brace_stack:
        errors.append("Missing closing brace '}'")

    for i in range(len(tokens) - 1):
        if tokens[i][0] == 'IDENTIFIER' and tokens[i+1][1] == ';':
            continue

    return errors
