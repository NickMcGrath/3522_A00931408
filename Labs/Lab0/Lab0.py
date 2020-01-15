def im_a_function(x):
    if(x == 5):
        print("wow you got the right number!")


def main():
    #dictionary as a switch statement
    input_map = {
        1: func1,
        2: func2,
        3: func3,
        4: func4
    }
    user_input = int(input("Enter option: "))
