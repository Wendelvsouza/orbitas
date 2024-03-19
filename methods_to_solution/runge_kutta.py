from interfaces.methods import MethodsInterface


class Orbits_runge_kutta_method(MethodsInterface):

    def runge_kutta_method(self, constante, passo, marte, terra) -> list:

        for _ in range(358000):
            x_b0 = marte["x_b"]
            y_b0 = marte["y_b"]
            vx_b0 = marte["vx_b"]
            vy_b0 = marte["vy_b"]

            x_a0 = terra["x_a"]
            y_a0 = terra["y_a"]
            vx_a0 = terra["vx_a"]
            vy_a0 = terra["vy_a"]

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

            terra["vx_a"] += acelera_ax * passo["dt"] / 2
            terra["vy_a"] += acelera_ay * passo["dt"] / 2

            marte["vx_b"] += acelera_bx * passo["dt"] / 2
            marte["vy_b"] += acelera_by * passo["dt"] / 2

            print("cheguei aqui")

            terra["x_a"] += self.terra["vx_a"] * passo["dt"] / 2
            marte["x_b"] += self.marte["vx_b"] * passo["dt"] / 2

            terra["y_a"] += terra["vy_a"] * passo["dt"] / 2
            marte["y_b"] += marte["vy_b"] * passo["dt"] / 2

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

            terra["vx_a"] = vx_a0 + acelera_ax * passo["dt"]
            terra["vy_a"] = vy_a0 + acelera_ay * passo["dt"]

            marte["vx_b"] = vx_b0 + acelera_bx * passo["dt"]
            marte["vy_b"] = vy_b0 + acelera_by * passo["dt"]

            terra["x_a"] = x_a0 + terra["vx_a"] * passo["dt"]
            marte["x_b"] = x_b0 + marte["vx_b"] * passo["dt"]

            terra["y_a"] = y_a0 + terra["vy_a"] * passo["dt"]
            marte["y_b"] = y_b0 + marte["vy_b"] * passo["dt"]

            rungekutta = [
                terra["pos_a_x"],
                terra["pos_a_y"],
                marte["pos_b_x"],
                marte["pos_b_y"],
            ]
        return rungekutta

    def euler_method(self) -> None:
        pass
