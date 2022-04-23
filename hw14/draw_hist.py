import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams['font.family'] = ['NanumGothic', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False

    dices = np.random.randint(1, 7, size=100)

    print(dices)

    plt.hist(dices, bins=6, color="b")
    plt.show()


if __name__ == "__main__":
    main()
