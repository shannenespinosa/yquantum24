from qiskit_optimization import QuadraticProgram
from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.primitives import Sampler

# quadratic programming
problem = QuadraticProgram()
problem.binary_var(name="x1")
problem.binary_var(name="x2")
problem.binary_var(name="x3")

# 2x_1x_2 + 3x_2x_3 − 4x_1x_3
problem.minimize(quadratic={("x1", "x2"): 2, ("x2", "x3"): 3, ("x1", "x3"): -4})

print(problem.prettyprint())

qaoa = QAOA(sampler=Sampler(), optimizer=COBYLA())
min_eigen_optimizer = MinimumEigenOptimizer(qaoa)

result = min_eigen_optimizer.solve(problem)
print(result)
