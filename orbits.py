from typing import Type
from interfaces.methods import MethodsInterface
from plot_orbits.plot import Plot


class Orbits:
    def __init__(self) -> None:
        # Constante
        self.constante = {"GM": 9.96 * 10 ** (-7)}
        self.passo = {"dt": 0.1}

        # Planeta terra
        self.terra = {
            "x_a": 0.1521,  # 10**2m
            "y_a": 0,
            "vx_a": 0,
            "vy_a": 2.530 * 10 ** (-3),  # 10**12 m/dia
            "Gm_a": 2.975 * 10 ** (-12),  # (10**12m)**3 / (dia)**2
            "pos_a_x": [],
            "pos_a_y": [],
        }

        # Planeta marte
        self.marte = {
            "x_b": 0.24921,  # 10**12m
            "y_b": 0,
            "vx_b": 0,
            "vy_b": 2.08 * 10 ** (-3),  # 10**12 m/dia
            "Gm_b": 3.197 * 10 ** (-14),  # (10**12m)**3 / (dia)**2
            "pos_b_x": [],
            "pos_b_y": [],
        }

    def apply_euler_method(self, gravitational_force: Type[MethodsInterface]):
        gravitational_force.euler_method(
            self.constante, self.passo, self.marte, self.terra
        )

    def apply_runge_kutta_method(self, gravitational_force: Type[MethodsInterface]):
        gravitational_force.runge_kutta_method(
            self.constante, self.passo, self.marte, self.terra
        )
        # plot = Plot()

        # plot.graph_force_grav(
        #     gravitational_force.runge_kutta_method(
        #         self.constante, self.passo, self.marte, self.terra
        #     )
        # )
