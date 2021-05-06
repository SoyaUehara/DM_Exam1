import dataset1
from sklearn import linear_model

if __name__ == "__main__":
    df = dataset1.exam1_5('output.tsv')
    reg = linear_model.LinearRegression()
    