# Copy here code of line function from previous exercise
def line(number, string):

    if string == "":
        print(number * "*")
    else:
        print(number * string[0])

def square_of_hashes(size):
    # You should call function line here with proper parameters
    for i in range(1, size + 1):
        line(size, "#")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
