#!/usr/bin/env python

from path_planning.states.base_state import BaseState


class LinearStateMachine(BaseState):
    """
    The exit code of this state machine is just the exit code of its last state.
    """

    def __init__(self, name, states):
        self.name = name
        self.states = states
        self.idx = 0
        self.completed = False

    def state_name(self):
        return self.name + '/' + self.states[self.idx].state_name()

    def initialize(self, t, controls, sub_state, world_state, sensors):
        self.states[self.idx].initialize(t, controls, sub_state, world_state, sensors)

    def process(self, t, controls, sub_state, world_state, sensors):
        state = self.states[self.idx]
        state.process(t, controls, sub_state, world_state, sensors)

        if state.has_completed():
            state.finalize(t, controls, sub_state, world_state, sensors)
            self.idx += 1
            if self.idx == len(self.states):
                self.completed = True
                return

            new_state = self.states[self.idx]
            print("Switching from %s to %s..." % (state.state_name(), new_state.state_name()))
            new_state.initialize(t, controls, sub_state, world_state, sensors)
            new_state.process(t, controls, sub_state, world_state, sensors)

    def finalize(self, t, controls, sub_state, world_state, sensors):
        pass

    def has_completed(self):
        return self.completed

    def exit_code(self):
        # return the exit code of the last state
        return self.state.exit_code()
