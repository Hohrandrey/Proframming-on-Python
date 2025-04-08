class Chaos:
    def __init__(self, mu, state):
        self.mu = mu
        self.state = state
        self.stabilize()

    def stabilize(self):
        for _ in range(1000):
            self.next()

    def next(self):
        raise NotImplementedError("Метод next должен быть переопределен в подклассе")


class LogisticMap(Chaos):
    def next(self):
        self.state = self.mu * self.state * (1 - self.state)
        return self.state


if __name__ == "__main__":
    for mu in [2.0, 3.2, 3.5, 3.55]:
        o = LogisticMap(mu, 0.1)
        print(o.next(), o.next(), o.next())