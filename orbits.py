from typing import Type
from interfaces.methods import MethodsInterface
from plot_orbits.plot import Plot


class Orbits:
    def __init__(self) -> None:
        # Constante
        self.constante = {"GM": 9.96 * 10 ** (-7)}
        self.passo = {"dt_euler": 0.1, "dt_runge_kutta": 0.01}

        # Planeta terra
        self.terra = {
            "x_a": 0.1521,  # 10**2m
            "y_a": 0,
            "vx_a": 0,
            "vy_a": 2.530 * 10 ** (-3),  # 10**12 m/dia
            "Gm_a": 2.975 * 10 ** (-12),  # (10**12m)**3 / (dia)**2
            # Euler
            "pos_a_x": [],
            "pos_a_y": [],
            # RungeKutta
            "pos_c_x": [],
            "pos_c_y": [],
        }

        # Planeta marte
        self.marte = {
            "x_b": 0.24921,  # 10**12m
            "y_b": 0,
            "vx_b": 0,
            "vy_b": 2.08 * 10 ** (-3),  # 10**12 m/dia
            "Gm_b": 3.197 * 10 ** (-14),  # (10**12m)**3 / (dia)**2
            # Euler
            "pos_b_x": [],
            "pos_b_y": [],
            # Rungekutta
            "pos_d_x": [],
            "pos_d_y": [],
        }

    def apply_euler_method(self, gravitational_force: Type[MethodsInterface]):
        name = "euler"
        terra_x, terra_y, marte_x, marte_y = gravitational_force.euler_method(
            self.constante, self.passo, self.marte, self.terra
        )
        plot_euler = Plot()
        plot_euler.graph_force_grav(name, terra_x, terra_y, marte_x, marte_y)

    def apply_runge_kutta_method(self, gravitational_force: Type[MethodsInterface]):
        name = "runge_kutta"
        terra_x, terra_y, marte_x, marte_y = gravitational_force.runge_kutta_method(
            self.constante, self.passo, self.marte, self.terra
        )
        plot_runge = Plot()
        plot_runge.graph_force_grav(name, terra_x, terra_y, marte_x, marte_y)
