#Boa:Dialog:msg_dialog

from wxPython.wx import *
import util


def create(parent):
    return msg_dialog(parent)

[wxID_MSG_DIALOG, wxID_MSG_DIALOGMSG_TEXT, wxID_MSG_DIALOGOK_BUTTON, 
] = map(lambda _init_ctrls: wxNewId(), range(3))

class msg_dialog(wxDialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxDialog.__init__(self, id=wxID_MSG_DIALOG, name='msg_dialog',
              parent=prnt, pos=wxPoint(394, 248), size=wxSize(632, 499),
              style=wxDEFAULT_DIALOG_STYLE, title='msg')
        self.SetClientSize(wxSize(624, 472))
        self.SetToolTipString('')

        self.msg_text = wxTextCtrl(id=wxID_MSG_DIALOGMSG_TEXT, name='msg_text',
              parent=self, pos=wxPoint(8, 8), size=wxSize(600, 400),
              style=wxHSCROLL | wxVSCROLL | wxTE_MULTILINE, value='')
        self.msg_text.SetToolTipString('')
        EVT_TEXT(self.msg_text, wxID_MSG_DIALOGMSG_TEXT, self.OnMsg_textText)

        self.ok_button = wxButton(id=wxID_MSG_DIALOGOK_BUTTON, label='OK',
              name='ok_button', parent=self, pos=wxPoint(240, 424),
              size=wxSize(128, 32), style=0)
        self.ok_button.SetToolTipString('')
        EVT_BUTTON(self.ok_button, wxID_MSG_DIALOGOK_BUTTON,
              self.OnOk_buttonButton)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.init_funcs(parent)

    def init_funcs(self, parent):
        #parent window node
        self.parent = parent

        #window title
        self.title = parent.select_msg_tpl
        self.row = parent.select_row
        self.SetTitle(self.title)

        #if initialize finished or not
        self.init_finised = False

        #the msg dialog is changed status
        self.is_changed = False

        #msg tpl disc
        self.msg_tpl_disc = parent.msg_tpl_disc

        #show text msg template
        self.init_msg(self.title)

        self.init_finised = True

    def init_msg(self, title):
        tpl_msg = ""

        #if use self define msg
        if title == self.parent.selfdef_flag:
            tpl_msg = self.parent.selfdef_msg_disc[self.row]
        #if use template msg
        else:
            #get template msg
            if title in self.msg_tpl_disc.keys():
                line_lst = self.msg_tpl_disc[title]
                for line in line_lst:
                    tpl_msg = tpl_msg + line + "\r\n"

        self.msg_text.SetValue(tpl_msg)

    def OnOk_buttonButton(self, event):
        self.parent.OnUtil_save_msg(event, self)
        self.Destroy()

    def OnUtil_get_text(self):
        text = self.msg_text.GetValue()
        return text

    def OnMsg_textText(self, event):
        if self.init_finised == True:
            self.is_changed = True

