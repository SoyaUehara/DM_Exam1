import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd
import matplotlib
import matplotlib.font_manager as font_manager


def true_function(x):
    """
    >>> true_function(0)
    0.0
    """
    return np.sin(np.pi*x*0.8)


def exam1_1():
    datasets = np.array([[-1],[1]])
    fig = plt.figure()
    plt.plot(datasets, true_function(datasets), color='black', label="data")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    fig.savefig("ex1.1.png")

def exam1_2():
    seed_List = []
    ture_num = []
    for i in range(0, 20):
        num = random.uniform(-1, 1)
        seed_List.append(num)
        ture_num.append(true_function(num))
    fig = plt.figure()
    df = pd.DataFrame({'観測点': seed_List, '真値': ture_num})
    plt.scatter(df['観測点'], df['真値'], color="black", label="data", s=5)
    plt.xlabel('観測点')
    plt.ylabel('真値')
    plt.legend()
    plt.show()
    fig.savefig("ex1.2.png")

def exam1_3():
    seed_List = []
    ture_num = []
    for i in range(0, 20):
        num = random.uniform(-1, 1)
        seed_List.append(num)
        Gauss = np.random.normal(0.0, 2.0, (1, 1))
        ture_num.append(true_function(num)+Gauss[0][0])
    fig = plt.figure()
    df = pd.DataFrame({'観測点': seed_List, '観測値': ture_num})
    plt.scatter(df['観測点'], df['観測値'], color="black", label="data", s=5)
    plt.xlabel('観測点')
    plt.ylabel('観測値')
    plt.legend()
    plt.show()
    fig.savefig("ex1.3.png")


def exam1_4():
    seed_List = []
    ture_num = []
    for i in range(0, 20):
        num = random.uniform(-1, 1)
        seed_List.append(num)
        Gauss = np.random.normal(0.0, 2.0, (1, 1))
        ture_num.append(true_function(num)+Gauss[0][0])
    df = pd.DataFrame({'観測点': seed_List, '観測値': ture_num})
    df.to_csv('output.tsv', sep='\t', index=False)


def exam1_5():
    df = pd.read_csv('output.tsv', sep='\t')



if __name__ == "__main__":
    font_path = '/Library/Fonts/Arial Unicode.ttf'
    font_prop = font_manager.FontProperties(fname = font_path)
    matplotlib.rcParams['font.family'] = font_prop.get_name()
    exam1_5()
