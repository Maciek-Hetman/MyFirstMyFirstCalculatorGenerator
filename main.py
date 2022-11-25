# TODO:
#   - Generate file in chunks (size of chunk is chosen by user)
#   - Improve TUI
#   - Add args support


def create_ifs(sign, number_range, chunk_size, file_name):
    tmp = ""
    pass_counter = 0
    chunk_counter = 0

    f = open(file_name, "a")

    print("\nGenerating first chunk")
    for i in range(0, number_range+1):
        for j in range(0, number_range+1):
            # TODO: Optimize this
            if sign == "+":
                res = i+j
            elif sign == "-":
                res = i-j
            elif sign == "/":
                try:
                    res = i/j
                except ZeroDivisionError:
                    res = "Inf"
            elif sign == "*":
                res = i*j

            tmp += "if sign == '%s' and a == %s and b == %s:\n\tprint(%s)\n\n" % (sign, i, j, str(res))
    
        pass_counter += 1
        
        if (pass_counter % chunk_size) == 0:
            f.write(tmp)
            tmp = ""
            chunk_counter += 1
            print("Generating chunk number %d of %d" % (chunk_counter, (number_range // chunk_size)))

    f.close()


def create_file(file_name, number_range, chunk_size):
    signs = ["+", "-", "/", "*"]
    code = """print('Wecome to this calculator')
sign = input('Please select sign(+, -, *, /): ')
a = int(input('Input first number: '))
b = int(input('Input second number: '))\n\n
"""
    
    with open(file_name, "w") as f:
        f.write(code)
        f.close()

    for sign in signs:
        print("\nGenerating sign %s" % sign)
        create_ifs(sign, number_range, chunk_size, file_name)


def main():
    print("Welcome to unofficial my_first_calculator.py generator\n")

    NUMBER_RANGE = 0
    while NUMBER_RANGE == 0:
        try:
            NUMBER_RANGE = int(input("Choose number range: "))
        except ValueError:
            print("gib number")
    
    try:
        CHUNK_SIZE = int(input("Choose chunk size[50]: "))
    except ValueError:
        CHUNK_SIZE = 50

    OUTPUT_FILE = input("Choose file name[my_first_calculator.py]: ")

    if OUTPUT_FILE == "":
        OUTPUT_FILE = "my_first_calculator.py"
    elif OUTPUT_FILE[-3:] != ".py":
        OUTPUT_FILE += ".py"
    
    create_file(OUTPUT_FILE, NUMBER_RANGE, CHUNK_SIZE)


if __name__ == '__main__':
    main()