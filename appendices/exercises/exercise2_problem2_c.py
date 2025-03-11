import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define parameters
M = 10
h = 1 / M
x = np.linspace(1, 2, M + 1)

# Define the system of equations for Newton's method
def system(u):
    equations = []
    # Interior points
    for i in range(1, M):
        eq = (u[i + 1] - 2 * u[i] + u[i - 1]) / h**2 + (2 / x[i]**3) * u[i]**3
        equations.append(eq)
    # Neumann condition at x_0
    equations.insert(0, 8 * (u[1] - u[0]) / h - 2 * u[0] - 1)
    # Dirichlet condition at x_M
    equations.append(u[M] - 2/3)
    return equations

# Initial guess
u0 = np.linspace(1, 2/3, M + 1)

# Solve the system using Newton's method
solution = fsolve(system, u0)

# Function to compute the solution for a given M
def solve_for_M(M):
    h = 1 / M
    x = np.linspace(1, 2, M + 1)
    
    def system(u):
        equations = []
        for i in range(1, M):
            eq = (u[i + 1] - 2 * u[i] + u[i - 1]) / h**2 + (2 / x[i]**3) * u[i]**3
            equations.append(eq)
        equations.insert(0, 8 * (u[1] - u[0]) / h - 2 * u[0] - 1)
        equations.append(u[M] - 2/3)
        return equations
    
    u0 = np.linspace(1, 2/3, M + 1)
    solution = fsolve(system, u0)
    return x, solution

# Compute solutions for different values of M
Ms = [10, 20, 40, 80]
solutions = {M: solve_for_M(M)[1] for M in Ms}

# Compute errors between successive refinements
errors = []
for i in range(len(Ms) - 1):
    M_fine = Ms[i + 1]
    M_coarse = Ms[i]
    h_fine = 1 / M_fine
    h_coarse = 1 / M_coarse
    
    # Interpolate coarse solution onto fine grid
    u_fine = solutions[M_fine]
    u_coarse = np.interp(np.linspace(1, 2, M_fine + 1), np.linspace(1, 2, M_coarse + 1), solutions[M_coarse])
    
    # Compute max norm error
    error = np.max(np.abs(u_fine - u_coarse))
    errors.append((M_coarse, M_fine, error))

# Estimate order of convergence
orders = [np.log(errors[i][2] / errors[i + 1][2]) / np.log(Ms[i + 1] / Ms[i]) for i in range(len(errors) - 1)]

# Create a figure with three subplots
plt.figure(figsize=(15, 5))

# First subplot: Initial solution for M=10
plt.subplot(131)
plt.plot(x, solution)
plt.scatter(x, solution, color='red', label='M = 10', zorder=5)
plt.title('Initial solution')
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.grid(True)

# Second subplot: Solutions for different M values
plt.subplot(132)
for M in Ms:
    x, solution = solve_for_M(M)
    plt.plot(x, solution, label=f'M = {M}')
plt.title('Solutions for different M')
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.grid(True)

# Third subplot: Error convergence
plt.subplot(133)
Ms = [10, 20, 40]
errors = [error[2] for error in errors]
plt.loglog(Ms, errors, marker='o')
plt.title('Error convergence')
plt.xlabel('M')
plt.ylabel('Error (log scale)')
plt.grid(True)

plt.tight_layout()
plt.show()

# Print numerical results
for i, error in enumerate(errors):
    print(f'M = {error[0]}, M = {error[1]}, error = {error[2]}, order = {orders[i]}')
    

