from graphviz import Digraph


def draw(vertices, edges):
    dot = Digraph()
    for v_id, v_label in vertices:
        dot.node(str(v_id), str(v_label))
    for src, dst in edges:
        dot.edge(str(src), str(dst))
    dot.render('graph_3', format='png', view=True)


class Chaos:
    def __init__(self, mu, state):
        self.mu = mu
        self.state = state
        self.stabilize()

    def stabilize(self):
        for _ in range(1000):
            self.next()

    def next(self):
        raise NotImplementedError("Метод next должен быть переопределен")


class LogisticMap(Chaos):
    def next(self):
        self.state = self.mu * self.state * (1 - self.state)
        return self.state


def visualize(system, steps=4):
    states = []
    edges = []
    for i in range(steps + 1):
        state = system.state
        states.append((i, state))
        if i > 0:
            edges.append((i - 1, i))
        system.next()
    draw(states, edges)
    for state in [s[1] for s in states[1:]]:
        print(state)


if __name__ == "__main__":
    visualize(LogisticMap(3.5, 0.1))