class A:
    class_static_var_a = 5
    print('class A variable start')

    def __init__(self, meme):
        print('in A constructor')
        self.meme = meme

    def mini_method(self):
        print('mini method a')


class B(A):
    class_static_var_b = 10
    print('class B variable start')
    def __init__(self, bum):
        super().mini_method()
        print('in B constructor')
        print(B.class_static_var_a, B.class_static_var_b)
        # super().__init__(bum)
        self.inital = 1;
        print(self.inital)
        # print(self.meme) -> 'B' object has no attribute 'meme'
        super().__init__(bum)
        print('after super call')
        print(self.meme)
    def test(self):
        self.meme
    def mini_method(self):
        print('mini method b')

def main():
    s = B('bum')
if __name__ == '__main__':
    main()