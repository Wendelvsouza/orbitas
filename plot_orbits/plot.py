from orbits import Orbits


class plot:

    def apply_method(
        self,
    ):
        plt.plot(terra["pos_a_x"], terra["pos_a_y"], label="Terra")
        plt.plot(marte["pos_b_x"], marte["pos_b_y"], label="Marte")
        plt.title("Orbita")
        plt.xlabel("Posição(x em metros)")
        plt.ylabel("Posição(y em metros)")
        plt.legend()
        plt.savefig("test.jpeg")
