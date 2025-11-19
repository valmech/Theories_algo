import sys

INF = sys.maxsize // 2 

def initialize_distance_matrix(num_nodes, graph_data, is_undirected=True):
    D = [[INF] * num_nodes for _ in range(num_nodes)]

    for i in range(num_nodes):
        D[i][i] = 0

    for u, v, weight in graph_data:
        u_idx, v_idx = u - 1, v - 1

        D[u_idx][v_idx] = weight

        if is_undirected:
            D[v_idx][u_idx] = weight

    return D

def floyd_warshall(D_initial):
    n = len(D_initial)
    D = [row[:] for row in D_initial]

    for k in range(n):
        for i in range(n):
            for j in range(n):

                if D[i][k] != INF and D[k][j] != INF:
                    new_distance = D[i][k] + D[k][j]

                    if D[i][j] > new_distance:
                        D[i][j] = new_distance

    return D

def get_graph_input_floyd():
    print("--- Введення графа для алгоритму Флойда ---")
    
    while True:
        try:
            num_nodes = int(input("Введіть кількість вершин (N): "))
            if num_nodes <= 0:
                raise ValueError
            break
        except ValueError:
            print("Будь ласка, введіть коректне додатне число.")

    graph_data = []
    print("\nВведіть ребра та їх ваги (початкова_вершина кінцева_вершина вага).")
    print("Програма АВТОМАТИЧНО зробить граф неорієнтованим.")
    print("Введіть 'готово', коли закінчите.")
    
    while True:
        line = input("Ребро (наприклад, 1 2 5) або 'готово': ").strip()
        if line.lower() == 'готово':
            break

        try:
            u, v, weight = map(int, line.split())

            if not (1 <= u <= num_nodes and 1 <= v <= num_nodes):
                print(f"Помилка: Вершини мають бути в межах 1-{num_nodes}.")
                continue

            graph_data.append((u, v, weight))

        except ValueError:
            print("Некоректний формат. Будь ласка, введіть три числа.")
        except Exception:
            print("Виникла помилка під час введення.")

    return num_nodes, graph_data

def display_matrix(D):
    n = len(D)
    
    print("\n\t" + "\t".join(str(i + 1) for i in range(n)))
    print("-" * (n * 8))
    
    for i in range(n):
        row_str = f"{i + 1}"
        for j in range(n):
            val = D[i][j]
            if val >= INF:
                row_str += "\t\u221E"
            else:
                row_str += f"\t{int(val)}"
        print(row_str)

def main_floyd():
    num_nodes, graph_data = get_graph_input_floyd()
    
    if num_nodes == 0:
        print("Граф порожній. Завершення роботи.")
        return

    D0 = initialize_distance_matrix(num_nodes, graph_data, is_undirected=True)
    
    print("\n--- Початкова матриця D(0) (Автоматично зроблено неорієнтованою) ---")
    display_matrix(D0)
    
    final_distance_matrix = floyd_warshall(D0)
    
    print("\n--- Фінальна матриця відстаней D(N) ---")
    display_matrix(final_distance_matrix)

if __name__ == "__main__":
    main_floyd()
