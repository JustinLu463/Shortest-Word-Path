from queue import PriorityQueue


def build_graph(dictionary):
    graph = {word: [] for word in dictionary}

    for word in dictionary:
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]

                if next_word in dictionary and next_word != word:
                    graph[word].append(next_word)

    return graph

def dijkstras(graph, first, second):
    pq = PriorityQueue()
    pq.put((0, first, [first])) 
    visited = set()

    while not pq.empty():
        (cost, current_node, path) = pq.get()

        if current_node in visited:
            continue

        visited.add(current_node)
        if current_node == second:
            return cost, path

        for next_node in graph[current_node]:
            if next_node not in visited:
                pq.put((cost + 1, next_node, path + [next_node]))

    return float("inf"), []

dictionary = set(line.strip().lower() for line in open('Dict.txt') if line.strip())
graph = build_graph(dictionary)

while True:
    first_word = input("Enter the first word or type 'q' to quit: ").strip().lower()

    if first_word == 'q':
        break

    second_word = input("Enter the second word: ").strip().lower()
    if first_word == 'q' or second_word == 'q':
        break

    if len(first_word) != len(second_word):
        print("The words must be the same length.")
        continue

    if first_word not in dictionary or second_word not in dictionary:
        print("Both words must be in the dictionary.")
        continue

    cost, path = dijkstras(graph, first_word, second_word)
    if cost < float("inf"):
        print(f"The length of the shortest path is {cost}") 
        print(f"{' > '.join(path)}")
    else:
        print("There is no path")

