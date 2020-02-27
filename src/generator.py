import parser

if __name__ == "__main__":
    arguments = parser.get_arguments()
    for argument in arguments:
        print(argument)