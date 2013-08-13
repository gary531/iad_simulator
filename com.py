# created by weiganyi on 201307
# -* - coding: UTF-8 -* -
from module import *
import util
import codec


UNEXCEPT_ERROR = "unexcept_error"
TIMEOUT_ERROR = "timeout_error"
VALUE_ERROR = "value_error"
UNKNOW_ERROR = "unknow_error"


class communicator:
    def __init__(self):
        #device network param
        self.local_number = 0
        self.local_ip = ""
        self.local_port = 0
        self.local_rtp_ip = ""
        self.local_rtp_port = 0
        self.remote_number = 0
        self.remote_ip = ""
        self.remote_port = 0
        self.remote_rtp_ip = ""
        self.remote_rtp_port = 0

        #the socket id for sip and rtp
        self.sip_socket = None
        self.rtp_socket = None

        #the thread msg queue for sip and rtp
        self.sip_send_msg_queue = None
        self.sip_recv_msg_queue = None
        self.rtp_send_msg_queue = None
        self.rtp_recv_msg_queue = None
        #the thread exit queue for sip and rtp
        self.sip_send_exit_queue = None
        self.sip_recv_exit_queue = None
        self.rtp_send_exit_queue = None
        self.rtp_recv_exit_queue = None

    def set_local_number(self, local_number=0):
        self.local_number = local_number

    def restart_sip(self, local_ip="", local_port=0):
        util.TRACE("[%s.%s] local_ip=%s local_port=%d"%(__name__, util.func(), local_ip, local_port))

        if local_ip != "" and local_port != 0:
            if self.local_ip != local_ip or self.local_port != local_port:
                try:
                    #send "exit" msg to running thread and let it quit
                    if self.sip_send_exit_queue != None:
                        self.sip_send_exit_queue.put("exit")
                    if self.sip_recv_exit_queue != None:
                        self.sip_recv_exit_queue.put("exit")

                    #close old sip socket
                    if self.sip_socket != None:
                        self.sip_socket.close()

                    sip_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    local_addr = (local_ip, local_port)
                    sip_socket.bind(local_addr)
                    sip_socket.setblocking(0)
                    util.TRACE("[%s.%s] create sip socket %s:%d succ"%(__name__, util.func(), local_ip, local_port))

                    self.sip_socket = sip_socket
                    self.local_ip = local_ip
                    self.local_port = local_port

                    #create thread msg queue for sip
                    if self.sip_send_msg_queue == None:
                        self.sip_send_msg_queue = Queue.Queue(64)
                    if self.sip_recv_msg_queue == None:
                        self.sip_recv_msg_queue = Queue.Queue(64)
                    if self.sip_send_exit_queue == None:
                        self.sip_send_exit_queue = Queue.Queue(64)
                    if self.sip_recv_exit_queue == None:
                        self.sip_recv_exit_queue = Queue.Queue(64)

                    thread.start_new_thread(self.t_sip_send_msg,())
                    thread.start_new_thread(self.t_sip_recv_msg,())
                except:
                    traceback.print_exc()
                    util.TRACE("[%s.%s] create sip socket fail, maybe port already used!"%(__name__, util.func()))

    def restart_rtp(self, local_rtp_ip="", local_rtp_port=0):
        util.TRACE("[%s.%s] local_ip=%s local_rtp_port=%d"%(__name__, util.func(), local_rtp_ip, local_rtp_port))

        if local_rtp_ip != "" and local_rtp_port != 0:
            if self.local_rtp_ip != local_rtp_ip or self.local_rtp_port != local_rtp_port:
                try:
                    #send "exit" msg to running thread and let it quit
                    if self.rtp_send_exit_queue != None:
                        self.rtp_send_exit_queue.put("exit")
                    if self.rtp_recv_exit_queue != None:
                        self.rtp_recv_exit_queue.put("exit")

                    #close old rtp socket
                    if self.rtp_socket != None:
                        self.rtp_socket.close()

                    rtp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    local_addr = (local_rtp_ip, local_rtp_port)
                    rtp_socket.bind(local_addr)
                    rtp_socket.setblocking(0)
                    util.TRACE("[%s.%s] create rtp socket %s:%d succ"%(__name__, util.func(), local_rtp_ip, local_rtp_port))

                    self.rtp_socket = rtp_socket
                    self.local_rtp_ip = local_rtp_ip
                    self.local_rtp_port = local_rtp_port

                    #create thread msg queue for rtp
                    if self.rtp_send_msg_queue == None:
                        self.rtp_send_msg_queue = Queue.Queue(64)
                    if self.rtp_recv_msg_queue == None:
                        self.rtp_recv_msg_queue = Queue.Queue(64)
                    if self.rtp_send_exit_queue == None:
                        self.rtp_send_exit_queue = Queue.Queue(64)
                    if self.rtp_recv_exit_queue == None:
                        self.rtp_recv_exit_queue = Queue.Queue(64)

                    thread.start_new_thread(self.t_rtp_send_msg,())
                    thread.start_new_thread(self.t_rtp_recv_msg,())
                except:
                    traceback.print_exc()
                    util.TRACE("[%s.%s] create rtp socket fail, maybe port already used!"%(__name__, util.func()))

    def set_remote_number(self, remote_number=0):
        self.remote_number = remote_number

    def set_remote_ip(self, remote_ip=""):
        self.remote_ip = remote_ip

    def set_remote_port(self, remote_port=0):
        self.remote_port = remote_port

    def set_remote_rtp_ip(self, remote_rtp_ip=""):
        self.remote_rtp_ip = remote_rtp_ip

    def set_remote_rtp_port(self, remote_rtp_port=0):
        self.remote_rtp_port = remote_rtp_port

    def t_sip_send_msg(self):
        while 1:
            try:
                data = self.sip_send_msg_queue.get_nowait()

                if self.remote_ip != "" and self.remote_port != 0:
                    remote_addr = (self.remote_ip, self.remote_port)
                    try:
                        self.sip_socket.sendto(data, remote_addr)
                    except:
                        traceback.print_exc()
                        util.TRACE("[%s.%s] socket send sip msg failure:\n%s\n"%(__name__, util.func(), data))
            except:
                try:
                    data = self.sip_send_exit_queue.get_nowait()

                    if data == "exit":
                        return
                except:
                    pass

                time.sleep(0.01)

    def t_sip_recv_msg(self):
        while 1:
            try:
                data, addr = self.sip_socket.recvfrom(1024)

                try:
                    self.sip_recv_msg_queue.put(data)
                except:
                    traceback.print_exc()
                    util.TRACE("[%s.%s] msg queue put failure!"%(__name__, util.func()))
            except:
                try:
                    data = self.sip_recv_exit_queue.get_nowait()

                    if data == "exit":
                        return
                except:
                    pass

                time.sleep(0.01)

    def t_rtp_send_msg(self):
        while 1:
            try:
                data = self.rtp_send_msg_queue.get_nowait()

                if self.remote_rtp_ip != "" and self.remote_rtp_port != 0:
                    remote_addr = (self.remote_rtp_ip, self.remote_rtp_port)
                    try:
                        self.rtp_socket.sendto(data, remote_addr)
                    except:
                        traceback.print_exc()
                        util.TRACE("[%s.%s] socket send rtp msg failure:\n%s\n"%(__name__, util.func(), data))
            except:
                try:
                    data = self.rtp_send_exit_queue.get_nowait()

                    if data == "exit":
                        return
                except:
                    pass

                time.sleep(0.005)

    def t_rtp_recv_msg(self):
        while 1:
            try:
                data, addr = self.rtp_socket.recvfrom(1024)
            except:
                try:
                    data = self.rtp_recv_exit_queue.get_nowait()

                    if data == "exit":
                        return
                except:
                    pass

                time.sleep(0.005)

    def wait_msg(self, type=0, msg="", wait_time=0):
        if type > 1 or msg == "" or wait_time==0:
            util.TRACE("[%s.%s] input param is incorrect!"%(__name__, util.func()))
            raise UNEXCEPT_ERROR
            return

        num = 0
        loop_num = wait_time / 0.01
        err_str = TIMEOUT_ERROR

        while num < loop_num:
            try:
                data = self.sip_recv_msg_queue.get_nowait()
                if data != "":
                    ret = codec.g_codec.decode_msg(data, type, msg)
                    if ret == 1 or ret == 3 or ret == 4:
                        err_str = UNEXCEPT_ERROR
                        break
                    elif ret == 2 or ret == 5:
                        err_str = VALUE_ERROR
                        continue
                    else:
                        err_str = ""
                        break
            except:
                time.sleep(0.01)
                num = num + 1

        if err_str != "":
            raise err_str

    def send_msg(self, type=0, msg=""):
        if type > 1 or msg == "":
            util.TRACE("[%s.%s] input param is incorrect!"%(__name__, util.func()))
            raise UNEXCEPT_ERROR
            return

        true_msg = codec.g_codec.encode_msg(type, msg)
        if true_msg != "":
            self.sip_send_msg_queue.put(true_msg)

    def delay(self, wait_time=0):
        if wait_time == 0:
            util.TRACE("[%s.%s] input param is incorrect!"%(__name__, util.func()))
            raise UNEXCEPT_ERROR
            return

        time.sleep(wait_time)

    def recv_rtp(self):
        return

    def send_rtp(self, file=""):
        if file == "":
            util.TRACE("[%s.%s] input param is incorrect!"%(__name__, util.func()))
            raise UNEXCEPT_ERROR
            return

        rtp_packet_lst = codec.g_rtp.parse_file(file)
        for rtp_packet in rtp_packet_lst:
            self.rtp_send_msg_queue.put(rtp_packet)
            #the packet be sent in every 30 ms
            time.sleep(0.03)

    def send_recv_rtp(self, file=""):
        try:
            self.send_rtp(file)
        except:
            raise

    def clear_env(self):
        #clear the sip recv msg queue leaved by last testcase
        while 1:
            try:
                data = self.sip_recv_msg_queue.get_nowait()
            except:
                break;

        #clear the rtp recv msg queue leaved by last testcase
        while 1:
            try:
                data = self.rtp_recv_msg_queue.get_nowait()
            except:
                break;


iad = communicator()

