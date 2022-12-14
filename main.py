# TODO:
#   - Generate file in chunks (size of chunk is chosen by user)
#   - Improve TUI
#   - Add args support
#   - Support different languages (c++, python, javascript, java...)

from sys import argv, exit

def create_ifs(sign, number_range, chunk_size, file_name):
    tmp = ""
    pass_counter = 0
    chunk_counter = 0

    f = open(file_name, "a")

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
            print("Generated chunk number %d of %d" % (chunk_counter, (number_range // chunk_size)))
            
    f.write(tmp)
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
        print("\nGenerating sign %s (%d of %d)" % (sign, signs.index(sign), len(signs)))
        create_ifs(sign, number_range, chunk_size, file_name)


def main(args):
    if len(args) == 1:
        try:
            NUMBER_RANGE = int(input("Enter number range[10000]: "))
        except ValueError:
            NUMBER_RANGE = 10000
            print("Entered invalid number range. Usning default 10 000")

        try:
            CHUNK_SIZE = int(input("Choose chunk size[500]: "))
        except ValueError:
            CHUNK_SIZE = 500

        OUTPUT_FILE = input("Choose file name[my_first_calculator.py]: ")

        if OUTPUT_FILE == "":
            OUTPUT_FILE = "my_first_calculator.py"
        elif OUTPUT_FILE[-3:] != ".py":
            OUTPUT_FILE += ".py"
    elif 1 < len(args) <= 3:
        print("Error: Incorrect number of arguments")
        exit(1)
    else:
        try:
            NUMBER_RANGE = int(args[1])
        except ValueError:
            NUMBER_RANGE = 10000
            print("Entered invalid number range, using default 10 000")
        
        try:
            CHUNK_SIZE = int(args[2])
        except ValueError:
            CHUNK_SIZE = 500
            print("Entered invalid chunk size, using default 500")
        
        try:
            OUTPUT_FILE = str(args[3])
        except ValueError:
            OUTPUT_FILE = "my_first_calculator.py"
            print("Entered invalid output file name, using default my_first_calculator.py")

        if OUTPUT_FILE[-3:] != ".py":
            OUTPUT_FILE += ".py"
    

    print(OUTPUT_FILE)
    print(CHUNK_SIZE)
    print(NUMBER_RANGE)
    
    print("Welcome to unofficial my_first_calculator.py generator")
    create_file(OUTPUT_FILE, NUMBER_RANGE, CHUNK_SIZE)


if __name__ == '__main__':
    main(argv)