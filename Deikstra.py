import heapq

def dijkstra(graph, start_node):
    
    dist = {node: float('inf') for node in graph}
    pred = {node: None for node in graph}
    
    dist[start_node] = 0  
    
    pq = [(0, start_node)]  

    while pq:
        current_distance, u = heapq.heappop(pq)
        if current_distance > dist[u]:
            continue
        for v, weight in graph[u].items():
            distance = current_distance + weight
            if distance < dist[v]:
                dist[v] = distance  
                pred[v] = u         
                heapq.heappush(pq, (distance, v)) 

    return dist, pred

def get_graph_input():
    """Запитує користувача про граф і повертає його у вигляді словника."""
    print("Введення даних для графа:")
    
    while True:
        try:
            num_nodes = int(input("Введіть кількість вершин у графі: "))
            if num_nodes <= 0:
                raise ValueError
            break
        except ValueError:
            print("Будь ласка, введіть коректне додатне число.")
    graph = {str(i): {} for i in range(1, num_nodes + 1)}
    
    print("\nВведіть ребра та їх ваги (наприклад, 1 2 3 означає ребро з 1 до 2 з вагою 3).")
    print("Введіть 'готово', коли закінчите.")
 
    while True:
        try:
            line = input(f"Ребро (початкова вершина, кінцева вершина, вага) або 'готово': ").strip()
            if line.lower() == 'готово':
                break

            parts = line.split()
            if len(parts) != 3:
                print("Некоректний формат. Спробуйте ще раз (наприклад, 1 2 3).")
                continue

            u, v, weight = parts
            weight = int(weight)

            if u not in graph or v not in graph:
                print("Одна з вершин не існує. Переконайтеся, що вершини в межах 1-{}".format(num_nodes))
                continue

            if weight < 0:
                print("Увага: Алгоритм Дейкстри вимагає невід'ємних ваг. Ребро проігноровано.")
                continue

            graph[u][v] = weight
            graph[v][u] = weight 

        except ValueError:
            print("Вага має бути цілим числом. Спробуйте ще раз.")
        except Exception as e:
            print(f"Виникла помилка: {e}")

    return graph

def get_start_node(graph):
    """Запитує користувача про стартову вершину."""
    nodes = list(graph.keys())
    while True:
        start_node = input(f"Введіть стартову вершину (з доступних: {', '.join(nodes)}): ").strip()
        if start_node in graph:
            return start_node
        else:
           print("Некоректна стартова вершина")

def main():
    """Запускає процес введення графа, виконання алгоритму Дейкстри та відображення результатів."""
    
    graph = get_graph_input()
    if not graph:
        print("Граф порожній. Завершення роботи.")
        return

    start_node = get_start_node(graph)
    
    print("\n--- Виконання алгоритму Дейкстри ---")
    final_dist, final_pred = dijkstra(graph, start_node)
    
    print("\n Результати:")
    print("---------------------------------------------------------")
    print(f"| Вершина | Найкоротша відстань від {start_node} | Шлях |")
    print("---------------------------------------------------------")
    
    for node in sorted(final_dist.keys(), key=lambda x: int(x)):
        distance = final_dist[node]
        if distance == float('inf'):
            print(f"| {node:<7} | {'∞ (недосяжна)':<29} | {'-':<4} |")
        else:
            path = []
            curr = node
            while curr is not None:
                path.append(curr)
                curr = final_pred.get(curr)

            path.reverse()
            path_str = " -> ".join(path)

            print(f"| {node:<7} | {distance:<29} | {path_str:<4} |")

    print("---------------------------------------------------------")

if __name__ == "__main__":
    main()

