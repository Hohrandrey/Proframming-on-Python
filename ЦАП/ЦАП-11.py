class StateMachineException(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.current_state = 'S0'
        self.visited_methods = set()
        self.variables = {'x': None, 'c': None}
        self.graph = {
            'S0': {'hike': 'S0', 'spin': 'S2', 'visit': 'S1'},
            'S1': {
                'hike': 'S2',
                'cast': ('S2', lambda: self.variables['c'] == 1)
            },
            'S2': {
                'spin': [
                    ('S0', lambda: self.variables['x'] == 0),
                    ('S2', lambda: self.variables['x'] == 1)
                ],
                'cast': 'S1',
                'swap': 'S2',
                'visit': 'S1'
            }
        }

    def hike(self):
        self.visited_methods.add('hike')
        if self.current_state == 'S0':
            return 'S0'
        elif self.current_state == 'S1':
            self.current_state = 'S2'
        elif self.current_state == 'S2':
            raise StateMachineException('unsupported')
        else:
            raise StateMachineException('unknown')
        return self.current_state

    def spin(self):
        self.visited_methods.add('spin')
        if self.current_state == 'S0':
            self.current_state = 'S2'
            return 'S2'
        elif self.current_state == 'S2':
            if self.variables['x'] == 0:
                self.current_state = 'S0'
            elif self.variables['x'] == 1:
                return 'S2'
            else:
                raise StateMachineException('unsupported')
        else:
            raise StateMachineException('unsupported')
        return self.current_state

    def visit(self):
        self.visited_methods.add('visit')
        if self.current_state == 'S0':
            self.current_state = 'S1'
        elif self.current_state == 'S2':
            self.current_state = 'S1'
        else:
            raise StateMachineException('unsupported')
        return self.current_state

    def cast(self):
        self.visited_methods.add('cast')
        if self.current_state == 'S1':
            if self.variables['c'] == 1:
                self.current_state = 'S2'
            else:
                raise StateMachineException('unsupported')
        elif self.current_state == 'S2':
            self.current_state = 'S1'
        else:
            raise StateMachineException('unsupported')
        return self.current_state

    def swap(self):
        self.visited_methods.add('swap')
        if self.current_state == 'S2':
            return 'S2'
        else:
            raise StateMachineException('unsupported')

    def let_x(self, value):
        self.variables['x'] = value

    def let_c(self, value):
        self.variables['c'] = value

    def seen_method(self, method_name):
        return method_name in self.visited_methods

    def _get_next_states(self, state):
        next_states = []
        for transition in self.graph.get(state, {}).values():
            if isinstance(transition, tuple):
                next_states.append(transition[0])
            elif isinstance(transition, list):
                next_states.extend(ns for ns, _ in transition)
            else:
                next_states.append(transition)
        return next_states

    def has_path_to(self, target_state):
        mapping = {
            't0': 'S0', 't1': 'S1', 't2': 'S2',
            't3': 'S0', 't4': 'S1', 't5': 'S1',
            't6': 'S2', 't7': 'S0'
        }
        target = mapping.get(target_state, target_state)
        if self.current_state == target:
            return True
        visited = set()
        queue = [self.current_state]
        while queue:
            state = queue.pop(0)
            if state in visited:
                continue
            visited.add(state)
            next_states = self._get_next_states(state)
            if target in next_states:
                return True
            queue.extend(ns for ns in next_states if ns not in visited)
        return False

    def has_max_out_edges(self):
        max_edges = max(len(v) for v in self.graph.values())
        return len(self.graph.get(self.current_state, {})) == max_edges

    def link(self):
        raise StateMachineException('unknown')

    def close(self):
        raise StateMachineException('unknown')


def _test_hike(sm):
    assert sm.hike() == 'S0'
    sm.current_state = 'S1'
    assert sm.hike() == 'S2'
    sm.current_state = 'S2'
    try:
        sm.hike()
        assert False
    except StateMachineException as e:
        assert str(e) == 'unsupported'
    sm.current_state = 'invalid'
    try:
        sm.hike()
        assert False
    except StateMachineException as e:
        assert str(e) == 'unknown'


def _test_spin(sm):
    sm.current_state = 'S0'
    assert sm.spin() == 'S2'
    sm.let_x(0)
    assert sm.spin() == 'S0'
    sm.current_state = 'S2'
    sm.let_x(1)
    assert sm.spin() == 'S2'
    sm.let_x(2)
    try:
        sm.spin()
        assert False
    except StateMachineException as e:
        assert str(e) == 'unsupported'
    sm.current_state = 'S1'
    try:
        sm.spin()
        assert False
    except StateMachineException as e:
        assert str(e) == 'unsupported'


def _test_visit(sm):
    sm.current_state = 'S0'
    assert sm.visit() == 'S1'
    sm.current_state = 'S2'
    assert sm.visit() == 'S1'
    sm.current_state = 'S1'
    try:
        sm.visit()
        assert False
    except StateMachineException as e:
        assert str(e) == 'unsupported'


def _test_cast(sm):
    sm.current_state = 'S1'
    sm.let_c(1)
    assert sm.cast() == 'S2'
    sm.current_state = 'S1'
    sm.let_c(0)
    try:
        sm.cast()
        assert False
    except StateMachineException as e:
        assert str(e) == 'unsupported'
    sm.current_state = 'S2'
    assert sm.cast() == 'S1'
    sm.current_state = 'S0'
    try:
        sm.cast()
        assert False
    except StateMachineException as e:
        assert str(e) == 'unsupported'


def _test_swap(sm):
    sm.current_state = 'S2'
    assert sm.swap() == 'S2'
    sm.current_state = 'S0'
    try:
        sm.swap()
        assert False
    except StateMachineException as e:
        assert str(e) == 'unsupported'
    sm.current_state = 'S1'
    try:
        sm.swap()
        assert False
    except StateMachineException as e:
        assert str(e) == 'unsupported'


def _test_vars(sm):
    sm.let_x(5)
    assert sm.variables['x'] == 5
    sm.let_c(2)
    assert sm.variables['c'] == 2
    assert sm.seen_method('cast')
    assert sm.seen_method('swap')
    assert not sm.seen_method('unknown')


def _test_paths(sm):
    sm.current_state = 'S0'
    assert sm.has_path_to('S2')
    assert not sm.has_path_to('invalid')
    sm.current_state = 'S2'
    assert sm.has_max_out_edges()
    sm.current_state = 'S0'
    assert not sm.has_max_out_edges()
    sm.current_state = 'S1'
    assert not sm.has_max_out_edges()


def _test_unknown(sm):
    try:
        sm.link()
        assert False
    except StateMachineException as e:
        assert str(e) == 'unknown'
    try:
        sm.close()
        assert False
    except StateMachineException as e:
        assert str(e) == 'unknown'


def _test_mappings(sm):
    for t in ['t0', 't1', 't2', 't3', 't4', 't5', 't6', 't7']:
        sm.current_state = 'S0'
        assert sm.has_path_to(t)


def _test_next_states_logic(sm):
    orig = sm.graph.copy()
    sm.graph["S1"]["tmp"] = ("S0", lambda: True)
    sm.graph["S0"]["tmp"] = [("S1", lambda: True), ("S2", lambda: False)]
    assert "S0" in sm._get_next_states("S1")
    assert "S1" in sm._get_next_states("S0")
    assert "S2" in sm._get_next_states("S0")
    sm.graph = orig


def _test_max_edges(sm):
    orig = sm.graph.copy()
    sm.graph["S3"] = {str(i): i for i in range(5)}
    sm.current_state = "S3"
    assert sm.has_max_out_edges()
    sm.graph = orig


def _test_lambdas(sm):
    sm.let_c(1)
    assert sm.graph["S1"]["cast"][1]()
    sm.let_c(0)
    assert not sm.graph["S1"]["cast"][1]()
    sm.let_x(0)
    assert sm.graph["S2"]["spin"][0][1]()
    sm.let_x(1)
    assert sm.graph["S2"]["spin"][1][1]()


def _test_spin_edge(sm):
    sm.current_state = "S0"
    assert sm.spin() == "S2"
    sm.current_state = "S1"
    try:
        sm.spin()
        assert False
    except StateMachineException as e:
        assert "unsupported" in str(e)


def _test_hike_edge(sm):
    sm.current_state = "S3"
    try:
        sm.hike()
        assert False
    except StateMachineException as e:
        assert "unknown" in str(e)


def test():
    sm = StateMachine()
    assert sm.current_state == 'S0'
    assert not sm.has_max_out_edges()
    assert sm.has_path_to('S1')
    assert not sm.seen_method('visit')
    _test_hike(sm)
    _test_spin(sm)
    _test_visit(sm)
    _test_cast(sm)
    _test_swap(sm)
    _test_vars(sm)
    _test_paths(sm)
    _test_unknown(sm)
    _test_mappings(sm)
    _test_next_states_logic(sm)
    _test_max_edges(sm)
    _test_lambdas(sm)
    _test_spin_edge(sm)
    _test_hike_edge(sm)


def main():
    return StateMachine()


if __name__ == "__main__":
    test()
