import matplotlib.pyplot as plt
import numpy as np


def drawHeart():
    t = np.linspace(0, np.pi, 1000)
    x = np.sin(t)
    y = np.cos(t) + np.power(x, 2.0 / 3)
    plt.plot(
        x,
        y,
        color='red',
        linewidth=2,
    )
    plt.plot(
        -x,
        y,
        color='red',
        linewidth=2,
    )

    plt.ylim(-1.5, 2)
    plt.xlim(-1.5, 1.5)

    plt.show()


if __name__ == "__main__":
    drawHeart()
