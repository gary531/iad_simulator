# created by weiganyi on 201307
# -* - coding: UTF-8 -* -
from module import *


#global log buffer list
g_log_buffer = []
#global log thread lock
g_log_lock = threading.Lock()

#observer module define
OB_MOD_MENU_BAR = "menu_bar"
OB_MOD_TOOL_BAR = "tool_bar"
OB_MOD_TREE = "tree"

#observer event define
OB_EVT_INVALID = 0
OB_EVT_INIT_FINISHED = 1
OB_EVT_TREE_SEL_CHANGED = 2
OB_EVT_WINDOWS_CREATE = 3
OB_EVT_WINDOWS_CLOSE = 4
OB_EVT_WINDOWS_CHANGED = 5
OB_EVT_WINDOWS_SAVED = 6


def TRACE(msg):
    return push_log_msg(msg)

def func():
    return inspect.stack()[1][3]

def push_log_msg(msg):
    g_log_lock.acquire()
    g_log_buffer.append(msg)
    g_log_lock.release()

def pop_log_msg():
    log_msg = ""

    g_log_lock.acquire()
    if len(g_log_buffer) > 0:
        log_msg = g_log_buffer[0]
        del g_log_buffer[0]
    g_log_lock.release()

    return log_msg

def get_device_info():  #test ok
    local_number = 0
    local_ip = ""
    local_port = 0
    local_rtp_ip = ""
    local_rtp_port = 0
    remote_number = 0
    remote_ip = ""
    remote_port = 0
    remote_rtp_ip = ""
    remote_rtp_port = 0

    try:
        config_object = configobj.ConfigObj("device.ini")
    except:
        traceback.print_exc()
        TRACE("[%s] open device.ini failure!"%func())
        return local_number, local_ip, local_port, local_rtp_ip, local_rtp_port, remote_number, \
            remote_ip, remote_port, remote_rtp_ip, remote_rtp_port

    device = "iad"

    local_number = eval(config_object[device]["local_number"])
    local_ip = config_object[device]["local_ip"]
    local_port = eval(config_object[device]["local_port"])
    local_rtp_ip = config_object[device]["local_rtp_ip"]
    local_rtp_port = eval(config_object[device]["local_rtp_port"])
    remote_number = eval(config_object[device]["remote_number"])
    remote_ip = config_object[device]["remote_ip"]
    remote_port = eval(config_object[device]["remote_port"])
    remote_rtp_ip = config_object[device]["remote_rtp_ip"]
    remote_rtp_port = eval(config_object[device]["remote_rtp_port"])

    return local_number, local_ip, local_port, local_rtp_ip, local_rtp_port, remote_number, \
        remote_ip, remote_port, remote_rtp_ip, remote_rtp_port

def set_device_info(local_number=0, local_ip="", local_port=0, local_rtp_ip="", local_rtp_port=0, \
    remote_number=0, remote_ip="", remote_port=0, remote_rtp_ip="", remote_rtp_port=0):
    try:
        config_object = configobj.ConfigObj("device.ini")
    except:
        traceback.print_exc()
        TRACE("[%s] open device.ini failure!"%func())
        return

    device = "iad"

    if local_number != 0:
        config_object[device]["local_number"] = str(local_number)
    if local_ip != "":
        config_object[device]["local_ip"] = local_ip
    if local_port != 0:
        config_object[device]["local_port"] = str(local_port)
    if local_rtp_ip != "":
        config_object[device]["local_rtp_ip"] = local_rtp_ip
    if local_rtp_port != 0:
        config_object[device]["local_rtp_port"] = str(local_rtp_port)
    if remote_number != 0:
        config_object[device]["remote_number"] = str(remote_number)
    if remote_ip != "":
        config_object[device]["remote_ip"] = remote_ip
    if remote_port != 0:
        config_object[device]["remote_port"] = str(remote_port)
    if remote_rtp_ip != "":
        config_object[device]["remote_rtp_ip"] = remote_rtp_ip
    if remote_rtp_port != 0:
        config_object[device]["remote_rtp_port"] = str(remote_rtp_port)

    try:
        config_object.write()
    except:
        pass

#get all msg template
def get_all_msg_tpl():
    #msg template disc
    msg_disc = {}

    try:
        config_object = configobj.ConfigObj("msg.ini")
    except:
        traceback.print_exc()
        TRACE("[%s] open msg.ini failure!"%func())
        return msg_disc

    msg_tpl_lst = config_object.keys()
    for msg_name in msg_tpl_lst:
        msg_disc[msg_name] = []
        msg_lst = []
        line_lst = config_object[msg_name].keys()
        for line in line_lst:
            msg = config_object[msg_name][line]
            msg_lst.append(msg)
        msg_disc[msg_name] = msg_lst

    return msg_disc

#get a msg template
def get_msg_tpl(msg_name=""):
    if msg_name == "":
        TRACE("[%s] input param is incorrect!"%func())
        return [], False

    msg_lst = []

    try:
        config_object = configobj.ConfigObj("msg.ini")
    except:
        traceback.print_exc()
        TRACE("[%s] open msg.ini failure!"%func())
        return msg_lst, False

    found = False

    msg_tpl_lst = config_object.keys()
    if msg_name in msg_tpl_lst:
        found = True
        line_lst = config_object[msg_name].keys()
        for line in line_lst:
            msg = config_object[msg_name][line]
            msg_lst.append(msg)

    return msg_lst, found

#set a msg template
def set_msg_tpl(msg_name="", msg_lst=[]):
    if msg_name == "" or len(msg_lst) == 0:
        TRACE("[%s] input param is incorrect!"%func())
        return

    try:
        config_object = configobj.ConfigObj("msg.ini")
    except:
        traceback.print_exc()
        TRACE("[%s] open msg.ini failure!"%func())
        return

    config_object[msg_name] = {}

    msg_lst_len = len(msg_lst)
    for line_no in range(msg_lst_len):
        if msg_lst[line_no] == "" and line_no+1 >= msg_lst_len:
            break
        line = "line" + str(line_no+1)
        config_object[msg_name][line] = msg_lst[line_no]

    try:
        config_object.write()
    except:
        pass

#add a null msg template
def add_msg_tpl(msg_name=""):
    if msg_name == "":
        TRACE("[%s] input param is incorrect!"%func())
        return

    try:
        config_object = configobj.ConfigObj("msg.ini")
    except:
        traceback.print_exc()
        TRACE("[%s] open msg.ini failure!"%func())
        return

    config_object[msg_name] = {}

    try:
        config_object.write()
    except:
        pass

#delete a msg template
def del_msg_tpl(msg_name=""):
    if msg_name == "":
        TRACE("[%s] input param is incorrect!"%func())
        return

    try:
        config_object = configobj.ConfigObj("msg.ini")
    except:
        traceback.print_exc()
        TRACE("[%s] open msg.ini failure!"%func())
        return

    msg_tpl_lst = config_object.keys()
    if msg_name in msg_tpl_lst:
        line_lst = config_object[msg_name].keys()
        for line in line_lst:
            del config_object[msg_name][line]
        del config_object[msg_name]

    try:
        config_object.write()
    except:
        pass

def general_random():
    return string.join(random.sample("abcdefghijklmmopqrstuvwxyz0123456789", 10), "")

def strip_quote(quote_str=""):
    if quote_str == "":
        TRACE("[%s] input param is incorrect!"%func())
        return ""

    ret_str = ""
    start = 0
    end = len(quote_str)

    while 1:
        if quote_str[start] == "\"" or quote_str[start] == "\'":
            start = start + 1
        else:
            break

    while 1:
        if quote_str[end-1] == "\"" or quote_str[end-1] == "\'":
            end = end - 1
        else:
            break

    ret_str = quote_str[start:end]

    return ret_str

def get_curr_time():
    currentTime = time.time()
    localTime = time.localtime(currentTime)
    currentTimeStr = time.strftime("%y%m%d_%H%M%S",localTime)
    return currentTimeStr

def copy_dir(src="", dst=""):
    if src == "" or dst == "":
        TRACE("[%s] input param is incorrect!"%func())
        return

    if not os.path.exists(dst):
        os.mkdir(dst)

    src_lst = os.listdir(src)
    src_lst.sort()

    for src_file in src_lst:
        src_file_path = src+"\\"+src_file
        dst_file_path = dst+"\\"+src_file
        if os.path.isdir(src_file_path):
            os.mkdir(dst_file_path)
            copy_dir(src_file_path, dst_file_path)
        if os.path.isfile(src_file_path):
            win32file.CopyFile(src_file_path, dst_file_path, True)

class observer:
    def __init__(self):
        self.observer_disc = {}
        self.key_func = "func"
        self.key_event = "event"

    def register(self, name="", func=None):
        if name == "" or func == None:
            TRACE("[%s.%s] input param is incorrect!"%(__name__, func()))
            return

        if not self.observer_disc.has_key(name):
            self.observer_disc[name] = {}
            self.observer_disc[name][self.key_event] = []

        self.observer_disc[name][self.key_func] = func

    def subscribe(self, name="", event=OB_EVT_INVALID):
        if name == "" or event == OB_EVT_INVALID:
            TRACE("[%s.%s] input param is incorrect!"%(__name__, func()))
            return

        if self.observer_disc.has_key(name):
            self.observer_disc[name][self.key_event].append(event)

    def publish(self, event=OB_EVT_INVALID, param=None):
        if event == OB_EVT_INVALID:
            TRACE("[%s.%s] input param is incorrect!"%(__name__, func()))
            return

        for name in self.observer_disc.keys():
            if event in self.observer_disc[name][self.key_event]:
                self.observer_disc[name][self.key_func](event, param)


g_observer = observer()

