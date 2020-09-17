from time import sleep

class Hanoi:
    def __init__(self, n):
        self.n = n
        self.towers = [[x for x in range(n, 0, -1)], [], []]
        print(str(self))
    
    def move(self, n=None, start=1, end=3, aux=2):
        if n is None:
            n = self.n

        if n >= 1:
            self.move(n - 1, start, aux, end)
            self.towers[end-1].append(self.towers[start - 1].pop())
            sleep(2)
            print(str(self))
            self.move(n - 1, aux, end, start)
    
    def __str__(self):
        result = "\u001b[2J\u001b[H"
        for tower in self.towers:
            result += "> "
            for element in tower:
                result += str(element) + " "
            result += "\n"
        return result

tower = Hanoi(4)
tower.move()