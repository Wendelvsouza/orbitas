import matplotlib.pyplot as plt


class Plot:

    def graph_force_grav(
        self,
        terra_x,
        terra_y,
        marte_x,
        marte_y,
    ):
        plt.plot(terra_x, terra_y, label="Terra")
        plt.plot(marte_x, marte_y, label="Marte")
        plt.title("Orbita")
        plt.xlabel("Posição(x em metros)")
        plt.ylabel("Posição(y em metros)")
        plt.legend()
        plt.savefig("test.jpeg")
