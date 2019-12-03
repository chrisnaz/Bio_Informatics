#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def topological_ordering(graph):
    graph = set(graph)
    ordering = []
    candidates = list({edge[0] for edge in graph} - {edge[1] for edge in graph})

    while len(candidates) != 0:
        ordering.append(candidates[0])
        temp_nodes = []

        for edge in filter(lambda e: e[0] == candidates[0], graph):
            graph.remove(edge)
            temp_nodes.append(edge[1])

        for node in temp_nodes:
            if node not in {edge[1] for edge in graph}:
                candidates.append(node)

        candidates = candidates[1:]
    return ordering

def longest_path(graph, edges, source, sink):
    top_order = topological_ordering(graph.keys())
    top_order = top_order[top_order.index(source)+1:top_order.index(sink)+1]
    S = {node:-100 for node in {edge[0] for edge in graph.keys()} | {edge[1] for edge in graph.keys()}}
    S[source] = 0
    backtrack = {node:None for node in top_order}

    for node in top_order:
        try:
            S[node], backtrack[node] = max(map(lambda e: [S[e[0]] + graph[e], e[0]], filter(lambda e: e[1] == node, graph.keys())), key=lambda p:p[0])

        except ValueError:
            pass

    path = [sink]
    while path[0] != source:
        path = [backtrack[path[0]]] + path
    return S[sink], path

def main():
    with open('Data/Longest_Path.txt') as input_data:
        source, sink = [int(input_data.readline()) for repeat in xrange(2)]
        edges, edge_weight = {}, {}

        for pair in [line.strip().split('->') for line in input_data.readlines()]:
            if int(pair[0]) not in edges:
                edges[int(pair[0])] = [int(pair[1].split(':')[0])]
            else:
                edges[int(pair[0])].append(int(pair[1].split(':')[0]))

            edge_weight[int(pair[0]), int(pair[1].split(':')[0])] = int(pair[1].split(':')[1])

    length, path = longest_path(edge_weight, edges, source, sink)
    lenth = str(length)
    path = '->'.join(map(str, path))

    print '\n'.join([lenth,path])
    with open('Data/Answer/Longest_Path.txt', 'w') as output_data:
        output_data.write('\n'.join([lenth,path]))


if __name__ == '__main__':

    main()
