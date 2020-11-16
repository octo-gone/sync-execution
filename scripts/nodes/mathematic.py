from scripts.nodes import base
from scripts.utils import utils, logger
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE


class NodeAbs(base.Node):
    """
    Class for node 'abs'. Node that returns absolute value.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node has input value then function take
        absolute value and sets it to output.
        """
        if self.get_value(0) is not None:
            self.set_value(abs(self.get_value(0)), 0)
            self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeAdd(base.Node):
    """
    Class for node 'add'. Node that returns sum of input values.
    """

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If all inputs have value then function summarizes them and saves value to output.
        """
        if all(map(lambda x: x is not None, self.get_value(0, True))):
            self.set_value(sum(self.get_value(0, True)), 0)
            self.state = ACTIVE


class NodeDec(base.Node):
    """
    Class for node 'dec' (decrement). Node that returns decremented value (input value - 1).
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node has input value then function sets to output decremented value.
        """
        if self.get_value(0) is not None:
            self.set_value(self.get_value(0) - 1, 0)
            self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeDivision(base.Node):
    """
    Class for node 'division'. Node that returns division
    between dividend and divider (divisor).
    """

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node has both input values then function checks zero division.

        If divider not equal to zero then function evaluates output value
        and changes state otherwise function raises error.
        """
        if self.get_value(0) is not None and self.get_value(1) is not None:
            if self.get_value(1) == 0:
                logger.log_error(f"node 'division' raised exception 'Zero Division'")
            self.set_value(self.get_value(0) / self.get_value(1), 0)
            self.state = ACTIVE


class NodeExp(base.Node):
    """
    Class for node 'exp' (exponentiation/involution). Node that returns
    first value multiplied second value times.
    """

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node has both input values then function
        generates value and sets it to output.
        """
        if self.get_value(0) is not None and self.get_value(1) is not None:
            self.set_value(self.get_value(0) ** self.get_value(1), 0)
            self.state = ACTIVE


class NodeInc(base.Node):
    """
    Class for node 'inc' (increment). Node that returns incremented value (input value + 1).
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node has input value then function sets to output incremented value.
        """
        if self.get_value(0) is not None:
            self.set_value(self.get_value(0) + 1, 0)
            self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeTrunc(base.Node):
    """
    Class for node 'trunc' (truncate). Node that returns only integer part of a number.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node has input value then function sets to output integer from number.
        """
        if self.get_value(0) is not None:
            self.set_value(int(self.get_value(0)), 0)
            self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeInv(base.Node):
    """
    Class for node 'inv' (inverse). Node that returns number with different number sign.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node has input value then function sets to output inverse number value.
        """
        if self.get_value(0) is not None:
            self.set_value(-self.get_value(0), 0)
            self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeMult(base.Node):
    """
    Class for node 'mult' (multiplication). Node that returns numbers multiplied by each other.
    """

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If all inputs have values then function multiplies them and sets to output.
        """
        if all(map(lambda x: x is not None, self.get_value(0, True))):
            m = 1
            for v in self.get_value(0, True):
                m *= v
            self.set_value(m, 0)
            self.state = ACTIVE


class NodeRound(base.Node):
    """
    Class for node 'round'. Node that returns rounded value of input number.
    """

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If some node connected to 'precision' input then function takes value
        from it otherwise function sets precision to 0.

        If number input value and precision are not equal to None then function evaluates
        round function and sets result to output.
        """
        precision = self.get_value(1) if self.inputs[1] else 0
        if self.get_value(0) is not None and precision is not None:
            self.set_value(round(self.get_value(0), precision), 0)
            self.state = ACTIVE


class NodeSub(base.Node):
    """
    Class for node 'sub' (subtraction). Node that returns first value reduced by second value.
    """

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node has both input values then function
        generates value and sets it to output.
        """
        if self.get_value(0) is not None and self.get_value(1) is not None:
            self.set_value(self.get_value(0) - self.get_value(1), 0)
            self.state = ACTIVE


class NodeMod(base.Node):
    """
    Class for node 'mod'. Node that returns reminder from division
    between dividend and divider (divisor).
    """

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node has both input values then function checks zero division.

        If divider not equal to zero then function evaluates output value
        and changes state otherwise function raises error.
        """
        if self.get_value(0) is not None and self.get_value(1) is not None:
            if self.get_value(1) == 0:
                logger.log_error(f"node 'mod' raised exception 'Zero Division'")
            self.set_value(self.get_value(0) % self.get_value(1), 0)
            self.state = ACTIVE


class NodeDiv(base.Node):
    """
    Class for node 'div'. Node that returns integer value from division
    between dividend and divider (divisor).
    """

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        If node has both input values then function checks zero division.

        If divider not equal to zero then function evaluates output value
        and changes state otherwise function raises error.
        """
        if self.get_value(0) is not None and self.get_value(1) is not None:
            if self.get_value(1) == 0:
                logger.log_error(f"node 'div' raised exception 'Zero Division'")
            self.set_value(self.get_value(0) // self.get_value(1), 0)
            self.state = ACTIVE
