class DecisionTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


def build_decision_tree():
    root = DecisionTreeNode("LESS'")

    x0 = DecisionTreeNode("x[0]")
    antlr = DecisionTreeNode("ANTLR")
    one = DecisionTreeNode(1)

    root.add_child(x0)
    root.add_child(antlr)
    root.add_child(one)

    pony = DecisionTreeNode("PONY'")
    cpp = DecisionTreeNode("C++")
    mirah = DecisionTreeNode("MIRAH")
    three = DecisionTreeNode(3)

    pony.add_child(cpp)
    pony.add_child(mirah)
    pony.add_child(three)

    x2 = DecisionTreeNode("x[2]")
    x2_1965 = DecisionTreeNode(1965)

    x2.add_child(x2_1965)

    year_2005 = DecisionTreeNode(2005)
    x3 = DecisionTreeNode("x[3]")
    pony_cpp = DecisionTreeNode("PONY")
    cpp_2 = DecisionTreeNode("C++")
    four = DecisionTreeNode(4)

    year_2005.add_child(x3)
    year_2005.add_child(pony_cpp)
    year_2005.add_child(cpp_2)
    year_2005.add_child(four)

    year_1990 = DecisionTreeNode(1990)
    x2_1958 = DecisionTreeNode(1958)
    x2_2018 = DecisionTreeNode(2018)

    year_1990.add_child(x2)
    year_1990.add_child(x2_1958)
    year_1990.add_child(x2_2018)

    mirah_six = DecisionTreeNode("MIRAH'")
    six = DecisionTreeNode(6)

    mirah_six.add_child(six)

    year_2005_2 = DecisionTreeNode(2005)
    x2_9 = DecisionTreeNode(9)

    year_2005_2.add_child(x2)
    year_2005_2.add_child(x2_9)

    ten = DecisionTreeNode(10)

    # Adding all nodes to the root
    root.add_child(pony)
    root.add_child(x2)
    root.add_child(year_2005)
    root.add_child(year_1990)
    root.add_child(mirah_six)
    root.add_child(year_2005_2)
    root.add_child(ten)

    return root


# Example usage
decision_tree = build_decision_tree()
print(decision_tree)