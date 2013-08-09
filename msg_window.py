# -* - coding: UTF-8 -* -
#Boa:MDIChild:msg_window
from module import *
import util


def create(parent):
    return msg_window(parent)

[wxID_MSG_WINDOW, wxID_MSG_WINDOWMSG_TEXT, wxID_MSG_WINDOWOK_BUTTON, 
] = map(lambda _init_ctrls: wxNewId(), range(3))

class msg_window(wxMDIChildFrame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxMDIChildFrame.__init__(self, id=wxID_MSG_WINDOW, name='msg_window',
              parent=prnt, pos=wxPoint(0, 0), size=wxSize(577, 493),
              style=wxDEFAULT_FRAME_STYLE, title='')
        self.SetClientSize(wxSize(569, 466))
        self.SetToolTipString('')
        EVT_CLOSE(self, self.OnMsg_windowClose)

        self.msg_text = wxTextCtrl(id=wxID_MSG_WINDOWMSG_TEXT, name='msg_text',
              parent=self, pos=wxPoint(24, 16), size=wxSize(520, 392),
              style=wxTE_MULTILINE, value='')
        self.msg_text.SetToolTipString('')
        EVT_TEXT(self.msg_text, wxID_MSG_WINDOWMSG_TEXT, self.OnMsg_textText)

        self.ok_button = wxButton(id=wxID_MSG_WINDOWOK_BUTTON, label='OK',
              name='ok_button', parent=self, pos=wxPoint(232, 424),
              size=wxSize(112, 32), style=0)
        self.ok_button.SetToolTipString('')
        EVT_BUTTON(self.ok_button, wxID_MSG_WINDOWOK_BUTTON,
              self.OnOk_buttonButton)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.init_funcs(parent)

    def OnMsg_windowClose(self, event):
        self.parent.OnCMD_close(event, self)

    def OnOk_buttonButton(self, event):
        self.parent.OnCMD_save(event, self)
        self.parent.OnUtil_clear_frame(self.title)
        self.Destroy()
        util.g_observer.publish(util.OB_EVT_WINDOWS_CLOSE)

    def OnUtil_get_content(self):
        msg_lst = []

        text = self.msg_text.GetValue()
        if text != "":
            msg_lst = text.split("\n")

        return msg_lst

    def init_funcs(self, parent):
        #parent window node
        self.parent = parent

        #window title
        self.title = parent.select_node_label
        self.SetTitle(self.title)

        #if initialize finished or not
        self.init_finised = False

        #the msg is changed status
        self.is_changed = False

        self.Maximize(true)

        #msg tpl disc
        self.msg_tpl_disc = parent.msg_disc

        #show text msg template
        self.init_msg(self.title)

        self.init_finised = True

    def init_msg(self, title=""):
        if title == "":
            util.TRACE("[%s.%s] input param is incorrect!"%(__name__, util.func()))

        tpl_msg = ""

        if title in self.msg_tpl_disc.keys():
            line_lst = self.msg_tpl_disc[title]
            for line in line_lst:
                tpl_msg = tpl_msg + line + "\n"

        self.msg_text.SetValue(tpl_msg)

    def OnMsg_textText(self, event):
        if self.init_finised == True:
            self.is_changed = True
            self.SetTitle(self.title + "*")
            util.g_observer.publish(util.OB_EVT_WINDOWS_CHANGED)

