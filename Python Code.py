
def fractal_eval(expr):
    def arithmetic_evaluation(fractal_expression):
        return eval(fractal_expression)

    def evaluate_expression(subexpression):
        return arithmetic_evaluation(subexpression) ** 2

    def result_expression(fractal_expression):
        stack = []
        i = 0
        while i < len(fractal_expression):
            if fractal_expression[i] == '[':
                stack.append(i)
            elif fractal_expression[i] == ']':
                start = stack.pop()
                subexpression = fractal_expression[start + 1:i]
                result = evaluate_expression(subexpression)
                fractal_expression = fractal_expression[:start] + str(result) + fractal_expression[i + 1:]
                i = start + len(str(result)) - 1
            i += 1
        return arithmetic_evaluation(fractal_expression)

    return result_expression(expr)

def main():
    exp = input("Please Enter the Arithmetic Expression: ")
    print(round(fractal_eval(exp)))

if __name__ == "__main__":
    main()
