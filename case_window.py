# -* - coding: UTF-8 -* -
#Boa:MDIChild:case_window
from module import *
import util
import msg_dialog


def create(parent):
    return case_window(parent)

[wxID_CASE_WINDOW, wxID_CASE_WINDOWCASE_GRID, 
] = map(lambda _init_ctrls: wxNewId(), range(2))

[wxID_CASE_WINDOWCASEITEM_DELETE, wxID_CASE_WINDOWCASEITEM_INSERT, 
 wxID_CASE_WINDOWCASEITEM_MSG, 
] = map(lambda _init_coll_Case_Items: wxNewId(), range(3))

class case_window(wxMDIChildFrame):
    def _init_coll_Case_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='', id=wxID_CASE_WINDOWCASEITEM_INSERT,
              item='Insert', kind=wxITEM_NORMAL)
        parent.Append(helpString='', id=wxID_CASE_WINDOWCASEITEM_DELETE,
              item='Delete', kind=wxITEM_NORMAL)
        parent.Append(helpString='', id=wxID_CASE_WINDOWCASEITEM_MSG,
              item='Msg', kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_CASE_WINDOWCASEITEM_INSERT,
              self.OnCaseItem_insertMenu)
        EVT_MENU(self, wxID_CASE_WINDOWCASEITEM_DELETE,
              self.OnCaseItem_deleteMenu)
        EVT_MENU(self, wxID_CASE_WINDOWCASEITEM_MSG, self.OnCaseItem_msgMenu)

    def _init_utils(self):
        # generated method, don't edit
        self.Case = wxMenu(title='')

        self._init_coll_Case_Items(self.Case)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxMDIChildFrame.__init__(self, id=wxID_CASE_WINDOW, name='case_window',
              parent=prnt, pos=wxPoint(0, 0), size=wxSize(600, 400),
              style=wxDEFAULT_FRAME_STYLE, title='')
        self._init_utils()
        self.SetClientSize(wxSize(324, 247))
        self.SetIcon(wxIcon('./image/new_case.ico',
              wxBITMAP_TYPE_ICO))
        self.SetToolTipString('')
        EVT_CLOSE(self, self.OnCase_windowClose)

        self.case_grid = wxGrid(id=wxID_CASE_WINDOWCASE_GRID, name='case_grid',
              parent=self, pos=wxPoint(0, 0), size=wxSize(328, 248),
              style=wxWANTS_CHARS)
        self.case_grid.SetColLabelSize(20)
        self.case_grid.SetRowLabelSize(20)
        self.case_grid.SetToolTipString('')
        self.case_grid.SetDefaultColSize(20)
        EVT_GRID_CELL_LEFT_DCLICK(self.case_grid,
              self.OnCase_gridGridCellLeftDclick)
        EVT_GRID_CELL_CHANGE(self.case_grid, self.OnCase_gridGridCellChange)
        EVT_GRID_CELL_RIGHT_CLICK(self.case_grid,
              self.OnCase_gridGridCellRightClick)
        EVT_GRID_LABEL_RIGHT_CLICK(self.case_grid,
              self.OnCase_gridGridLabelRightClick)
        EVT_GRID_LABEL_LEFT_CLICK(self.case_grid,
              self.OnCase_gridGridLabelLeftClick)
        EVT_KEY_DOWN(self.case_grid, self.OnCase_gridKeyDown)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.init_funcs(parent)

    def OnCase_windowClose(self, event):
        self.parent.OnCMD_close(event, self)

    def OnCase_gridGridCellLeftDclick(self, event):
        self.select_row = event.GetRow()
        self.OnCMD_show_msg(event)

    def OnCase_gridGridCellChange(self, event):
        self.is_changed = True
        self.SetTitle(self.title + "*")
        util.g_observer.publish(util.OB_EVT_WINDOWS_CHANGED)

        col = event.GetCol()
        row = event.GetRow()

        #if the column of the msg template changed
        if col == 2:
            if self.selfdef_msg_disc.has_key(row):
                del self.selfdef_msg_disc[row]

    def OnCase_gridGridCellRightClick(self, event):
        self.case_grid.PopupMenu(self.Case, event.GetPosition())

    def OnCase_gridGridLabelRightClick(self, event):
        self.case_grid.PopupMenu(self.Case, event.GetPosition())

    def OnCase_gridGridLabelLeftClick(self, event):
        row = event.GetRow()

        if event.ControlDown() == TRUE:
            self.case_grid.SelectRow(row, addToSelected = TRUE)
        elif event.ShiftDown() == TRUE:
            pos = self.case_grid.GetSelectedRows()
            if len(pos) == 0:
                pos.append(row)
            self.case_grid.SelectRow(pos[0])
            if pos[0] <= row:
                for i in range(pos[0]+1,row+1):
                    self.case_grid.SelectRow(i, addToSelected = TRUE)
            else:
                for i in range(row,pos[0]):
                    self.case_grid.SelectRow(i, addToSelected = TRUE)
        else:
            self.case_grid.SelectRow(row)

    def OnCase_gridKeyDown(self, event):
        #return directly, so if come into edit status, need double keydown butn't once keydown
        return

    def OnCaseItem_insertMenu(self, event):
        pos = self.case_grid.GetSelectedRows()
        insert_num = len(pos)

        #if it's not selected by label column
        if insert_num == 0:
            cur_row = self.case_grid.GetGridCursorRow()
            pos.append(cur_row)
        pos.sort()

        idx = 0
        for row in pos:
            self.case_grid.InsertRows(row+idx)

            self.case_grid.SetCellValue(row+idx, 3, "")

            row_num = self.case_grid.GetNumberRows()
            for row in range(row_num-1, row+idx-1, -1):
                if self.selfdef_msg_disc.has_key(row):
                    temp_value = self.selfdef_msg_disc[row]
                    del self.selfdef_msg_disc[row]
                    self.selfdef_msg_disc[row+1] = temp_value
            idx = idx + 1

        self.is_changed = True
        self.SetTitle(self.title + "*")
        util.g_observer.publish(util.OB_EVT_WINDOWS_CHANGED)

    def OnCaseItem_deleteMenu(self, event):
        pos = self.case_grid.GetSelectedRows()
        del_num = len(pos)

        #if it's not selected by label column
        if del_num == 0:
            cur_row = self.case_grid.GetGridCursorRow()
            pos.append(cur_row)
        row_num = self.case_grid.GetNumberRows()
        pos.sort()

        idx = 0
        for row in pos:
            self.case_grid.DeleteRows(row-idx)
            self.case_grid.AppendRows(1)

            self.case_grid.SetCellValue(row_num-1, 3, "")

            if self.selfdef_msg_disc.has_key(row-idx):
                del self.selfdef_msg_disc[row-idx]

            for tmp_row in range(row-idx+1, row_num):
                if self.selfdef_msg_disc.has_key(tmp_row):
                    temp_value = self.selfdef_msg_disc[tmp_row]
                    del self.selfdef_msg_disc[tmp_row]
                    self.selfdef_msg_disc[tmp_row-1] = temp_value
            idx = idx + 1

        self.is_changed = True
        self.SetTitle(self.title + "*")
        util.g_observer.publish(util.OB_EVT_WINDOWS_CHANGED)

    def OnCaseItem_msgMenu(self, event):
        self.select_row = self.case_grid.GetGridCursorRow()
        self.OnCMD_show_msg(event)

    def OnCMD_show_msg(self, event):
        select_action = self.case_grid.GetCellValue(self.select_row, 1)
        if (select_action != "recv_rtp" and select_action != "send_rtp" \
            and select_action != "send_recv_rtp"):
            self.select_msg_tpl = self.case_grid.GetCellValue(self.select_row, 2)
            frame = msg_dialog.create(self)
            frame.ShowModal()

    def OnUtil_get_content(self):
        row = 0
        row_num = self.case_grid.GetNumberRows()
        script = ""

        for row in range(row_num):
            time = self.case_grid.GetCellValue(row, 0)
            op = self.case_grid.GetCellValue(row, 1)
            msg = self.case_grid.GetCellValue(row, 2)
            enable = self.case_grid.GetCellValue(row, 3)

            is_selfdef_msg = "0"
            true_msg = ""
            script_line = ""

            if op == "wait_msg" or op == "send_msg":
                if msg in self.msg_name_lst:
                    true_msg = msg
                    is_selfdef_msg = "0"
                elif msg == self.selfdef_flag:
                    true_msg = self.selfdef_msg_disc[row]
                    is_selfdef_msg = "1"
                else:
                    continue

            if enable == "":
                continue

            if op == "wait_msg":
                script_line = "com.iad." + op + "(" + is_selfdef_msg + ",'" + true_msg + "'," + time + ")"
            elif op == "send_msg":
                script_line = "com.iad." + op + "(" + is_selfdef_msg + ",'" + true_msg + "')"
            elif op == "delay":
                script_line = "com.iad." + op + "(" + time + ")"
            elif op == "recv_rtp":
                script_line = "com.iad." + op + "(" + ")"
            elif op == "send_rtp":
                script_line = "com.iad." + op + "('" + msg + "')"
            elif op == "send_recv_rtp":
                script_line = "com.iad." + op + "('" + msg + "')"

            script = script + script_line + "\r\n"

        return script

    def OnUtil_save_msg(self, event, frame=None):
        if frame == None:
            return

        text = frame.OnUtil_get_text()
        tpl_msg = ""

        if frame.is_changed == True:
            #if origin use self define msg
            if frame.title == self.selfdef_flag:
                self.selfdef_msg_disc[frame.row] = text
                self.is_changed = True
                self.SetTitle(frame.title + "*")
                util.g_observer.publish(util.OB_EVT_WINDOWS_CHANGED)
            #if origin use template msg
            else:
                #get template msg
                if frame.title in self.msg_tpl_disc.keys():
                    line_lst = self.msg_tpl_disc[frame.title]
                    for line in line_lst:
                        tpl_msg = tpl_msg + line + "\n"
                #if template msg had some changed, think it as self define msg
                if tpl_msg != "" and text != tpl_msg:
                    self.selfdef_msg_disc[frame.row] = text
                    self.case_grid.SetCellValue(frame.row, 2, self.selfdef_flag)
                    self.is_changed = True
                    self.SetTitle(frame.title + "*")
                    util.g_observer.publish(util.OB_EVT_WINDOWS_CHANGED)

    def init_funcs(self, parent):
        #parent window node
        self.parent = parent

        #window title
        self.title = parent.select_node_label
        self.SetTitle(self.title)

        self.Maximize(true)

        #the case is changed status
        self.is_changed = False

        #msg tpl disc
        self.msg_tpl_disc = parent.msg_disc

        #self define msg disc
        self.selfdef_msg_disc = {}
        #self define flag
        self.selfdef_flag = "self define"

        #msg template name list
        self.msg_name_lst = []

        #the current selected msg template and row number
        self.select_msg_tpl = ""
        self.select_row = 0

        #init grid
        self.init_grid()

        #show the case file
        self.init_case(self.title)

    def init_grid(self):
        self.case_grid.CreateGrid(20,4)

        self.case_grid.SetFont(wxFont(20, wxSWISS, wxNORMAL, wxNORMAL, False,
              'Arial Black'))
        self.case_grid.SetDefaultCellFont(wxFont(9, wxSWISS, wxNORMAL, wxBOLD,
              False, 'Rockwell'))
        self.case_grid.SetDefaultCellTextColour(wxColour(0, 0, 128))
        self.case_grid.SetGridLineColour(wxColour(128, 128, 255))

        self.case_grid.SetColSize(0,100)
        self.case_grid.SetColSize(1,100)
        self.case_grid.SetColSize(2,300)
        self.case_grid.SetColSize(3,50)
        self.case_grid.SetMargins(0,0)

        self.case_grid.SetColLabelValue(0, "time")
        self.case_grid.SetColLabelValue(1, "op")
        self.case_grid.SetColLabelValue(2, "msg")
        self.case_grid.SetColLabelValue(3, "enable")
        self.case_grid.SetDefaultCellAlignment(wxALIGN_CENTRE ,wxALIGN_BOTTOM)

        attr0 = wxGridCellAttr()
        self.cell0 = wxGridCellNumberEditor(min = 0, max = 9999)
        attr0.SetEditor(self.cell0)
        self.case_grid.SetColAttr(0, attr0)

        attr1 = wxGridCellAttr()
        act1 = "wait_msg,send_msg,delay,recv_rtp,send_rtp,send_recv_rtp"
        self.cell1 = wxGridCellChoiceEditor()
        attr1.SetEditor(self.cell1)
        self.case_grid.SetColAttr(1, attr1)
        self.cell1.SetParameters(act1)

        attr2 = wxGridCellAttr()
        act2 = ""
        #add msg template list
        self.msg_name_lst = self.msg_tpl_disc.keys()
        for key in self.msg_name_lst:
            act2 = act2 + key
            act2 = act2 + ","
        #add self define msg flag
        act2 = act2 + self.selfdef_flag
        act2 = act2 + ","
        #add rtp file list
        os.chdir(self.parent.rtp_dir)
        rtp_lst = os.listdir(self.parent.rtp_dir)
        rtp_lst.sort()
        for key in rtp_lst:
            act2 = act2 + key
            act2 = act2 + ","
        os.chdir(self.parent.home_dir)
        self.cell2 = wxGridCellChoiceEditor()
        attr2.SetEditor(self.cell2)
        self.case_grid.SetColAttr(2, attr2)
        self.cell2.SetParameters(act2)

        attr3 = wxGridCellAttr()
        self.cell3 = wxGridCellBoolEditor()
        attr3.SetEditor(self.cell3)
        self.cell3 = wxGridCellBoolRenderer()
        attr3.SetRenderer(self.cell3)
        self.case_grid.SetColAttr(3, attr3)

    def init_case(self, name=""):
        if name == "":
            util.TRACE("[%s.%s] input param is incorrect!"%(__name__, util.func()))

        #first clear grid
        self.case_grid.ClearGrid()
        row_num = self.case_grid.GetNumberRows()

        method_rule = r"com.iad\.(.+)\((.+)\)"
        param2_rule = r"(.+)\,(.+)"
        param3_rule = r"(.+)\,(.+)\,(.+)"

        is_enable = True
        row = 0

        dir = self.parent.case_dir + "\\" + name + ".py"
        fp = open(dir, "r")
        while 1:
            line = fp.readline()
            if line == "":
                break

            if line[0] == "#":
                is_enable = False
                line = line[1:]

            m = re.match(method_rule, line)
            if m != None:
                method = m.group(1)
                param = m.group(2)
                #wait_msg method
                if method == "wait_msg":
                    self.case_grid.SetCellValue(row, 1, "wait_msg")
                    m2 = re.match(param3_rule, param)
                    if m2 != None:
                        type = m2.group(1)
                        msg = m2.group(2)
                        msg = util.strip_quote(msg)
                        time = m2.group(3)
                        if type == "0":
                            if msg in self.msg_name_lst:
                                self.case_grid.SetCellValue(row, 2, msg)
                        elif type == "1":
                            self.case_grid.SetCellValue(row, 2, self.selfdef_flag)
                            self.selfdef_msg_disc[row] = msg
                        self.case_grid.SetCellValue(row, 0, time)
                #send_msg method
                elif method == "send_msg":
                    self.case_grid.SetCellValue(row, 1, "send_msg")
                    m2 = re.match(param2_rule, param)
                    if m2 != None:
                        type = m2.group(1)
                        msg = m2.group(2)
                        msg = util.strip_quote(msg)
                        if type == "0":
                            if msg in self.msg_name_lst:
                                self.case_grid.SetCellValue(row, 2, msg)
                        elif type == "1":
                            self.case_grid.SetCellValue(row, 2, self.selfdef_flag)
                            self.selfdef_msg_disc[row] = msg
                        self.case_grid.SetCellValue(row, 0, "0")
                #delay method
                elif method == "delay":
                    self.case_grid.SetCellValue(row, 1, "delay")
                    time = param.strip()
                    self.case_grid.SetCellValue(row, 0, time)
                #recv_rtp method
                elif method == "recv_rtp":
                    self.case_grid.SetCellValue(row, 0, "0")
                    self.case_grid.SetCellValue(row, 1, "recv_rtp")
                #send_rtp method
                elif method == "send_rtp":
                    self.case_grid.SetCellValue(row, 0, "0")
                    self.case_grid.SetCellValue(row, 1, "send_rtp")
                    param = util.strip_quote(param)
                    self.case_grid.SetCellValue(row, 2, param)
                #send_recv_rtp method
                elif method == "send_recv_rtp":
                    self.case_grid.SetCellValue(row, 0, "0")
                    self.case_grid.SetCellValue(row, 1, "send_recv_rtp")
                    param = util.strip_quote(param)
                    self.case_grid.SetCellValue(row, 2, param)

                if is_enable == True:
                    self.case_grid.SetCellValue(row, 3, "1")
                else:
                    self.case_grid.SetCellValue(row, 3, "")

                if row > row_num:
                    self.case_grid.AppendRows(5)
                    for idx in range(row, row+5):
                        self.case_grid.SetCellValue(idx, 3, "")
                    row_num = self.case_grid.GetNumberRows()

                row = row + 1

