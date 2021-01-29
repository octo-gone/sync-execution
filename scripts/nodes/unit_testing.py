from scripts.nodes import base
from scripts.utils import exceptions, logger, utils
from scripts.nodes.base import ACTIVE, WAITING, INACTIVE


class NodeUnitTest(base.Node):
    aliases = ("unit test",)

    def __init__(self, data):
        super().__init__(data)
        self.state = ACTIVE

    def update_waiting(self):
        self.state = INACTIVE

    def update_active(self):
        if base.Node.ut_send is None:
            base.Node.ut_send = []
            base.Node.ut_catch = []
            logger.log_success("unit testing started")
        split_value, *tests = self.desc_value.split("&#xa;")
        catch = False
        for test in tests:
            if split_value == test:
                catch = True
                continue
            if not catch:
                base.Node.ut_send += [test]
            else:
                base.Node.ut_catch += [test]
        logger.log_success("unit test added")
        self.set_active(0)
        self.state = INACTIVE
