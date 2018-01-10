# -*- coding utf-8 -*-
#!/usr/bin/python3

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, arg):
        super(LoggableList, self).append(arg)
        self.log(arg)


def start():
    x = LoggableList([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    print(x)
    x.append([123])


if __name__ == '__main__':
    start()
