from colored import fg, bg, attr
from abc import ABC, abstractmethod


class Handler(ABC):  # Интерфейс обработчика
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractHandler:  # Базовый класс обработчика
    _next_handler = None

    def set_next_deleg(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

    def handleBlue(self, request):
        if request == "Blue":
            return f"%sBlue:  The console is blue, your request: {request}" % (fg(116))
        else:
            return self.handle(request)

    def handlePink(self, request):
        if request == "Pink":
            return f" %s Pink:  The console is Pink, your request: {request}" % (fg(218))
        else:
            return self.handle(request)

    def handleGreen(self, request):
        if request == "Green":
            return f"%sGreen:  The console is green, your request: {request}" % (fg(83))
        else:
            return self.handle(request)


class BlueHandler:
    def __init__(self):
        self._delegat = AbstractHandler()

    def handle(self, request):
        return self._delegat.handleBlue(request)

    def set_next(self, handler):
        return self._delegat.set_next_deleg(handler)


class PinkHandler:
    def __init__(self):
        self._delegat = AbstractHandler()

    def handle(self, request):
        return self._delegat.handlePink(request)

    def set_next(self, handler):
        return self._delegat.set_next_deleg(handler)

class GreenHandler:
    def __init__(self):
        self._delegat = AbstractHandler()

    def handle(self, request):
        return self._delegat.handleGreen(request)

    def set_next(self, handler):
        return self._delegat.set_next_deleg(handler)


def client_code(handler):
    for color in ["Blue", "Pink", "Green"]:
        print(f"\nClient: Wanna see {color} color?")
        result = handler.handle(color)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {color} was left untouched.", end="")



if __name__ == "__main__":
    blueColor = BlueHandler()
    greenColor = GreenHandler()
    pinkColor = PinkHandler()

    blueColor.set_next(pinkColor).set_next(greenColor)

    print("Chain: Blue > Pink > Green")
    client_code(blueColor)
    print("\n")

    print("Subchain: Pink > Green")
    client_code(pinkColor)