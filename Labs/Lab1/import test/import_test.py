from pack_test.pack_test import Toss, ExceptionB


def main():
    try:
        a = [Toss().tossb()]
    except ExceptionB:
        print("hi")


if __name__ == '__main__':
    main()
