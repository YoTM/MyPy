# -*- coding utf-8 -*-
#!/usr/bin/python3

class ExtendedStack(list):
    def sum(self):
        # операция сложения
        if len(self) > 1:
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1+top2)

    def sub(self):
        # операция вычитания
        if len(self) > 1:
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1-top2)

    def mul(self):
        # операция умножения
        if len(self) > 1:
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1*top2)

    def div(self):
        # операция целочисленного деления
        if len(self) > 1:
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1//top2)

def start():
    x = ExtendedStack([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    print(x)
    x.sum()
    print(x)
    x.sub()
    print(x)
    x.mul()
    print(x)
    x.div()
    print(x)


if __name__ == '__main__':
    start()
