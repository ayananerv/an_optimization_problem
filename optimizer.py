import numpy as np

from potential import PotentialCalculator
from geometry import *

class GradientDescentOptimizer:
    """
    梯度下降优化器
    用于最小化势能函数
    """

    def __init__(self, polygon):
        self.polygon = polygon  # 凸多边形顶点
        self.potential_calculator = PotentialCalculator(polygon)  # 势能计算器

    
    def gradient_descent(self, start_point, error=1e-6, max_iter=100):
        path_record = [start_point.copy()]
        phi_record = [self.potential_calculator.potential(start_point)]
        current_point = start_point.copy()
        lr = 0.01

        for i in range(max_iter):
            # Step 1: Calculate the potential (phi)
            phi = self.potential_calculator.potential(current_point)
            
            # Step 2: Calculate the gradient (g)
            g = self.potential_calculator.gradient(current_point)

            # Step 3: Calculate the norm of the gradient
            g_norm = np.linalg.norm(g)

            if i % (max_iter / 10) == 0:
                print(f"Iteration {i}: Current point = {current_point}, Potential = {phi}, Gradient = {g}, Norm = {g_norm}")

            # Step 4: Check convergence
            if g_norm < error:
                print(f"Converged after {i} iterations.")
                print(f"Final point: {current_point}, Potential: {phi}, Gradient: {g}, Norm: {g_norm}")
                break

            # Step 5: Calculate the new point
            new_point = current_point - lr * (g / g_norm)
            new_phi = self.potential_calculator.potential(new_point)

            # Step 6: Deal with boundary conditions
            if not is_point_in_polygon(new_point, self.polygon):
                print(f"Point {new_point} is outside the polygon, adjusting the learning rate to try again.")
                lr *= 0.5
                continue

            # Step 7: Deal with negative optimization
            if new_phi >= phi:
                print(f"Potential did not decrease, adjusting the learning rate to try again.")
                lr *= 0.5
                continue

            # Step 8: Update the current point
            path_record.append(new_point.copy())
            phi_record.append(new_phi)
            current_point = new_point.copy()
            lr = min(lr * 1.5, 0.01)
        
        return path_record, phi_record
