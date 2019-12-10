# Подключение библиотеки абстрактных классов Abstract Base Class
from abc import ABCMeta, abstractmethod


# Функция поиска в глубину
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)
    return visited


# Интерфейс итератора
class Iterator(metaclass=ABCMeta):

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass

    @abstractmethod
    def current(self):
        pass

    @abstractmethod
    def first(self):
        pass


# Конкретный итератор для графа
class GraphIterator(Iterator):

    def __init__(self, graph, start='A'):  # Конструктор
        self.graph = graph
        self.start = start
        self.next = self.start
        self.visited = []
        self.i = 0

    def __iter__(self):  # Возвращает объект итератор
        return self

    def __next__(self):  # Возвращает следующий элемент графа в глубину
        self.i += 1
        if self.next not in self.visited:
            self.visited.append(self.next)
            for n in graph[self.next]:
                dfs(graph, n, self.visited)
        if self.i > len(self.visited) - 1:
            raise StopIteration()
        self.next = self.visited[self.i]
        return self.next

    def has_next(self):
        pass

    def current(self):  # Возвращает текущий элемент
        return self.next

    def first(self):  # Возвращает первый элемент
        self.next = self.start
        self.i = 0

# Интерфейс подписчика
class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, message: str) -> None:
        pass

# Интерфейс издателя
class Observable(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.observers = []

    def register(self, observer: Observer) -> None:
        self.observers.append(observer)

    def notify_observers(self, message: str) -> None:
        for observer in self.observers:
            observer.update(message)

# Конкретный издатель
class Publisher(Observable):

    def add_news(self, news: str) -> None:
        self.notify_observers(news)

# Конкретный подписчик
class Citizen(Observer):

    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, message: str) -> None:
        print('{} оповещен об том, что {}'.format(self.name, message))


# Клиент
if __name__ == '__main__':
    graph = {'A': (['B', 'C']),  # Инициализируем граф
             'B': (['A', 'D', 'E']),
             'C': (['A', 'F']),
             'D': (['B']),
             'E': (['B']),
             'F': (['C'])}

    itr = GraphIterator(graph)  # Создаем объект итератор графа
    news = Publisher()  # Создаем объект издатель
    news.register(Citizen('Алексей'))  # Создаем подписчиков и оформляем подписку
    news.register(Citizen('Максим'))
    for elem in itr:  # Проходим по графу
        print("Пройден {} узел графа".format(elem))  # Выводим результат
        if elem == "C" or elem == "D":  # Проверяем узел
            bbc = "узел {} пройден".format(elem)  # Формируем новость
            news.add_news(bbc)  # Добавляем новую новость, оповещаем подписчиков
    else:
        print("Поиск в глубину завершен")
