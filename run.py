from methods_to_solution.euler import Orbits_euler_method
from methods_to_solution.runge_kutta import Orbits_runge_kutta_method
from orbits import Orbits


orbits = Orbits()

orbits_euler_method = Orbits_euler_method()
orbits.apply_euler_method(orbits_euler_method)

orbits_runge_kutta_method = Orbits_runge_kutta_method()
orbits.apply_runge_kutta_method(orbits_runge_kutta_method)
