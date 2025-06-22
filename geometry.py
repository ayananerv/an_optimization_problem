"""
凸多边形几何操作和验证
"""
import numpy as np
from scipy.spatial import ConvexHull

def validate_and_sort_points(points):
    """
    验证输入点集是否为有效凸多边形并排序
    返回逆时针排序的凸包点
    """
    if len(points) < 3:
        raise ValueError("至少需要三个点来定义一个凸多边形")

    unique_points = np.unique(points, axis=0)
    if len(unique_points) < len(points):
        raise ValueError("输入点集中存在重复点")
    
    try:
        hull = ConvexHull(unique_points)
    except Exception as e:
        raise ValueError(f"无法计算凸包，可能点集不满足凸多边形条件: {e}")
    
    if len(hull.vertices) != len(unique_points):
        raise ValueError("输入点集不是凸多边形")
    
    return unique_points[hull.vertices]
    

def is_point_in_polygon(point, polygon) -> bool:
    """
    判断点是否在凸多边形内部
    使用射线法或向量叉积法

    在这里使用向量叉积法
    因为该凸多边形是逆时针排布的
    所以判断点是否在边的左侧
    
    时间复杂度：O(n)，其中 n 是多边形的顶点数
    """
    num_vertices = len(polygon)

    for i in range(num_vertices):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % num_vertices]
        
        edge_vec = p2 - p1
        point_vec = point - p1

        # 计算2D向量的叉积 (z分量)
        # cross_product = edge_vec x point_vec
        # cross_product > 0: point在向量左侧
        # cross_product < 0: point在向量右侧
        # cross_product = 0: point在向量所在的直线上
        cross_product = edge_vec[0] * point_vec[1] - edge_vec[1] * point_vec[0]
        if cross_product < 0:
            return False
        
    return True
    
    
def project_to_polygon(point, polygon):
    """
    将点投影到凸多边形边界上
    当优化点移出多边形时使用

    WARNING: 该方法未实现
    """
    if is_point_in_polygon(point, polygon):
        return point
    
    return point

    

def distance(p1, p2):
    return np.hypot(p1[0] - p2[0], p1[1] - p2[1])
