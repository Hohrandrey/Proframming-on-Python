import unittest


class StateMachineException(Exception):
    pass


class MooreMachine:
    def __init__(self):
        self.transitions = {
            't3': {
                'hike': [{'next_state': 't2', 'cond': None, 'output': 'S0'}],
                'visit': [{'next_state': 't7', 'cond': None, 'output': 'S1'}]
            },
            't2': {
                'spin': [{'next_state': 't1', 'cond': None, 'output': 'S2'}]
            },
            't1': {
                'hike': [{'next_state': 't6', 'cond': None, 'output': 'S2'}]
            },
            't6': {
                'hike': [{'next_state': 't7', 'cond': None, 'output': 'S2'}],
                'swap': [{'next_state': 't7', 'cond': None, 'output': 'S2'}]
            },
            't7': {
                'cast': [
                    {'next_state': 't1', 'cond': {'var': 'c', 'value': 1}, 'output': 'S2'},
                    {'next_state': 't0', 'cond': {'var': 'c', 'value': 0}, 'output': 'S1'}
                ],
                'swap': [{'next_state': 't6', 'cond': None, 'output': 'S2'}]
            },
            't0': {
                'spin': [
                    {'next_state': 't6', 'cond': {'var': 'x', 'value': 0}, 'output': 'S0'},
                    {'next_state': 't4', 'cond': {'var': 'x', 'value': 1}, 'output': 'S2'}
                ]
            },
            't4': {
                'visit': [{'next_state': 't5', 'cond': None, 'output': 'S1'}]
            },
            't5': {
                'hike': [{'next_state': 't6', 'cond': None, 'output': 'S0'}]
            }
        }
        self.current_state = 't3'
        self.variables = {'c': None, 'x': None}
        self.executed_methods = set()

    def let_c(self, value): self.variables['c'] = value
    def let_x(self, value): self.variables['x'] = value
    def visit(self): return self._execute_method('visit')
    def cast(self): return self._execute_method('cast')
    def spin(self): return self._execute_method('spin')
    def hike(self): return self._execute_method('hike')
    def link(self): raise StateMachineException('unknown')
    def close(self): raise StateMachineException('unknown')
    def seen_method(self, method): return method in self.executed_methods

    def has_max_out_edges(self):
        current = sum(len(m) for m in self.transitions.get(self.current_state, {}).values())
        max_edges = max(sum(len(m) for m in s.values()) for s in self.transitions.values())
        return bool(current and current == max_edges)

    def has_path_to(self, target):
        visited, stack = set(), [self.current_state]
        while stack:
            state = stack.pop()
            if state == target: return True
            if state not in visited:
                visited.add(state)
                stack.extend(t['next_state'] for m in self.transitions.get(state, {}).values() for t in m
                            if t['next_state'] not in visited)
        return False

    def _execute_method(self, method):
        if method not in self.transitions.get(self.current_state, {}):
            raise StateMachineException('unsupported')
        for t in self.transitions[self.current_state][method]:
            if t.get('cond') is None or self.variables.get(t['cond']['var']) == t['cond']['value']:
                self.current_state = t['next_state']
                self.executed_methods.add(method)
                return t['output']
        raise StateMachineException('unsupported')


def main(): return MooreMachine()


def test_condition_branch():
    obj = main()
    obj.current_state, obj.let_c(1) = 't7',
    assert obj.cast() == 'S2'
    obj.current_state, obj.let_c(0) = 't7',
    assert obj.cast() == 'S1'


def test_no_condition():
    assert main().visit() == 'S1'


def test_unsupported():
    obj = main()
    obj.current_state = 't1'
    try:
        obj.visit()
    except StateMachineException as e:
        assert str(e) == 'unsupported'


def test_spin():
    obj = main()
    try:
        obj.spin()
    except StateMachineException as e:
        assert str(e) == 'unsupported'
    obj.current_state = 't2'
    assert obj.spin() == 'S2' and obj.current_state == 't1'


def test_spin_conditions():
    obj = main()
    obj.current_state, obj.let_c(0) = 't7',
    obj.cast()
    obj.let_x(0)
    assert obj.spin() == 'S0' and obj.current_state == 't6'
    obj.current_state, obj.let_x(1) = 't0',
    assert obj.spin() == 'S2' and obj.current_state == 't4'


def test_hike():
    obj = main()
    assert obj.hike() == 'S0' and obj.current_state == 't2'
    obj.current_state = 't1'
    assert obj.hike() == 'S2' and obj.current_state == 't6'
    assert obj.hike() == 'S2' and obj.current_state == 't7'


def test_hike_unsupported():
    obj = main()
    obj.current_state = 't4'
    try:
        obj.hike()
    except StateMachineException as e:
        assert str(e) == 'unsupported'


def test_hike_t5():
    obj = main()
    obj.current_state = 't4'
    obj.visit()
    assert obj.hike() == 'S0' and obj.current_state == 't6'


def test_state_unsupported():
    cases = [('t3','spin'),('t3','cast'),('t2','visit'),('t2','hike'),
             ('t1','spin'),('t1','visit'),('t6','spin'),('t6','visit'),
             ('t7','visit'),('t0','hike'),('t0','visit'),('t4','hike'),
             ('t4','spin'),('t5','spin'),('t5','visit')]
    for s, m in cases:
        obj = main()
        obj.current_state = s
        try:
            getattr(obj, m)()
        except StateMachineException as e:
            assert str(e) == 'unsupported'


def test_unmet_conditions():
    obj = main()
    obj.current_state = 't7'
    try:
        obj.cast()
    except StateMachineException as e:
        assert str(e) == 'unsupported'
    obj.current_state, obj.variables['x'] = 't0', 2
    try:
        obj.spin()
    except StateMachineException as e:
        assert str(e) == 'unsupported'


def test_nonexistent_state():
    obj = main()
    obj.current_state = 'nonexistent'
    for m in ['visit', 'cast', 'spin', 'hike']:
        try:
            getattr(obj, m)()
        except StateMachineException as e:
            assert str(e) == 'unsupported'


def test_seen_method():
    obj = main()
    assert not obj.seen_method('visit')
    obj.visit()
    assert obj.seen_method('visit')
    assert not obj.seen_method('cast')


def test_max_edges():
    obj = main()
    obj.current_state = 't3'
    assert not obj.has_max_out_edges()
    obj.current_state = 't7'
    assert obj.has_max_out_edges()
    obj.current_state = 'nonexistent'
    assert not obj.has_max_out_edges()


def test_path():
    obj = main()
    obj.current_state = 't3'
    assert obj.has_path_to('t4') and obj.has_path_to('t7')
    assert not obj.has_path_to('nonexistent')
    obj.current_state = 't0'
    assert obj.has_path_to('t4') and obj.has_path_to('t6')
    obj.current_state = 't5'
    assert obj.has_path_to('t7') and not obj.has_path_to('t3')


def test_unknown():
    obj = main()
    try:
        obj.link()
    except StateMachineException as e:
        assert str(e) == 'unknown'
    try:
        obj.close()
    except StateMachineException as e:
        assert str(e) == 'unknown'


def test():
    test_condition_branch()
    test_no_condition()
    test_unsupported()
    test_spin()
    test_spin_conditions()
    test_hike()
    test_hike_unsupported()
    test_hike_t5()
    test_state_unsupported()
    test_unmet_conditions()
    test_nonexistent_state()
    test_seen_method()
    test_max_edges()
    test_path()
    test_unknown()