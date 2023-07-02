import matplotlib.pyplot as plt
import numpy as np

def plot(name, x, y):
    plt.ylabel('epoch')
    plt.plot(y, x)
    plt.savefig('runs/' + name + '.png')
    plt.close()

if __name__ == '__main__':
    # test
    t = [[0.0337, 0.0367],
        [0.042,  0.0443],
        [0.0476, 0.0508]]
    t = np.array(t)
    plot('nghia_test', t[:,0], [0,1,2])
    plot('nghia2_test', t[:,1], [0,1,2])
