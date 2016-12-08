import matplotlib.pyplot as plt

def main():
    data1 = [i for i in range(100)]
    data2 = [i for i in range(100)]
    xs = []
    ys = []

    for i in range(1000):
        for i in range(len(data1)):
            xs.append(data2[i]+1-1.4*(data1[i])**2)
            ys.append(0.3*data1[i])

    plt.title("Henon's Function")
    plt.plot(xs, ys, 'o')
    plt.plot(data1, data2, 's')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(["Fractal", "Original"])
    plt.savefig('Henons Formula Graph.jpeg')
    plt.show()


main()
