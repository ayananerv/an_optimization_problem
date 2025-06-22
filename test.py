import numpy as np

from geometry import *
from visualization import draw_polygon_and_point
from optimizer import GradientDescentOptimizer

if __name__ == "__main__":
    # 测试验证和排序点集
    points = [
        np.array([0, 0]), 
        np.array([0, 1]), 
        np.array([1, 1]), 
        np.array([1, 0]),
    ]

    polygon = validate_and_sort_points(points)

    print("该多边形输入为有效输入")

    valid_test_point = np.array([0.5, 0.5])
    invalid_test_point = np.array([2, 2])
    to_optimize_point = np.array([0.3, 0.66])

    assert is_point_in_polygon(valid_test_point, polygon), "点 (0.5, 0.5) 应在凸多边形内"
    assert not is_point_in_polygon(invalid_test_point, polygon), "点 (2, 2) 不应在凸多边形内"
    
    opt = GradientDescentOptimizer(polygon)
    path_record, phi_record = opt.gradient_descent(to_optimize_point)

    print(f"起点: {path_record[0]}, 最优点: {path_record[-1]}")

    draw_polygon_and_point(polygon, path_record[::len(path_record) // 10])
