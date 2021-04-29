import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd


def true_function(x):
    """
    >>> true_function(0)
    0.0
    """
    return np.sin(np.pi*x*0.8)


if __name__ == "__main__":
    seed_List = []
    ture_num = []
    for i in range(0, 20):
        num = random.uniform(-1, 1)
        seed_List.append(num)
        ture_num.append(true_function(num))

    dic_arr = {'観測点': seed_List, '真値': ture_num}
    print(pd.DataFrame(dic_arr))
    dic_arr = pd.DataFrame(dic_arr)
    x = dic_arr['観測点']
    y = dic_arr['真値']

    fig = plt.figure()
    plt.scatter(x, y, color="black", label="data", s=5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    fig.savefig("ex1.2.png")
