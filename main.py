import networkx as nx
import matplotlib.pyplot as plt
import random
import sys
import re
from time import sleep

# ---------------

class Graph:
    def __init__(self):
        self.graph = nx.DiGraph()

    # 程序读入文本数据，进行分析，将其转化为有向图

    def function1(self, file_name: str):
        with open(file_name, 'r', encoding='utf-8') as input_file:
            content = input_file.read()
            content = ''.join(ch for ch in content if ch.isalpha() or ch in [' ', '\n', '\t'])
            content = content.lower()
            content = re.split('[ \n\t]', content)
            content = [item for item in content if item != '']

        node_list = content
        edge_dict = {}
        for i in range(len(node_list) - 1):
            if (node_list[i], node_list[i + 1]) in edge_dict:
                edge_dict[(node_list[i], node_list[i + 1])] += 1
            else:
                edge_dict[(node_list[i], node_list[i + 1])] = 1

        for item in node_list:
            self.graph.add_node(item)
        for key, value in edge_dict.items():
            self.graph.add_edge(key[0], key[1], weight=value)

    def function2(self):
        pos = nx.spring_layout(self.graph)
        weights = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, font_weight='bold')

        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=weights, font_weight='bold')

        plt.show()

    def function3(self, node1, node2, show: bool) -> list:
        ans = []
        edges = self.graph.edges()
        neighbors = self.graph.neighbors(node1)
        for neighbor in neighbors:
            if node2 in self.graph.neighbors(neighbor):
                ans.append(neighbor)

        if show is True:
            for item in ans:
                print(item)

        return ans

    def function4(self, content):
        content = ''.join(ch for ch in content if ch.isalpha() or ch in [' ', '\n', '\t'])
        # content = content.lower()
        content = re.split('[ \n\t]', content)
        content = [item for item in content if item != '']

        nodes = self.graph.nodes

        for i in range(len(content) - 1):
            if content[i] not in nodes or content[i + 1] not in nodes:
                continue
            result = self.function3(content[i], content[i + 1], show=False)
            if result:
                word = random.choice(result)
                content.insert(i + 1, word)

        content = ' '.join(content)
        print(content)

    def function5(self, src_node: str, dst_node: str = None):
        nodes = self.graph.nodes()
        if src_node not in nodes:
            print(f"\'{src_node}\' not in the graph")
            return

        if dst_node is not None:
            if dst_node not in nodes:
                print(f"\'{dst_node}\' not in the graph")
                return
            paths = nx.all_shortest_paths(self.graph, src_node, dst_node)
            for path in paths:
                for index, node in enumerate(path):
                    print(node, end='')
                    if index < len(path) - 1:
                        print('->', end='')
                print()
        else:
            for dst in self.graph.nodes:
                if dst != src_node:
                    paths = nx.all_shortest_paths(self.graph, src_node, dst)
                    print(dst)
                    for path in paths:
                        for index, node in enumerate(path):
                            print(node, end='')
                            if index < len(path) - 1:
                                print('->', end='')
                        print()

    def function6(self, start_node: str = None):
        nodes = self.graph.nodes
        if start_node is not None:
            if start_node not in nodes:
                print(f"\'{start_node}\' not in the graph")
            node = start_node
        else:
            node = random.choice(nodes)

        passed_edge = []

        while True:
            if not list(self.graph.successors(node)):
                print(f"\'{node}\' does not have a successor")
                return
            print(node)
            successors = list(self.graph.successors(node))
            successor = random.choice(successors)
            edge = (node, successor)
            if edge in passed_edge:
                print(f'Edge {edge} already passed through')
                return
            passed_edge.append(edge)
            node = successor
            sleep(0.2)


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print("Usage: python main.py <file_name>")
        exit()

    G = Graph()
    G.function1(args[1])
    # G.function2()

    # G.function3('to', 'to', show=True)

    # G.function4("Seek to explore new and exciting synergies")

    # G.function5('to', 'and')
    # G.function5('to')
    # G.function5('to', 'to')
    # G.function6('to')
    # modify

    # B1 modify
