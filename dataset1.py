import numpy as np
import matplotlib.pyplot as plt


def true_function(x):
    """
    >>> true_function(0)
    0.0
    """
    return np.sin(np.pi*x*0.8)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    datasets = np.array([[-1], [1]])
    x = datasets[:, 0]
    fig = plt.figure()
    plt.plot(x, true_function(x), color='black', label="data test")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    fig.savefig("ex1.1.png")
