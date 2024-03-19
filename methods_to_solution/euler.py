from interfaces.methods import MethodsInterface
from plot_orbits.plot import Plot


class Orbits_euler_method(MethodsInterface):

    def euler_method(self, constante, passo, marte, terra) -> list:
        for i in range(19000):
            terra["pos_a_x"].append(terra["x_a"])
            terra["pos_a_y"].append(terra["y_a"])

            marte["pos_b_x"].append(marte["x_b"])
            marte["pos_b_y"].append(marte["y_b"])

            div_b = (marte["x_b"] ** 2 + marte["y_b"] ** 2) ** (3 / 2)
            div_a = (terra["x_a"] ** 2 + terra["y_a"] ** 2) ** (3 / 2)
            div_a_b = (
                (marte["x_b"] - terra["x_a"]) ** 2 + (marte["y_b"] - terra["y_a"]) ** 2
            ) ** (3 / 2)

            acelera_ax = (
                -constante["GM"] * terra["x_a"] / div_a
                + terra["Gm_a"] * (marte["x_b"] - terra["x_a"]) / div_a_b
            )
            acelera_ay = (
                -constante["GM"] * terra["y_a"] / div_a
                + terra["Gm_a"] * (marte["y_b"] - terra["y_a"]) / div_a_b
            )

            acelera_bx = (
                -constante["GM"] * marte["x_b"] / div_b
                - marte["Gm_b"] * (marte["x_b"] - terra["x_a"]) / div_a_b
            )
            acelera_by = (
                -constante["GM"] * marte["y_b"] / div_b
                - marte["Gm_b"] * (marte["y_b"] - terra["y_a"]) / div_a_b
            )

            terra["vx_a"] += acelera_ax * passo["dt_euler"]
            terra["vy_a"] += acelera_ay * passo["dt_euler"]

            marte["vx_b"] += acelera_bx * passo["dt_euler"]
            marte["vy_b"] += acelera_by * passo["dt_euler"]

            terra["x_a"] += terra["vx_a"] * passo["dt_euler"]
            terra["y_a"] += terra["vy_a"] * passo["dt_euler"]

            marte["x_b"] += marte["vx_b"] * passo["dt_euler"]
            marte["y_b"] += marte["vy_b"] * passo["dt_euler"]

        return (
            terra["pos_a_x"],
            terra["pos_a_y"],
            marte["pos_b_x"],
            marte["pos_b_y"],
        )

    def runge_kutta_method(self) -> list:
        pass
