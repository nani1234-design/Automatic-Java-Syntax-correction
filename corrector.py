def auto_correct(code):
    lines = code.split('\n')
    corrected = []

    for line in lines:
        stripped = line.strip()

        if stripped and not stripped.endswith((';', '{', '}')) and \
           any(stripped.startswith(k) for k in ['int', 'float', 'double', 'String']):
            line += ';'

        corrected.append(line)

    open_braces = sum(l.count('{') for l in corrected)
    close_braces = sum(l.count('}') for l in corrected)

    while close_braces < open_braces:
        corrected.append('}')
        close_braces += 1

    return '\n'.join(corrected)
