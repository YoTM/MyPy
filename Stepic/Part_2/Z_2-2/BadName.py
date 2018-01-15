_GREETING = "Hello, "

class BadName(Exception):
    pass

def greet(name):
    """
    Ф-ия получает имя и проверяет его
    на наличие заглавной буквы
    если написано не с заглавной,
    то кидает исключение
    :param name:
    :return:
    """

    if name[0].isupper():
        return _GREETING + name
    else:
        raise BadName(name + " is innaporiate name")

#__all__ = ("BadName", "greet")
