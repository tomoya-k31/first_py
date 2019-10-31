import utils as u


class Main:

    class_hensu = "test"
    class_num = 0

    def __init__(self):
        self.main = ""
        Main.class_num += 1

    def mmain(self):
        print(self.main)

    def set_main(self, val):
        self.main = val


if __name__ == '__main__':
    ma = Main()
    ma.mmain()
    print(ma.main)
    print(Main.class_hensu)
    ma = Main()
    ma.mmain()
    print(ma.main)
    print(Main.class_num)
    u.print_test("test222")
