# created by weiganyi on 201307
# -* - coding: UTF-8 -* -
from module import *
import util
import com


class runner:
    def __init__(self):
        return

    def run_script(self, name=""):
        if name == "":
            util.TRACE("[%s.%s] input param is incorrect!"%(__name__, util.func()))
            return

        thread.start_new_thread(self.running,(name, ))

    def running(self, name=""):
        #first, clear the running environment
        com.iad.clear_env()

        try:
            execfile(name)
            util.TRACE("[%s.%s] testcase: %s run success"%(__name__, util.func(), name))
            return 0
        except com.UNEXCEPT_ERROR:
            util.TRACE("[%s.%s] testcase: %s run failure, error is %s"%(__name__, util.func(), name, com.UNEXCEPT_ERROR))
            return 1
        except com.TIMEOUT_ERROR:
            util.TRACE("[%s.%s] testcase: %s run failure, error is %s"%(__name__, util.func(), name, com.TIMEOUT_ERROR))
            return 2
        except com.VALUE_ERROR:
            util.TRACE("[%s.%s] testcase: %s run failure, error is %s"%(__name__, util.func(), name, com.VALUE_ERROR))
            return 3
        except:
            traceback.print_exc()
            util.TRACE("[%s.%s] testcase: %s run failure, error is %s"%(__name__, util.func(), name, com.UNKNOW_ERROR))
            return 4

g_runner = runner()

