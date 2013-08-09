# -* - coding: UTF-8 -* -
#Boa:MDIChild:device_window
from module import *
import util


def create(parent):
    return device_window(parent)

[wxID_DEVICE_WINDOW, wxID_DEVICE_WINDOWLOCAL_IP_LABEL, 
 wxID_DEVICE_WINDOWLOCAL_IP_TEXT, wxID_DEVICE_WINDOWLOCAL_NUMBER_LABEL, 
 wxID_DEVICE_WINDOWLOCAL_NUMBER_TEXT, wxID_DEVICE_WINDOWLOCAL_PORT_LABEL, 
 wxID_DEVICE_WINDOWLOCAL_PORT_TEXT, wxID_DEVICE_WINDOWLOCAL_RTP_IP_LABEL, 
 wxID_DEVICE_WINDOWLOCAL_RTP_IP_TEXT, wxID_DEVICE_WINDOWLOCAL_RTP_PORT_LABEL, 
 wxID_DEVICE_WINDOWLOCAL_RTP_PORT_TEXT, wxID_DEVICE_WINDOWOK_BUTTON, 
 wxID_DEVICE_WINDOWREMOTE_IP_LABEL, wxID_DEVICE_WINDOWREMOTE_IP_TEXT, 
 wxID_DEVICE_WINDOWREMOTE_NUMBER_LABEL, wxID_DEVICE_WINDOWREMOTE_NUMBER_TEXT, 
 wxID_DEVICE_WINDOWREMOTE_PORT_LABEL, wxID_DEVICE_WINDOWREMOTE_PORT_TEXT, 
 wxID_DEVICE_WINDOWREMOTE_RTP_IP_LABEL, wxID_DEVICE_WINDOWREMOTE_RTP_IP_TEXT, 
 wxID_DEVICE_WINDOWREMOTE_RTP_PORT_LABEL, 
 wxID_DEVICE_WINDOWREMOTE_RTP_PORT_TEXT, 
] = map(lambda _init_ctrls: wxNewId(), range(22))

class device_window(wxMDIChildFrame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxMDIChildFrame.__init__(self, id=wxID_DEVICE_WINDOW,
              name='device_window', parent=prnt, pos=wxPoint(449, 277),
              size=wxSize(376, 588), style=wxDEFAULT_FRAME_STYLE,
              title='device config')
        self.SetClientSize(wxSize(368, 561))
        self.SetToolTipString('')
        EVT_CLOSE(self, self.OnDevice_windowClose)

        self.local_number_label = wxStaticText(id=wxID_DEVICE_WINDOWLOCAL_NUMBER_LABEL,
              label='local_number', name='local_number_label', parent=self,
              pos=wxPoint(48, 16), size=wxSize(88, 20), style=wxALIGN_RIGHT)
        self.local_number_label.SetToolTipString('')

        self.local_number_text = wxTextCtrl(id=wxID_DEVICE_WINDOWLOCAL_NUMBER_TEXT,
              name='local_number_text', parent=self, pos=wxPoint(144, 16),
              size=wxSize(150, 20), style=0, value='')
        self.local_number_text.SetToolTipString('')
        EVT_TEXT(self.local_number_text, wxID_DEVICE_WINDOWLOCAL_NUMBER_TEXT,
              self.OnLocal_number_textText)

        self.local_ip_label = wxStaticText(id=wxID_DEVICE_WINDOWLOCAL_IP_LABEL,
              label='local_ip', name='local_ip_label', parent=self,
              pos=wxPoint(48, 64), size=wxSize(88, 20), style=wxALIGN_RIGHT)
        self.local_ip_label.SetToolTipString('')

        self.local_ip_text = wxTextCtrl(id=wxID_DEVICE_WINDOWLOCAL_IP_TEXT,
              name='local_ip_text', parent=self, pos=wxPoint(144, 64),
              size=wxSize(150, 20), style=0, value='')
        self.local_ip_text.SetToolTipString('')
        EVT_TEXT(self.local_ip_text, wxID_DEVICE_WINDOWLOCAL_IP_TEXT,
              self.OnLocal_ip_textText)

        self.local_port_label = wxStaticText(id=wxID_DEVICE_WINDOWLOCAL_PORT_LABEL,
              label='local_port', name='local_port_label', parent=self,
              pos=wxPoint(56, 112), size=wxSize(80, 20), style=wxALIGN_RIGHT)
        self.local_port_label.SetToolTipString('')

        self.local_port_text = wxTextCtrl(id=wxID_DEVICE_WINDOWLOCAL_PORT_TEXT,
              name='local_port_text', parent=self, pos=wxPoint(144, 112),
              size=wxSize(150, 20), style=0, value='')
        self.local_port_text.SetToolTipString('')
        EVT_TEXT(self.local_port_text, wxID_DEVICE_WINDOWLOCAL_PORT_TEXT,
              self.OnLocal_port_textText)

        self.local_rtp_ip_label = wxStaticText(id=wxID_DEVICE_WINDOWLOCAL_RTP_IP_LABEL,
              label='local_rtp_ip', name='local_rtp_ip_label', parent=self,
              pos=wxPoint(56, 160), size=wxSize(80, 16), style=wxALIGN_RIGHT)
        self.local_rtp_ip_label.SetToolTipString('')

        self.local_rtp_ip_text = wxTextCtrl(id=wxID_DEVICE_WINDOWLOCAL_RTP_IP_TEXT,
              name='local_rtp_ip_text', parent=self, pos=wxPoint(144, 160),
              size=wxSize(152, 22), style=0, value='')
        self.local_rtp_ip_text.SetToolTipString('')
        EVT_TEXT(self.local_rtp_ip_text, wxID_DEVICE_WINDOWLOCAL_RTP_IP_TEXT,
              self.OnLocal_rtp_ip_textText)

        self.local_rtp_port_label = wxStaticText(id=wxID_DEVICE_WINDOWLOCAL_RTP_PORT_LABEL,
              label='local_rtp_port', name='local_rtp_port_label', parent=self,
              pos=wxPoint(40, 216), size=wxSize(96, 20), style=wxALIGN_RIGHT)
        self.local_rtp_port_label.SetToolTipString('')

        self.local_rtp_port_text = wxTextCtrl(id=wxID_DEVICE_WINDOWLOCAL_RTP_PORT_TEXT,
              name='local_rtp_port_text', parent=self, pos=wxPoint(144, 216),
              size=wxSize(150, 20), style=0, value='')
        self.local_rtp_port_text.SetToolTipString('')
        EVT_TEXT(self.local_rtp_port_text,
              wxID_DEVICE_WINDOWLOCAL_RTP_PORT_TEXT,
              self.OnLocal_rtp_port_textText)

        self.remote_number_label = wxStaticText(id=wxID_DEVICE_WINDOWREMOTE_NUMBER_LABEL,
              label='remote_number', name='remote_number_label', parent=self,
              pos=wxPoint(48, 264), size=wxSize(88, 20), style=wxALIGN_RIGHT)
        self.remote_number_label.SetToolTipString('')

        self.remote_number_text = wxTextCtrl(id=wxID_DEVICE_WINDOWREMOTE_NUMBER_TEXT,
              name='remote_number_text', parent=self, pos=wxPoint(144, 264),
              size=wxSize(150, 20), style=0, value='')
        self.remote_number_text.SetToolTipString('')
        EVT_TEXT(self.remote_number_text, wxID_DEVICE_WINDOWREMOTE_NUMBER_TEXT,
              self.OnRemote_number_textText)

        self.remote_ip_label = wxStaticText(id=wxID_DEVICE_WINDOWREMOTE_IP_LABEL,
              label='remote_ip', name='remote_ip_label', parent=self,
              pos=wxPoint(56, 312), size=wxSize(80, 20), style=wxALIGN_RIGHT)
        self.remote_ip_label.SetToolTipString('')

        self.remote_ip_text = wxTextCtrl(id=wxID_DEVICE_WINDOWREMOTE_IP_TEXT,
              name='remote_ip_text', parent=self, pos=wxPoint(144, 312),
              size=wxSize(150, 20), style=0, value='')
        self.remote_ip_text.SetToolTipString('')
        EVT_TEXT(self.remote_ip_text, wxID_DEVICE_WINDOWREMOTE_IP_TEXT,
              self.OnRemote_ip_textText)

        self.remote_port_label = wxStaticText(id=wxID_DEVICE_WINDOWREMOTE_PORT_LABEL,
              label='remote_port', name='remote_port_label', parent=self,
              pos=wxPoint(48, 364), size=wxSize(88, 20), style=wxALIGN_RIGHT)
        self.remote_port_label.SetToolTipString('')

        self.remote_port_text = wxTextCtrl(id=wxID_DEVICE_WINDOWREMOTE_PORT_TEXT,
              name='remote_port_text', parent=self, pos=wxPoint(144, 360),
              size=wxSize(150, 20), style=0, value='')
        self.remote_port_text.SetToolTipString('')
        EVT_TEXT(self.remote_port_text, wxID_DEVICE_WINDOWREMOTE_PORT_TEXT,
              self.OnRemote_port_textText)

        self.remote_rtp_ip_label = wxStaticText(id=wxID_DEVICE_WINDOWREMOTE_RTP_IP_LABEL,
              label='remote_rtp_ip', name='remote_rtp_ip_label', parent=self,
              pos=wxPoint(56, 408), size=wxSize(78, 16), style=wxALIGN_RIGHT)
        self.remote_rtp_ip_label.SetToolTipString('')

        self.remote_rtp_ip_text = wxTextCtrl(id=wxID_DEVICE_WINDOWREMOTE_RTP_IP_TEXT,
              name='remote_rtp_ip_text', parent=self, pos=wxPoint(144, 408),
              size=wxSize(152, 24), style=0, value='')
        self.remote_rtp_ip_text.SetToolTipString('')
        EVT_TEXT(self.remote_rtp_ip_text, wxID_DEVICE_WINDOWREMOTE_RTP_IP_TEXT,
              self.OnRemote_rtp_ip_textText)

        self.remote_rtp_port_label = wxStaticText(id=wxID_DEVICE_WINDOWREMOTE_RTP_PORT_LABEL,
              label='remote_rtp_port', name='remote_rtp_port_label',
              parent=self, pos=wxPoint(48, 464), size=wxSize(90, 24),
              style=wxALIGN_RIGHT)
        self.remote_rtp_port_label.SetToolTipString('')

        self.remote_rtp_port_text = wxTextCtrl(id=wxID_DEVICE_WINDOWREMOTE_RTP_PORT_TEXT,
              name='remote_rtp_port_text', parent=self, pos=wxPoint(144, 464),
              size=wxSize(152, 22), style=0, value='')
        self.remote_rtp_port_text.SetToolTipString('')
        EVT_TEXT(self.remote_rtp_port_text,
              wxID_DEVICE_WINDOWREMOTE_RTP_PORT_TEXT,
              self.OnRemote_rtp_port_textText)

        self.ok_button = wxButton(id=wxID_DEVICE_WINDOWOK_BUTTON, label='OK',
              name='ok_button', parent=self, pos=wxPoint(144, 512),
              size=wxSize(87, 32), style=0)
        self.ok_button.SetToolTipString('')
        EVT_BUTTON(self.ok_button, wxID_DEVICE_WINDOWOK_BUTTON,
              self.OnOk_buttonButton)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.init_funcs(parent)

    def OnDevice_windowClose(self, event):
        self.parent.OnCMD_close(event, self)

    def OnOk_buttonButton(self, event):
        self.parent.OnCMD_save(event, self)
        self.parent.OnUtil_clear_frame(self.title)
        self.Destroy()
        util.g_observer.publish(util.OB_EVT_WINDOWS_CLOSE)

    def OnUtil_get_content(self):
        local_number = self.local_number_text.GetValue()
        local_ip = self.local_ip_text.GetValue()
        local_port = self.local_port_text.GetValue()
        local_rtp_ip = self.local_rtp_ip_text.GetValue()
        local_rtp_port = self.local_rtp_port_text.GetValue()
        remote_number = self.remote_number_text.GetValue()
        remote_ip = self.remote_ip_text.GetValue()
        remote_port = self.remote_port_text.GetValue()
        remote_rtp_ip = self.remote_rtp_ip_text.GetValue()
        remote_rtp_port = self.remote_rtp_port_text.GetValue()

        return eval(local_number), local_ip, eval(local_port), local_rtp_ip, eval(local_rtp_port), \
            eval(remote_number), remote_ip, eval(remote_port), remote_rtp_ip, eval(remote_rtp_port)

    def init_funcs(self, parent):
        #parent window node
        self.parent = parent

        #window title
        self.title = parent.select_node_label
        self.SetTitle(self.title)

        #if initialize finished or not
        self.init_finised = False

        #the device is changed status
        self.is_changed = False

        self.Maximize(true)

        #show device config
        self.init_device()

        self.init_finised = True

    def init_device(self):
        (local_number, local_ip, local_port, local_rtp_ip, local_rtp_port, remote_number, \
            remote_ip, remote_port, remote_rtp_ip, remote_rtp_port) = util.get_device_info()

        if local_number != 0:
            self.local_number_text.SetValue(str(local_number))

        if local_ip != "":
            self.local_ip_text.SetValue(local_ip)

        if local_port != 0:
            self.local_port_text.SetValue(str(local_port))

        if local_rtp_ip != "":
            self.local_rtp_ip_text.SetValue(local_rtp_ip)

        if local_rtp_port != 0:
            self.local_rtp_port_text.SetValue(str(local_rtp_port))

        if remote_number != 0:
            self.remote_number_text.SetValue(str(remote_number))

        if remote_ip != "":
            self.remote_ip_text.SetValue(remote_ip)

        if remote_port != 0:
            self.remote_port_text.SetValue(str(remote_port))

        if remote_rtp_ip != "":
            self.remote_rtp_ip_text.SetValue(remote_rtp_ip)

        if remote_rtp_port != 0:
            self.remote_rtp_port_text.SetValue(str(remote_rtp_port))

    def OnLocal_number_textText(self, event):
        self.OnCMD_Changed(event)

    def OnLocal_ip_textText(self, event):
        self.OnCMD_Changed(event)

    def OnLocal_port_textText(self, event):
        self.OnCMD_Changed(event)

    def OnLocal_rtp_ip_textText(self, event):
        self.OnCMD_Changed(event)

    def OnLocal_rtp_port_textText(self, event):
        self.OnCMD_Changed(event)

    def OnRemote_number_textText(self, event):
        self.OnCMD_Changed(event)

    def OnRemote_ip_textText(self, event):
        self.OnCMD_Changed(event)

    def OnRemote_port_textText(self, event):
        self.OnCMD_Changed(event)

    def OnRemote_rtp_ip_textText(self, event):
        self.OnCMD_Changed(event)

    def OnRemote_rtp_port_textText(self, event):
        self.OnCMD_Changed(event)

    def OnCMD_Changed(self, event):
        if self.init_finised == True:
            self.is_changed = True
            self.SetTitle(self.title + "*")
            util.g_observer.publish(util.OB_EVT_WINDOWS_CHANGED)

