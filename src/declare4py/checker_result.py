from _future_ import annotations

"""
Initializes class CheckerResults

Parameters
--------
    num_fulfillments

    num_violations

    num_pendings

    num_activations

    state

Attributes
--------
    num_fulfillments

    num_violations

    num_pendings

    num_activations

    state
"""

class CheckerResult:
    def __init__(self, num_fulfillments, num_violations, num_pendings, num_activations, state):
        self.num_fulfillments = num_fulfillments
        self.num_violations = num_violations
        self.num_pendings = num_pendings
        self.num_activations = num_activations
        self.state = state
