import operator


def calculate_expression(expression):
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    try:
        expr = expression.strip().split()
        num1 = float(expr[0])
        op = expr[1]
        num2 = float(expr[2])

        result = operators[op](num1, num2)
        return result, None
    except (ValueError, ZeroDivisionError) as e:
        return None, str(e)


def main():
    errors = []
    results = []

    with open("exprs.txt", "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        result, error = calculate_expression(line)
        if result is not None:
            results.append((i + 1, result))
        else:
            errors.append((i + 1, error))

    with open("results.txt", "w") as f:
        for r in results:
            f.write(f"{r[0]} {r[1]}\n")

    with open("errors.txt", "w") as f:
        for e in errors:
            f.write(f"{e[0]} {e[1]}\n")


if __name__ == "__main__":
    main()