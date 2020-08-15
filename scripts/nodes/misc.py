from scripts.nodes import base
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE
from scripts.utils import utils, logger
import random


class NodeValueSwitch(base.Node):
    """
    Class for node 'value switch'. Node that allows connecting multiple nodes to single input.
    It activates next node without delay and sets value to output.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function changes state to INACTIVE to prevent wrong functionality.
        """
        self.state = INACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Function changes state to INACTIVE to prevent wrong functionality.
        """
        self.state = INACTIVE

    def set_state(self, state, input_index, **kwargs):
        """
        Change state function, runs when other nodes are trying to activate current node.

        If node received signal then function takes value directly
        from object output and saves it to output. After all function
        resets node and activates next nodes
        """
        if state == WAITING:
            self.output_values[0] = kwargs["obj"].output_values[kwargs["output_index"]]
            self.set_active(0)
            self.state = INACTIVE


class NodeGetType(base.Node):
    """
    Class for node 'get type'. Node can't be activated.
    Node generates values in INACTIVE update function and saves them to output.
    """

    def __init__(self, data):
        """
        Class constructor. Creates variables:
            value_created - state that describes whether or not values were generated

        :param dict data: node information
        """
        super().__init__(data)
        self.value_created = False

    def update_inactive(self):
        """
        Update function, runs if state is INACTIVE.

        If values is not generated yet then function tries to
        take default value and type from description (desc_value).

        If there is no suitable type then values become None.
        """
        if not self.value_created:
            if self.desc_value in utils.types_default:
                self.output_values[1] = utils.types_default[self.desc_value]
                self.output_values[0] = type(utils.types_default[self.desc_value])
            else:
                self.output_values[0] = None
                self.output_values[1] = None
            self.value_created = True

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.
        """
        pass

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.
        """
        pass


class NodeType(base.Node):
    """
    Class for node 'type'. Node saves to output type of input data.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Saves to output type from input.
        """
        self.output_values[0] = type(self.get_value(0))
        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeRandom(base.Node):
    """
    Class for node 'random'. Basic random node that
    outputs random value in range [0, 1)
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Saves to output random value.
        """
        self.output_values[0] = random.random()
        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeRandomInt(base.Node):
    """
    Class for node 'random int'. Random node that
    outputs random integer value in settable range.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Saves to output random value in range [first input int value, second input int value).
        """
        if self.get_value(0) is not None and self.get_value(1) is not None:
            self.output_values[0] = random.randrange(int(self.get_value(0)), int(self.get_value(1)))
            self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeRandomNum(base.Node):
    """
    Class for node 'random int'. Random node that
    outputs random number value in settable range.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Saves to output random value in range [first input value, second input value).
        """
        if self.get_value(0) is not None and self.get_value(1) is not None:
            self.output_values[0] = utils.Number(self.get_value(0) +
                                                 random.random() * (self.get_value(1) - self.get_value(0)))
            self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE


class NodeRandomSeed(base.Node):
    """
    Class for node 'random int'. Special node that allows to change
    initial value of a pseudo random number generator.
    """

    def update_waiting(self):
        """
        Update function, runs if state is WAITING.

        Function sets seed from input value.
        """
        random.seed(self.get_value(0))
        self.state = ACTIVE

    def update_active(self):
        """
        Update function, runs if state is ACTIVE.

        Resets node and activates next nodes.
        """
        self.set_active(0)
        self.state = INACTIVE
