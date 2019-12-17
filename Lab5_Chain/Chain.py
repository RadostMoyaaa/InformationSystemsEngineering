from colored import fg, bg, attr
from abc import ABC, abstractmethod


class Handler(ABC):  # Интерфейс обработчика
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractHandler(Handler):  # Базовый класс обработчика
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class BlueHandler(AbstractHandler):
    def handle(self, request):
        if request == "Blue":
            return f"%sBlue:  The console is blue, your request: {request}" % (fg(116))
        else:
            return super().handle(request)


class PinkHandler(AbstractHandler):
    def handle(self, request):
        if request == "Pink":
            return f" %s Pink:  The console is Pink, your request: {request}" % (fg(218))
        else:
            return super().handle(request)


class GreenHandler(AbstractHandler):
    def handle(self, request):
        if request == "Green":
            return f"%sGreen:  The console is green, your request: {request}" % (fg(83))
        else:
            return super().handle(request)

def client_code(handler):
    for color in ["Blue", "Green", "Pink"]:
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

    blueColor.set_next(greenColor).set_next(pinkColor)

    print("Chain: Blue > Green > Pink")
    client_code(blueColor)
    print("\n")

    print("Subchain: Green > Pink")
    client_code(greenColor)