import unittest


class StateMachineException(Exception):
    pass


class MooreMachine:
    def __init__(self):
        self.transitions = {
            't3': {
                'hike': [{
                    'next_state': 't2',
                    'cond': None,
                    'output': 'S0'
                }],
                'visit': [{
                    'next_state': 't7',
                    'cond': None,
                    'output': 'S1'
                }]
            },
            't2': {
                'spin': [{
                    'next_state': 't1',
                    'cond': None,
                    'output': 'S2'
                }]
            },
            't1': {
                'hike': [{
                    'next_state': 't6',
                    'cond': None,
                    'output': 'S2'
                }]
            },
            't6': {
                'hike': [{
                    'next_state': 't7',
                    'cond': None,
                    'output': 'S2'
                }],
                'swap': [{
                    'next_state': 't7',
                    'cond': None,
                    'output': 'S2'
                }]
            },
            't7': {
                'cast': [
                    {
                        'next_state': 't1',
                        'cond': {'var': 'c', 'value': 1},
                        'output': 'S2'
                    },
                    {
                        'next_state': 't0',
                        'cond': {'var': 'c', 'value': 0},
                        'output': 'S1'
                    }
                ],
                'swap': [{
                    'next_state': 't6',
                    'cond': None,
                    'output': 'S2'
                }]
            },
            't0': {
                'spin': [
                    {
                        'next_state': 't6',
                        'cond': {'var': 'x', 'value': 0},
                        'output': 'S0'
                    },
                    {
                        'next_state': 't4',
                        'cond': {'var': 'x', 'value': 1},
                        'output': 'S2'
                    }
                ]
            },
            't4': {
                'visit': [{
                    'next_state': 't5',
                    'cond': None,
                    'output': 'S1'
                }]
            },
            't5': {
                'hike': [{
                    'next_state': 't3',
                    'cond': None,
                    'output': 'S0'
                }]
            }
        }
        self.current_state = 't3'
        self.variables = {'c': None, 'x': None}
        self.executed_methods = set()

    def let_c(self, v):
        self.variables['c'] = v

    def let_x(self, v):
        self.variables['x'] = v

    def visit(self):
        return self._exec('visit')

    def cast(self):
        return self._exec('cast')

    def spin(self):
        return self._exec('spin')

    def hike(self):
        return self._exec('hike')

    def swap(self):
        return self._exec('swap')

    def link(self):
        raise StateMachineException('unknown')

    def open(self):
        raise StateMachineException('unknown')

    def close(self):
        raise StateMachineException('unknown')

    def seen_method(self, m):
        return m in self.executed_methods

    def has_max_out_edges(self):
        cur = sum(len(m) for m in self.transitions.get(
            self.current_state, {}).values())
        if not cur:
            return False
        max_edges = max(
            sum(len(m) for m in s.values())
            for s in self.transitions.values()
        )
        return cur == max_edges

    def has_path_to(self, target):
        from collections import deque

        visited = set()
        queue = deque([self.current_state])

        while queue:
            current = queue.popleft()

            if current == target:
                return True

            if current in visited:
                continue

            visited.add(current)
            queue.extend(self._get_unvisited_next_states(current, visited))

        return False

    def _get_unvisited_next_states(self, state, visited):
        next_states = []
        for transitions in self.transitions.get(state, {}).values():
            for transition in transitions:
                next_states.append(transition['next_state'])
        return [s for s in next_states if s not in visited]

    def _exec(self, method):
        if method not in self.transitions.get(self.current_state, {}):
            raise StateMachineException('unsupported')
        for t in self.transitions[self.current_state][method]:
            c = t.get('cond')
            if c is None or self.variables.get(c['var']) == c['value']:
                self.current_state = t['next_state']
                self.executed_methods.add(method)
                return t['output']
        raise StateMachineException('unsupported')

    def __getattr__(self, name):
        raise StateMachineException('unknown')


def main():
    return MooreMachine()


def test_execute_method_condition_branch():
    o = main()
    o.current_state = 't7'
    o.let_c(1)
    assert o.cast() == 'S2'


def test_execute_method_no_condition_branch():
    assert main().visit() == 'S1'


def test_execute_method_unsupported():
    o = main()
    o.current_state = 't1'
    try:
        o.visit()
    except StateMachineException as e:
        assert str(e) == 'unsupported'


def test_spin_method():
    o = main()
    try:
        o.spin()
    except StateMachineException as e:
        assert str(e) == 'unsupported'
    o.current_state = 't2'
    assert o.spin() == 'S2'


def test_spin_method_with_conditions():
    o = main()
    o.current_state = 't7'
    o.let_c(0)
    o.cast()
    o.let_x(0)
    assert o.spin() == 'S0'


def test_hike_method():
    o = main()
    assert o.hike() == 'S0'
    o.current_state = 't1'
    assert o.hike() == 'S2'


def test_hike_method_unsupported():
    o = main()
    o.current_state = 't4'
    try:
        o.hike()
    except StateMachineException as e:
        assert str(e) == 'unsupported'


def test_unsupported_due_to_unmet_conditions():
    o = main()
    o.current_state = 't0'
    o.variables['x'] = 2
    try:
        o.spin()
    except StateMachineException as e:
        assert str(e) == 'unsupported'


def test_unsupported_in_non_existent_state():
    o = main()
    o.current_state = 'non_existent_state'
    for m in ['visit', 'cast', 'spin', 'hike']:
        try:
            getattr(o, m)()
        except StateMachineException as e:
            assert str(e) == 'unsupported'


def test_seen_method():
    o = main()
    o.visit()
    assert o.seen_method('visit')


def test_has_max_out_edges():
    o = main()
    o.current_state = 't3'
    assert not o.has_max_out_edges()
    o.current_state = 'nonexistent'
    assert not o.has_max_out_edges()


def test_has_path_to():
    o = main()
    o.current_state = 't3'
    assert o.has_path_to('t4')
    assert not o.has_path_to('nonexistent')


def test_getattr_multiple_unknown_methods():
    o = main()
    for method in ['race', 'chain', 'sort']:
        try:
            getattr(o, method)()
        except StateMachineException as e:
            assert str(e) == 'unknown'


def test_swap_unsupported_state():
    o = main()
    o.current_state = 't3'
    try:
        o.swap()
    except StateMachineException as e:
        assert str(e) == 'unsupported'


def test_cast_with_unmet_condition():
    o = main()
    o.current_state = 't7'
    o.let_c(2)
    try:
        o.cast()
    except StateMachineException as e:
        assert str(e) == 'unsupported'


def test_link_open_close_methods():
    o = main()
    for method in ['link', 'open', 'close']:
        try:
            getattr(o, method)()
        except StateMachineException as e:
            assert str(e) == 'unknown'


def test():
    test_execute_method_condition_branch()
    test_execute_method_no_condition_branch()
    test_execute_method_unsupported()
    test_spin_method()
    test_spin_method_with_conditions()
    test_hike_method()
    test_hike_method_unsupported()
    test_unsupported_due_to_unmet_conditions()
    test_unsupported_in_non_existent_state()
    test_seen_method()
    test_has_max_out_edges()
    test_has_path_to()
    test_getattr_multiple_unknown_methods()
    test_swap_unsupported_state()
    test_cast_with_unmet_condition()
    test_link_open_close_methods()
