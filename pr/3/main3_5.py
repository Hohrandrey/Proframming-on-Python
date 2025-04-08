import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta


class LogisticMap:
    def __init__(self, mu, state):
        self.mu = mu
        self.state = state

    def next(self):
        self.state = self.mu * self.state * (1 - self.state)
        return self.state


o = LogisticMap(mu=4.0, state=0.1)
values = [o.next() for _ in range(10000)]

plt.figure(figsize=(10, 6))
plt.hist(values, bins=50, density=True, alpha=0.6)

x = np.linspace(0.01, 0.99, 1000)
plt.plot(x, beta.pdf(x, 0.5, 0.5), 'r-', lw=2)

plt.title('3.5')
plt.legend()
plt.show()