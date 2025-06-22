"""
势能函数及导数计算
"""
import numpy as np

from geometry import *

class PotentialCalculator:

    def __init__(self, sources):
        self.sources = sources  # 场源坐标数组
        
    def potential(self, point):
        """
        计算点处的总势能值 (\\Phi)

        每个场源产生的势能为 \\Phi_k=\\frac{1}{r_k}

        总的势能为：\\Phi=\\sum\\frac{1}{r_k}
        """
        phi = 0.0

        for s in self.sources:
            r = np.linalg.norm(point - s)
            phi += 1 / r

        return phi
    

    def gradient(self, point):
        """
        计算势能函数的梯度 (\\nabla\\Phi)

        计算公式为：\\nabla\\Phi=\\sum-\\frac{(x-x_k,y-y_k)}{r_k^3}
        """
        g = np.zeros(2)
        for s in self.sources:
            r = point - s
            r_norm = np.linalg.norm(r)
            g -= r / (r_norm ** 3)

        return g
    

    def hessian(self, point):
        """
        计算Hessian矩阵 (可选，用于牛顿法)

        WARNING: 未实现
        """
        return np.zeros((2, 2))  # 对于此问题，Hessian矩阵通常不需要计算