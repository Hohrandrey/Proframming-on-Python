import unittest


class StateMachineException(Exception):
    pass


class MooreMachine:
    def __init__(self):
        self.transitions = {
            't3': {
                'hike': [
                    {
                        'next_state': 't2',
                        'cond': None,
                        'output': 'S0'
                    }
                ],
                'visit': [
                    {
                        'next_state': 't7',
                        'cond': None,
                        'output': 'S1'
                    }
                ]
            },
            't2': {
                'spin': [
                    {
                        'next_state': 't1',
                        'cond': None,
                        'output': 'S2'
                    }
                ]
            },
            't1': {
                'hike': [
                    {
                        'next_state': 't6',
                        'cond': None,
                        'output': 'S2'
                    }
                ]
            },
            't6': {
                'hike': [
                    {
                        'next_state': 't7',
                        'cond': None,
                        'output': 'S2'
                    }
                ],
                'swap': [
                    {
                        'next_state': 't7',
                        'cond': None,
                        'output': 'S2'
                    }
                ]
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
                'swap': [
                    {
                        'next_state': 't6',
                        'cond': None,
                        'output': 'S2'
                    }
                ]
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
                'visit': [
                    {
                        'next_state': 't5',
                        'cond': None,
                        'output': 'S1'
                    }
                ]
            },
            't5': {
                'hike': [
                    {
                        'next_state': 't6',
                        'cond': None,
                        'output': 'S0'
                    }
                ]
            }
        }

        self.current_state = 't3'
        self.variables = {'c': None, 'x': None}
        self.executed_methods = set()

    def let_c(self, value):
        self.variables['c'] = value

    def let_x(self, value):
        self.variables['x'] = value

    def visit(self):
        return self._execute_method('visit')

    def cast(self):
        return self._execute_method('cast')

    def spin(self):
        return self._execute_method('spin')

    def hike(self):
        return self._execute_method('hike')

    def link(self):
        raise StateMachineException('unknown')

    def close(self):
        raise StateMachineException('unknown')

    def seen_method(self, method_name):
        return method_name in self.executed_methods

    def has_max_out_edges(self):
        current_out_edges = sum(len(methods) for methods in self.transitions.get(self.current_state, {}).values())
        if current_out_edges == 0:
            return False
        max_out_edges = max(
            sum(len(methods) for methods in state_transitions.values())
            for state_transitions in self.transitions.values()
        )
        return current_out_edges == max_out_edges

    def has_path_to(self, target_state):
        visited = set()
        stack = [self.current_state]

        while stack:
            state = stack.pop()
            if state == target_state:
                return True
            if state not in visited:
                visited.add(state)
                for method_transitions in self.transitions.get(state, {}).values():
                    for transition in method_transitions:
                        if transition['next_state'] not in visited:
                            stack.append(transition['next_state'])
        return False

    def _execute_method(self, method_name):
        if method_name not in self.transitions.get(self.current_state, {}):
            raise StateMachineException('unsupported')
        transitions = self.transitions[self.current_state][method_name]
        for trans in transitions:
            cond = trans.get('cond')
            if (cond is None
                    or self.variables.get(cond['var']) == cond['value']):
                self.current_state = trans['next_state']
                self.executed_methods.add(method_name)
                return trans['output']
        raise StateMachineException('unsupported')


def main():
    return MooreMachine()


def test_execute_method_condition_branch():
    obj = main()
    obj.current_state = 't7'
    obj.let_c(1)
    assert obj.cast() == 'S2'
    obj.current_state = 't7'
    obj.let_c(0)
    assert obj.cast() == 'S1'


def test_execute_method_no_condition_branch():
    obj = main()
    assert obj.visit() == 'S1'


def test_execute_method_unsupported():
    obj = main()
    obj.current_state = 't1'
    try:
        obj.visit()
    except StateMachineException as e:
        assert str(e) == 'unsupported'


def test_spin_method():
    obj = main()
    try:
        obj.spin()
    except StateMachineException as e:
        assert str(e) == 'unsupported'
    obj.current_state = 't2'
    assert obj.spin() == 'S2'
    assert obj.current_state == 't1'


def test_spin_method_with_conditions():
    obj = main()
    obj.current_state = 't7'
    obj.let_c(0)
    obj.cast()
    obj.let_x(0)
    assert obj.spin() == 'S0'
    assert obj.current_state == 't6'
    obj.current_state = 't0'
    obj.let_x(1)
    assert obj.spin() == 'S2'
    assert obj.current_state == 't4'


def test_hike_method():
    obj = main()
    assert obj.hike() == 'S0'
    assert obj.current_state == 't2'
    obj.current_state = 't1'
    assert obj.hike() == 'S2'
    assert obj.current_state == 't6'
    assert obj.hike() == 'S2'
    assert obj.current_state == 't7'


def test_hike_method_unsupported():
    obj = main()
    obj.current_state = 't4'
    try:
        obj.hike()
    except StateMachineException as e:
        assert str(e) == 'unsupported'


def test_hike_method_in_t5():
    obj = main()
    obj.current_state = 't4'
    obj.visit()
    assert obj.hike() == 'S0'
    assert obj.current_state == 't6'


def test_unsupported_method_in_current_state():
    states_and_methods = [
        ('t3', 'spin'),
        ('t3', 'cast'),
        ('t2', 'visit'),
        ('t2', 'hike'),
        ('t1', 'spin'),
        ('t1', 'visit'),
        ('t6', 'spin'),
        ('t6', 'visit'),
        ('t7', 'visit'),
        ('t0', 'hike'),
        ('t0', 'visit'),
        ('t4', 'hike'),
        ('t4', 'spin'),
        ('t5', 'spin'),
        ('t5', 'visit'),
    ]
    for state, method in states_and_methods:
        obj = main()
        obj.current_state = state
        try:
            getattr(obj, method)()
        except StateMachineException as e:
            assert str(e) == 'unsupported'


def test_unsupported_due_to_unmet_conditions():
    obj = main()
    obj.current_state = 't7'
    obj.variables['c'] = None
    try:
        obj.cast()
    except StateMachineException as e:
        assert str(e) == 'unsupported'
    obj.current_state = 't0'
    obj.variables['x'] = 2
    try:
        obj.spin()
    except StateMachineException as e:
        assert str(e) == 'unsupported'


def test_unsupported_in_non_existent_state():
    obj = main()
    obj.current_state = 'non_existent_state'
    for method in ['visit', 'cast', 'spin', 'hike']:
        try:
            getattr(obj, method)()
        except StateMachineException as e:
            assert str(e) == 'unsupported'


def test_seen_method():
    obj = main()
    assert not obj.seen_method('visit')
    obj.visit()
    assert obj.seen_method('visit')
    assert not obj.seen_method('cast')


def test_has_max_out_edges():
    obj = main()
    obj.current_state = 't3'
    assert not obj.has_max_out_edges()
    obj.current_state = 't7'
    assert obj.has_max_out_edges()
    obj.current_state = 'nonexistent'
    assert not obj.has_max_out_edges()


def test_has_path_to():
    obj = main()
    obj.current_state = 't3'
    assert obj.has_path_to('t4')
    assert obj.has_path_to('t7')
    assert not obj.has_path_to('nonexistent')
    obj.current_state = 't0'
    assert obj.has_path_to('t4')
    assert obj.has_path_to('t6')
    obj.current_state = 't5'
    assert obj.has_path_to('t7')
    assert not obj.has_path_to('t3')


def test_link_and_close():
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
    test_execute_method_condition_branch()
    test_execute_method_no_condition_branch()
    test_execute_method_unsupported()
    test_spin_method()
    test_spin_method_with_conditions()
    test_hike_method()
    test_hike_method_unsupported()
    test_hike_method_in_t5()
    test_unsupported_method_in_current_state()
    test_unsupported_due_to_unmet_conditions()
    test_unsupported_in_non_existent_state()
    test_seen_method()
    test_has_max_out_edges()
    test_has_path_to()
    test_link_and_close()
