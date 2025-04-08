from graphviz import Digraph


def draw(vertices, edges):
    dot = Digraph()
    for v_id, v_label in vertices:
        dot.node(str(v_id), v_label)
    for src, dst in edges:
        dot.edge(str(src), str(dst))
    dot.render('graph', format='png', view=True)

draw([(1, 'v1'), (2, 'v2')], [(1, 2), (2, 3), (2, 2)])