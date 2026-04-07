import heapq

# -------------------------- 1. 罗马尼亚地图数据 --------------------------
# 实际路径代价（相邻城市间的距离，无向图）
romania_map = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

# 启发函数 h(n)：各城市到 Bucharest 的直线距离（A* 核心，保证最优解）
heuristic = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

# -------------------------- 2. A* 算法核心 --------------------------
def a_star_romania(start, goal='Bucharest'):
    # 优先队列：(f(n), 当前城市, 已走路径, 已走代价)
    open_heap = []
    # 初始 f(n) = g(0) + h(n)
    initial_h = heuristic[start]
    heapq.heappush(open_heap, (initial_h, start, [start], 0))

    visited = {start: 0}

    while open_heap:
        # 取出 f(n) 最小的节点
        f_current, current_city, path, g_current = heapq.heappop(open_heap)

        # 到达目标，直接返回最优解
        if current_city == goal:
            return path, g_current

        # 遍历所有邻居
        for neighbor, cost in romania_map[current_city]:
            g_new = g_current + cost  # 新的实际代价 g(n)
            h_new = heuristic[neighbor]  # 启发代价 h(n)
            f_new = g_new + h_new  # 总代价 f(n)

            # 未访问过 或 找到更优路径
            if neighbor not in visited or g_new < visited[neighbor]:
                visited[neighbor] = g_new
                new_path = path + [neighbor]
                heapq.heappush(open_heap, (f_new, neighbor, new_path, g_new))

if __name__ == '__main__':
    start_city = "Arad"
    best_path, total_cost = a_star_romania(start_city)

    if best_path:
        print(f" 从 {start_city} 到 Bucharest 的最优路径：")
        print(" → ".join(best_path))
        print(f" 总路径代价：{total_cost}")
        print(f"  朱显忠 2023213081")
    else:
        print(f" 未找到路径")
