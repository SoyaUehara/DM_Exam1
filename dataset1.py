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


if __name__ == "__main__":
    font_path = '/Library/Fonts/Arial Unicode.ttf'
    font_prop = font_manager.FontProperties(fname = font_path)
    matplotlib.rcParams['font.family'] = font_prop.get_name()
    seed_List = []
    ture_num = []
    for i in range(0, 20):
        num = random.uniform(-1, 1)
        seed_List.append(num)
        Gauss = np.random.normal(0.0, 2.0, (1, 1))
        ture_num.append(true_function(num)+Gauss[0][0])

    dic_arr = {'観測点': seed_List, '観測値': ture_num}
    df = pd.DataFrame(dic_arr)
    df.to_csv('output.tsv', sep='\t', index=False)