# created by weiganyi on 201307
# -* - coding: UTF-8 -* -
from module import *
import util
import com


class codec:
    def __init__(self):
        #template msg disc
        self.msg_disc = {}

        #the msg line list in the lastest received msg
        self.last_msg = []

    def encode_msg(self, msg_type=0, msg_tpl=""):
        if msg_type > 1 or msg_tpl == "":
            util.TRACE("[%s.%s] input param is incorrect!"%(__name__, util.func()))
            return ""

        msg = ""

        #if msg_type=0, use template msg; if msg_type==1, use self defined msg
        if msg_type == 0:
            if msg_tpl in self.msg_disc.keys():
                msg_lst = self.msg_disc[msg_tpl]
                for line in msg_lst:
                    msg = msg + line + "\r\n"
            else:
                util.TRACE("[%s.%s] msg template %s isn't defined!"%(__name__, util.func(), msg_tpl))
                return ""
        elif msg_type == 1:
            msg = msg_tpl

        #replace key words within []
        start = 0
        while 1:
            idx1 = string.find(msg, '[', start)
            if idx1 != -1:
                idx2 = string.find(msg, ']', idx1+1)
                if idx2 != -1 and idx2-idx1 > 1:
                    key = msg[idx1+1:idx2]
                    #replace device key word
                    if key == "local_ip":
                        msg = string.replace(msg, '['+key+']', com.iad.local_ip)
                    elif key == "local_port":
                        msg = string.replace(msg, '['+key+']', str(com.iad.local_port))
                    elif key == "local_rtp_port":
                        msg = string.replace(msg, '['+key+']', str(com.iad.local_rtp_port))
                    elif key == "local_number":
                        msg = string.replace(msg, '['+key+']', str(com.iad.local_number))
                    elif key == "remote_number":
                        msg = string.replace(msg, '['+key+']', str(com.iad.remote_number))
                    elif key == "remote_ip":
                        msg = string.replace(msg, '['+key+']', com.iad.remote_ip)
                    elif key == "remote_port":
                        msg = string.replace(msg, '['+key+']', str(com.iad.remote_port))
                    elif key == "remote_rtp_ip":
                        msg = string.replace(msg, '['+key+']', com.iad.remote_rtp_ip)
                    elif key == "remote_rtp_port":
                        msg = string.replace(msg, '['+key+']', str(com.iad.remote_rtp_port))
                    #anylse if seq param included in the msg key word, such as:[Route:,2]
                    bk_key = key
                    replace_num = 1
                    idx3 = string.find(bk_key, ',', 0)
                    if idx3 != -1:
                        replace_num = bk_key[idx3+1:]
                        if replace_num < 1:
                            util.TRACE("[%s.%s] key [%s] has a wrong replace num param!"%(__name__, util.func(), bk_key))
                            replace_num = 1
                        key = bk_key[:idx3]
                    #replace msg key word
                    num = 0
                    for line in self.last_msg:
                        idx4 = string.find(line, key, 0)
                        if idx4 != -1:
                            num = num + 1
                            if num == replace_num:
                                msg = string.replace(msg, '['+bk_key+']', line[idx4:])
                                break
                    #replace random key word
                    if key == "random":
                        msg = string.replace(msg, '['+key+']', util.general_random())
                    #continue to find another key word
                    start = idx1+1
                else:
                    break
            else:
                break

        return msg

    def decode_msg(self, recv_msg="", msg_type=0, msg_tpl=""):
        if msg_type > 1 or msg_tpl == "" or recv_msg == "":
            util.TRACE("[%s.%s] input param is incorrect!"%(__name__, util.func()))
            return 1

        #parse msg into line list format
        recv_msg_lst = string.split(recv_msg, '\n')
        if len(recv_msg_lst) == 0:
            util.TRACE("[%s.%s] recv msg format error!"%(__name__, util.func()))
            return 2

        #strip the space or '\r' before every line and after
        recv_msg_lst2 = []
        for line in recv_msg_lst:
            line.strip()
            if len(line) >= 1 and line[-1] == '\r':
                recv_msg_lst2.append(line[:-1])
            else:
                recv_msg_lst2.append(line)

        #if msg_type=0, use template msg; if msg_type==1, use self defined msg
        if msg_type == 0:
            if msg_tpl in self.msg_disc.keys():
                match_msg_lst2 = self.msg_disc[msg_tpl]
            else:
                util.TRACE("[%s.%s] msg template %s isn't defined!"%(__name__, util.func(), msg_tpl))
                return 3
        elif msg_type == 1:
            #parse template msg into line list format
            match_msg_lst = string.split(msg_tpl, '\n')
            if len(match_msg_lst) == 0:
                util.TRACE("[%s.%s] match msg format error!"%(__name__, util.func()))
                return 4
            #strip the space or '\r' before every line and after
            match_msg_lst2 = []
            for line in match_msg_lst:
                line.strip()
                if len(line) >= 1 and line[-1] == '\r':
                    match_msg_lst2.append(line[:-1])
                match_msg_lst2.append(line)

        #check if the every line of the template msg be included in the recv msg
        for match_msg_line in match_msg_lst2:
            found = 0
            for recv_msg_line in recv_msg_lst2:
                if match_msg_line in recv_msg_line:
                    found = 1
                    break
            if found == 0:
                util.TRACE("[%s.%s] msg parse failure!"%(__name__, util.func()))
                return 5

        self.last_msg = recv_msg_lst2
        return 0

    def set_msg_disc(self, msg_disc={}):
        self.msg_disc = msg_disc


class rtp:
    def __init__(self):
        self.home_dir = ""
        self.rtp_dir = ""
        return

    def parse_file(self, file=""):
        rtp_packet_lst = []

        if file == "":
            util.TRACE("[%s.%s] input param is incorrect!"%(__name__, util.func()))
            return rtp_packet_lst

        os.chdir(self.rtp_dir)
        try:
            fpcap = open(file, "rb")
            raw_data = fpcap.read()
        except:
            traceback.print_exc()
            os.chdir(self.home_dir)
            return rtp_packet_lst

        pcap_hdr = {}
        pcap_hdr["magic_number"] = raw_data[0:4]
        pcap_hdr["version_major"] = raw_data[4:6]
        pcap_hdr["version_minor"] = raw_data[6:8]
        pcap_hdr["thiszone"] = raw_data[8:12]
        pcap_hdr["sigfigs"] = raw_data[12:16]
        pcap_hdr["snaplen"] = raw_data[16:20]
        pcap_hdr["linktype"] = raw_data[20:24]

        i = 24
        pcap_packet_hdr = {}
        rtp_packet_hdr = {}
        rtp_packet = ""

        while(i < len(raw_data)):
            pcap_packet_hdr["gmttime"] = raw_data[i:i+4]
            pcap_packet_hdr["microtime"] = raw_data[i+4:i+8]
            pcap_packet_hdr["caplen"] = raw_data[i+8:i+12]
            pcap_packet_hdr["len"] = raw_data[i+12:i+16]

            packet_len = struct.unpack("I", pcap_packet_hdr["len"])[0]

            #the length of ethernet is 14 bytes
            rtp_packet_hdr["ethernet"] = raw_data[i+16:i+30]
            #the length of ip is 20 bytes
            rtp_packet_hdr["ip"] = raw_data[i+30:i+50]
            #the length of udp is 8 bytes
            rtp_packet_hdr["udp"] = raw_data[i+50:i+58]

            rtp_packet = raw_data[i+58:i+16+packet_len]
            rtp_packet_lst.append(rtp_packet)

            i = i + 16 + packet_len

        os.chdir(self.home_dir)
        return rtp_packet_lst

    def set_home_dir(self, dir=""):
        if dir == "":
            util.TRACE("[%s.%s] input param is incorrect!"%(__name__, util.func()))
            return

        self.home_dir = dir

    def set_rtp_dir(self, dir=""):
        if dir == "":
            util.TRACE("[%s.%s] input param is incorrect!"%(__name__, util.func()))
            return

        self.rtp_dir = dir


g_codec = codec()

g_rtp = rtp()

