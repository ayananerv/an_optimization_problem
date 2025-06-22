import numpy as np
import matplotlib.pyplot as plt

def draw_polygon(polygon, fig, ax):
    # 为了闭合多边形，将第一个顶点追加到数组末尾
    closed_polygon = np.vstack([polygon, polygon[0]])

    
    # 2) 绘制每个顶点
    ax.plot(polygon[:, 0], polygon[:, 1], 'ro') # 'ro' 表示红色的圆点
    
    # 3) 绘制顶点连成的凸多边形
    ax.plot(closed_polygon[:, 0], closed_polygon[:, 1], 'b-') # 'b-' 表示蓝色的实线


def draw_points(points, fig, ax):
    for p in points:
        ax.plot(p[0], p[1], 'go') # 'go' 表示绿色的圆点

def draw_polygon_and_point(polygon, points):
    # 绘图设置
    fig, ax = plt.subplots()

    # 1) 绘制坐标系
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Convex Polygon")

    draw_polygon(polygon, fig, ax)
    draw_points(points, fig, ax)
    
    # plt.legend()
    plt.show()