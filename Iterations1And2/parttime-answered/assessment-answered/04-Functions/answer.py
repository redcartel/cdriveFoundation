def print_list(input_list):
    for x in range(len(input_list)):
        print("line",x,": ",input_list[x])

def squares_to(maximum):
    result = []
    for i in range(maximum):
        result.append(i*i)
    return result

if __name__ == "__main__":
    x = 12
    print_list(squares_to(x))