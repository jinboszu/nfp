import matplotlib.pyplot as plt
from nfp import nfp


def plot_nfp(P, Q, R):
    _, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    xs, ys = zip(*P)
    ax.plot(xs + xs[:1], ys + ys[:1], color='tab:blue')

    xs, ys = zip(*R)
    ax.fill(xs, ys, facecolor='tab:red', alpha=0.25)

    for rx, ry in R:
        xs, ys = zip(*[(rx + qx, ry + qy) for qx, qy in Q])
        ax.plot(xs + xs[:1], ys + ys[:1], color='tab:green')
        ax.scatter(xs[:1], ys[:1], color='tab:green', zorder=3)

    plt.show()


if __name__ == '__main__':
    P = [(0, 0), (3, 0), (3, 3), (0, 3)]
    Q = [(0, 0), (2, 0), (1, 1)]
    R = nfp(P, Q)
    plot_nfp(P, Q, R)
