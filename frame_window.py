# -* - coding: UTF-8 -* -
#Boa:MDIParent:frame_window
from module import *
import util
import com
import codec
import runner
import case_window
import msg_window
import device_window


def create(parent):
    return frame_window(parent)

[wxID_FRAME_WINDOW, wxID_FRAME_WINDOWBOTTOM_SASHLAYOUTWINDOW, 
 wxID_FRAME_WINDOW_TREE, wxID_FRAME_WINDOWLEFT_SASHLAYOUTWINDOW, 
 wxID_FRAME_WINDOWOUTPUT_TEXT, wxID_FRAME_WINDOWSTATUS_BAR, 
 wxID_FRAME_WINDOWTOOL_BAR, 
] = map(lambda _init_ctrls: wxNewId(), range(7))

[wxID_FRAME_WINDOWFILEITEM_BACKUP, wxID_FRAME_WINDOWFILEITEM_CLEAR, 
 wxID_FRAME_WINDOWFILEITEM_CLOSE, wxID_FRAME_WINDOWFILEITEM_CLOSE_ALL, 
 wxID_FRAME_WINDOWFILEITEM_EXIT, wxID_FRAME_WINDOWFILEITEM_NEW_CASE, 
 wxID_FRAME_WINDOWFILEITEM_NEW_MSG, wxID_FRAME_WINDOWFILEITEM_SAVE, 
 wxID_FRAME_WINDOWFILEITEM_SAVE_ALL, 
] = map(lambda _init_coll_File_Items: wxNewId(), range(9))

[wxID_FRAME_WINDOWWORKITEM_RUN, 
] = map(lambda _init_coll_Work_Items: wxNewId(), range(1))

[wxID_FRAME_WINDOWEDITITEM_COPY, wxID_FRAME_WINDOWEDITITEM_DELETE, 
 wxID_FRAME_WINDOWEDITITEM_PASTE, wxID_FRAME_WINDOWEDITITEM_RENAME, 
] = map(lambda _init_coll_Edit_Items: wxNewId(), range(4))

[wxID_FRAME_WINDOWTOOL_BARTOOL_BACKUP, wxID_FRAME_WINDOWTOOL_BARTOOL_CLEAR, 
 wxID_FRAME_WINDOWTOOL_BARTOOL_CLOSE, wxID_FRAME_WINDOWTOOL_BARTOOL_CLOSE_ALL, 
 wxID_FRAME_WINDOWTOOL_BARTOOL_COPY, wxID_FRAME_WINDOWTOOL_BARTOOL_DELETE, 
 wxID_FRAME_WINDOWTOOL_BARTOOL_NEW_CASE, wxID_FRAME_WINDOWTOOL_BARTOOL_NEW_MSG, 
 wxID_FRAME_WINDOWTOOL_BARTOOL_PASTE, wxID_FRAME_WINDOWTOOL_BARTOOL_RENAME, 
 wxID_FRAME_WINDOWTOOL_BARTOOL_RUN, wxID_FRAME_WINDOWTOOL_BARTOOL_SAVE, 
 wxID_FRAME_WINDOWTOOL_BARTOOL_SAVE_ALL, 
] = map(lambda _init_coll_tool_bar_Tools: wxNewId(), range(13))

[wxID_FRAME_WINDOWTREEITEM_COPY, wxID_FRAME_WINDOWTREEITEM_DELETE, 
 wxID_FRAME_WINDOWTREEITEM_NEW_CASE, wxID_FRAME_WINDOWTREEITEM_NEW_MSG, 
 wxID_FRAME_WINDOWTREEITEM_PASTE, wxID_FRAME_WINDOWTREEITEM_RUN, 
] = map(lambda _init_coll_Tree_Items: wxNewId(), range(6))

class frame_window(wxMDIParentFrame):
    def _init_coll_menu_bar_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.File, title='File')
        parent.Append(menu=self.Edit, title='Edit')
        parent.Append(menu=self.Work, title='Work')

    def _init_coll_image_list_Images(self, parent):
        # generated method, don't edit

        parent.Add(bitmap=wxBitmap('./image/new_case.bmp', wxBITMAP_TYPE_BMP),
              mask=wxNullBitmap)
        parent.Add(bitmap=wxBitmap('./image/new_msg.bmp', wxBITMAP_TYPE_BMP),
              mask=wxNullBitmap)
        parent.Add(bitmap=wxBitmap('./image/save.png', wxBITMAP_TYPE_PNG),
              mask=wxNullBitmap)
        parent.Add(bitmap=wxBitmap('./image/backup.png', wxBITMAP_TYPE_PNG),
              mask=wxNullBitmap)
        parent.Add(bitmap=wxBitmap('./image/close.png', wxBITMAP_TYPE_PNG),
              mask=wxNullBitmap)
        parent.Add(bitmap=wxBitmap('./image/close_all.bmp', wxBITMAP_TYPE_BMP),
              mask=wxNullBitmap)
        parent.Add(bitmap=wxBitmap('./image/copy.png', wxBITMAP_TYPE_PNG),
              mask=wxNullBitmap)
        parent.Add(bitmap=wxBitmap('./image/delete.png', wxBITMAP_TYPE_PNG),
              mask=wxNullBitmap)
        parent.Add(bitmap=wxBitmap('./image/paste.png', wxBITMAP_TYPE_PNG),
              mask=wxNullBitmap)
        parent.Add(bitmap=wxBitmap('./image/rename.png', wxBITMAP_TYPE_PNG),
              mask=wxNullBitmap)
        parent.Add(bitmap=wxBitmap('./image/run.png', wxBITMAP_TYPE_PNG),
              mask=wxNullBitmap)
        parent.Add(bitmap=wxBitmap('./image/save_all.png', wxBITMAP_TYPE_PNG),
              mask=wxNullBitmap)
        parent.Add(bitmap=wxBitmap('./image/clear.png', wxBITMAP_TYPE_PNG),
              mask=wxNullBitmap)
        parent.Add(bitmap=wxBitmap('./image/dir.png', wxBITMAP_TYPE_PNG),
              mask=wxNullBitmap)
        parent.Add(bitmap=wxBitmap('./image/dir_open.bmp', wxBITMAP_TYPE_BMP),
              mask=wxNullBitmap)

    def _init_coll_File_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='', id=wxID_FRAME_WINDOWFILEITEM_NEW_CASE,
              item='New Case', kind=wxITEM_NORMAL)
        parent.Append(helpString='', id=wxID_FRAME_WINDOWFILEITEM_NEW_MSG,
              item='New Msg', kind=wxITEM_NORMAL)
        parent.AppendSeparator()
        parent.Append(helpString='', id=wxID_FRAME_WINDOWFILEITEM_SAVE,
              item='Save', kind=wxITEM_NORMAL)
        parent.Append(helpString='', id=wxID_FRAME_WINDOWFILEITEM_SAVE_ALL,
              item='Save All', kind=wxITEM_NORMAL)
        parent.AppendSeparator()
        parent.Append(helpString='', id=wxID_FRAME_WINDOWFILEITEM_CLOSE,
              item='Close', kind=wxITEM_NORMAL)
        parent.Append(helpString='', id=wxID_FRAME_WINDOWFILEITEM_CLOSE_ALL,
              item='Close All', kind=wxITEM_NORMAL)
        parent.AppendSeparator()
        parent.Append(helpString='', id=wxID_FRAME_WINDOWFILEITEM_BACKUP,
              item='Backup', kind=wxITEM_NORMAL)
        parent.Append(helpString='', id=wxID_FRAME_WINDOWFILEITEM_CLEAR,
              item='Clear', kind=wxITEM_NORMAL)
        parent.AppendSeparator()
        parent.Append(helpString='', id=wxID_FRAME_WINDOWFILEITEM_EXIT,
              item='Exit', kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_FRAME_WINDOWFILEITEM_NEW_CASE,
              self.OnFileItem_new_caseMenu)
        EVT_MENU(self, wxID_FRAME_WINDOWFILEITEM_NEW_MSG,
              self.OnFileItem_new_msgMenu)
        EVT_MENU(self, wxID_FRAME_WINDOWFILEITEM_CLOSE,
              self.OnFileItem_closeMenu)
        EVT_MENU(self, wxID_FRAME_WINDOWFILEITEM_CLOSE_ALL,
              self.OnFileItem_close_allMenu)
        EVT_MENU(self, wxID_FRAME_WINDOWFILEITEM_SAVE, self.OnFileItem_saveMenu)
        EVT_MENU(self, wxID_FRAME_WINDOWFILEITEM_SAVE_ALL,
              self.OnFileItem_save_allMenu)
        EVT_MENU(self, wxID_FRAME_WINDOWFILEITEM_BACKUP,
              self.OnFileItem_backupMenu)
        EVT_MENU(self, wxID_FRAME_WINDOWFILEITEM_CLEAR,
              self.OnFileItem_clearMenu)
        EVT_MENU(self, wxID_FRAME_WINDOWFILEITEM_EXIT, self.OnFileItem_exitMenu)

    def _init_coll_Edit_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='', id=wxID_FRAME_WINDOWEDITITEM_COPY,
              item='Copy', kind=wxITEM_NORMAL)
        parent.Append(helpString='', id=wxID_FRAME_WINDOWEDITITEM_PASTE,
              item='Paste', kind=wxITEM_NORMAL)
        parent.Append(helpString='', id=wxID_FRAME_WINDOWEDITITEM_DELETE,
              item='Delete', kind=wxITEM_NORMAL)
        parent.Append(helpString='', id=wxID_FRAME_WINDOWEDITITEM_RENAME,
              item='Rename', kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_FRAME_WINDOWEDITITEM_COPY, self.OnEditItem_copyMenu)
        EVT_MENU(self, wxID_FRAME_WINDOWEDITITEM_PASTE,
              self.OnEditItem_pasteMenu)
        EVT_MENU(self, wxID_FRAME_WINDOWEDITITEM_DELETE,
              self.OnEditItem_deleteMenu)
        EVT_MENU(self, wxID_FRAME_WINDOWEDITITEM_RENAME,
              self.OnEditItem_renameMenu)

    def _init_coll_Tree_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='', id=wxID_FRAME_WINDOWTREEITEM_NEW_CASE,
              item='New Case', kind=wxITEM_NORMAL)
        parent.Append(helpString='', id=wxID_FRAME_WINDOWTREEITEM_NEW_MSG,
              item='New Msg', kind=wxITEM_NORMAL)
        parent.AppendSeparator()
        parent.Append(helpString='', id=wxID_FRAME_WINDOWTREEITEM_COPY,
              item='Copy', kind=wxITEM_NORMAL)
        parent.Append(helpString='', id=wxID_FRAME_WINDOWTREEITEM_PASTE,
              item='Paste', kind=wxITEM_NORMAL)
        parent.Append(helpString='', id=wxID_FRAME_WINDOWTREEITEM_DELETE,
              item='Delete', kind=wxITEM_NORMAL)
        parent.AppendSeparator()
        parent.Append(helpString='', id=wxID_FRAME_WINDOWTREEITEM_RUN,
              item='Run', kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_FRAME_WINDOWTREEITEM_NEW_CASE,
              self.OnTreeItem_new_caseMenu)
        EVT_MENU(self, wxID_FRAME_WINDOWTREEITEM_NEW_MSG,
              self.OnTreeItem_new_msgMenu)
        EVT_MENU(self, wxID_FRAME_WINDOWTREEITEM_COPY, self.OnTreeItem_copyMenu)
        EVT_MENU(self, wxID_FRAME_WINDOWTREEITEM_PASTE,
              self.OnTreeItem_pasteMenu)
        EVT_MENU(self, wxID_FRAME_WINDOWTREEITEM_DELETE,
              self.OnTreeItem_deleteMenu)
        EVT_MENU(self, wxID_FRAME_WINDOWTREEITEM_RUN, self.OnTreeItem_runMenu)

    def _init_coll_Work_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='', id=wxID_FRAME_WINDOWWORKITEM_RUN,
              item='Run', kind=wxITEM_NORMAL)
        EVT_MENU(self, wxID_FRAME_WINDOWWORKITEM_RUN, self.OnWorkItem_runMenu)

    def _init_coll_tool_bar_Tools(self, parent):
        # generated method, don't edit

        parent.DoAddTool(bitmap=wxBitmap('./image/new_case.bmp',
              wxBITMAP_TYPE_BMP), bmpDisabled=wxBitmap('./image/new_case.bmp',
              wxBITMAP_TYPE_BMP), id=wxID_FRAME_WINDOWTOOL_BARTOOL_NEW_CASE,
              kind=wxITEM_NORMAL, label='New Case', longHelp='',
              shortHelp='New Case')
        parent.DoAddTool(bitmap=wxBitmap('./image/new_msg.bmp',
              wxBITMAP_TYPE_BMP), bmpDisabled=wxBitmap('./image/new_msg.bmp',
              wxBITMAP_TYPE_BMP), id=wxID_FRAME_WINDOWTOOL_BARTOOL_NEW_MSG,
              kind=wxITEM_NORMAL, label='New Msg', longHelp='',
              shortHelp='New Msg')
        parent.DoAddTool(bitmap=wxBitmap('./image/save.png', wxBITMAP_TYPE_PNG),
              bmpDisabled=wxBitmap('./image/save.png', wxBITMAP_TYPE_PNG),
              id=wxID_FRAME_WINDOWTOOL_BARTOOL_SAVE, kind=wxITEM_NORMAL,
              label='Save', longHelp='', shortHelp='Save')
        parent.DoAddTool(bitmap=wxBitmap('./image/save_all.png',
              wxBITMAP_TYPE_PNG), bmpDisabled=wxBitmap('./image/save_all.png',
              wxBITMAP_TYPE_PNG), id=wxID_FRAME_WINDOWTOOL_BARTOOL_SAVE_ALL,
              kind=wxITEM_NORMAL, label='Save All', longHelp='',
              shortHelp='Save All')
        parent.DoAddTool(bitmap=wxBitmap('./image/close.png',
              wxBITMAP_TYPE_PNG), bmpDisabled=wxBitmap('./image/close.png',
              wxBITMAP_TYPE_PNG), id=wxID_FRAME_WINDOWTOOL_BARTOOL_CLOSE,
              kind=wxITEM_NORMAL, label='Close', longHelp='',
              shortHelp='Close')
        parent.DoAddTool(bitmap=wxBitmap('./image/close_all.bmp',
              wxBITMAP_TYPE_BMP), bmpDisabled=wxBitmap('./image/close_all.bmp',
              wxBITMAP_TYPE_BMP), id=wxID_FRAME_WINDOWTOOL_BARTOOL_CLOSE_ALL,
              kind=wxITEM_NORMAL, label='Close All', longHelp='',
              shortHelp='Close All')
        parent.DoAddTool(bitmap=wxBitmap('./image/backup.png',
              wxBITMAP_TYPE_PNG), bmpDisabled=wxBitmap('./image/backup.png',
              wxBITMAP_TYPE_PNG), id=wxID_FRAME_WINDOWTOOL_BARTOOL_BACKUP,
              kind=wxITEM_NORMAL, label='Backup', longHelp='',
              shortHelp='Backup')
        parent.DoAddTool(bitmap=wxBitmap('./image/clear.png',
              wxBITMAP_TYPE_PNG), bmpDisabled=wxBitmap('./image/clear.png',
              wxBITMAP_TYPE_PNG), id=wxID_FRAME_WINDOWTOOL_BARTOOL_CLEAR,
              kind=wxITEM_NORMAL, label='Clear', longHelp='',
              shortHelp='Clear')
        parent.AddSeparator()
        parent.DoAddTool(bitmap=wxBitmap('./image/copy.png', wxBITMAP_TYPE_PNG),
              bmpDisabled=wxBitmap('./image/copy.png', wxBITMAP_TYPE_PNG),
              id=wxID_FRAME_WINDOWTOOL_BARTOOL_COPY, kind=wxITEM_NORMAL,
              label='Copy', longHelp='', shortHelp='Copy')
        parent.DoAddTool(bitmap=wxBitmap('./image/paste.png',
              wxBITMAP_TYPE_PNG), bmpDisabled=wxBitmap('./image/paste.png',
              wxBITMAP_TYPE_PNG), id=wxID_FRAME_WINDOWTOOL_BARTOOL_PASTE,
              kind=wxITEM_NORMAL, label='Paste', longHelp='',
              shortHelp='Paste')
        parent.DoAddTool(bitmap=wxBitmap('./image/delete.png',
              wxBITMAP_TYPE_PNG), bmpDisabled=wxBitmap('./image/delete.png',
              wxBITMAP_TYPE_PNG), id=wxID_FRAME_WINDOWTOOL_BARTOOL_DELETE,
              kind=wxITEM_NORMAL, label='Delete', longHelp='',
              shortHelp='Delete')
        parent.DoAddTool(bitmap=wxBitmap('./image/rename.png',
              wxBITMAP_TYPE_PNG), bmpDisabled=wxBitmap('./image/rename.png',
              wxBITMAP_TYPE_PNG), id=wxID_FRAME_WINDOWTOOL_BARTOOL_RENAME,
              kind=wxITEM_NORMAL, label='Rename', longHelp='',
              shortHelp='Rename')
        parent.AddSeparator()
        parent.DoAddTool(bitmap=wxBitmap('./image/run.png', wxBITMAP_TYPE_PNG),
              bmpDisabled=wxBitmap('./image/run.png', wxBITMAP_TYPE_PNG),
              id=wxID_FRAME_WINDOWTOOL_BARTOOL_RUN, kind=wxITEM_NORMAL,
              label='Run', longHelp='', shortHelp='Run')
        EVT_TOOL(self, wxID_FRAME_WINDOWTOOL_BARTOOL_NEW_CASE,
              self.OnTool_barTool_new_caseTool)
        EVT_TOOL(self, wxID_FRAME_WINDOWTOOL_BARTOOL_NEW_MSG,
              self.OnTool_barTool_new_msgTool)
        EVT_TOOL(self, wxID_FRAME_WINDOWTOOL_BARTOOL_CLOSE,
              self.OnTool_barTool_closeTool)
        EVT_TOOL(self, wxID_FRAME_WINDOWTOOL_BARTOOL_CLOSE_ALL,
              self.OnTool_barTool_close_allTool)
        EVT_TOOL(self, wxID_FRAME_WINDOWTOOL_BARTOOL_SAVE,
              self.OnTool_barTool_saveTool)
        EVT_TOOL(self, wxID_FRAME_WINDOWTOOL_BARTOOL_SAVE_ALL,
              self.OnTool_barTool_save_allTool)
        EVT_TOOL(self, wxID_FRAME_WINDOWTOOL_BARTOOL_BACKUP,
              self.OnTool_barTool_backupTool)
        EVT_TOOL(self, wxID_FRAME_WINDOWTOOL_BARTOOL_CLEAR,
              self.OnTool_barTool_clearTool)
        EVT_TOOL(self, wxID_FRAME_WINDOWTOOL_BARTOOL_COPY,
              self.OnTool_barTool_copyTool)
        EVT_TOOL(self, wxID_FRAME_WINDOWTOOL_BARTOOL_PASTE,
              self.OnTool_barTool_pasteTool)
        EVT_TOOL(self, wxID_FRAME_WINDOWTOOL_BARTOOL_DELETE,
              self.OnTool_barTool_deleteTool)
        EVT_TOOL(self, wxID_FRAME_WINDOWTOOL_BARTOOL_RENAME,
              self.OnTool_barTool_renameTool)
        EVT_TOOL(self, wxID_FRAME_WINDOWTOOL_BARTOOL_RUN,
              self.OnTool_barTool_runTool)

        parent.Realize()

    def _init_coll_status_bar_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(1)

        parent.SetStatusText(i=0, text='')

        parent.SetStatusWidths([-1])

    def _init_utils(self):
        # generated method, don't edit
        self.menu_bar = wxMenuBar()

        self.File = wxMenu(title='')

        self.Edit = wxMenu(title='')

        self.Work = wxMenu(title='')

        self.image_list = wxImageList(height=16, width=16)
        self._init_coll_image_list_Images(self.image_list)

        self.Tree = wxMenu(title='')

        self._init_coll_menu_bar_Menus(self.menu_bar)
        self._init_coll_File_Items(self.File)
        self._init_coll_Edit_Items(self.Edit)
        self._init_coll_Work_Items(self.Work)
        self._init_coll_Tree_Items(self.Tree)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxMDIParentFrame.__init__(self, id=wxID_FRAME_WINDOW,
              name='frame_window', parent=prnt, pos=wxPoint(306, 211),
              size=wxSize(960, 728),
              style=wxDEFAULT_FRAME_STYLE | wxVSCROLL | wxHSCROLL,
              title='iad simulator')
        self._init_utils()
        self.SetClientSize(wxSize(952, 701))
        self.SetMenuBar(self.menu_bar)
        self.SetAutoLayout(True)
        self.SetIcon(wxIcon('./image/iad_simulater.ico',wxBITMAP_TYPE_ICO))
        self.SetToolTipString('')
        EVT_IDLE(self, self.OnFrame_windowIdle)
        EVT_CLOSE(self, self.OnFrame_windowClose)
        EVT_SIZE(self, self.OnFrame_windowSize)

        self.status_bar = wxStatusBar(id=wxID_FRAME_WINDOWSTATUS_BAR,
              name='status_bar', parent=self, style=0)
        self.status_bar.SetToolTipString('')
        self._init_coll_status_bar_Fields(self.status_bar)
        self.SetStatusBar(self.status_bar)

        self.tool_bar = wxToolBar(id=wxID_FRAME_WINDOWTOOL_BAR, name='tool_bar',
              parent=self, pos=wxPoint(0, 0), size=wxSize(952, 27),
              style=wxTB_HORIZONTAL | wxNO_BORDER)
        self.tool_bar.SetToolTipString('')
        self.SetToolBar(self.tool_bar)

        self.left_sashLayoutWindow = wxSashLayoutWindow(id=wxID_FRAME_WINDOWLEFT_SASHLAYOUTWINDOW,
              name='left_sashLayoutWindow', parent=self, pos=wxPoint(0, 54),
              size=wxSize(240, 635), style=wxCLIP_CHILDREN | wxSW_3D)
        self.left_sashLayoutWindow.SetAlignment(wxLAYOUT_LEFT)
        self.left_sashLayoutWindow.SetToolTipString('')
        self.left_sashLayoutWindow.SetSashVisible(wxSASH_RIGHT, True)
        self.left_sashLayoutWindow.SetOrientation(wxLAYOUT_VERTICAL)
        self.left_sashLayoutWindow.SetDefaultSize(wxSize(240, 635))
        EVT_SASH_DRAGGED(self.left_sashLayoutWindow,
              wxID_FRAME_WINDOWLEFT_SASHLAYOUTWINDOW,
              self.OnLeft_sashLayoutWindowSashDragged)

        self.bottom_sashLayoutWindow = wxSashLayoutWindow(id=wxID_FRAME_WINDOWBOTTOM_SASHLAYOUTWINDOW,
              name='bottom_sashLayoutWindow', parent=self, pos=wxPoint(240,
              534), size=wxSize(713, 153), style=wxCLIP_CHILDREN | wxSW_3D)
        self.bottom_sashLayoutWindow.SetAlignment(wxLAYOUT_BOTTOM)
        self.bottom_sashLayoutWindow.SetToolTipString('')
        self.bottom_sashLayoutWindow.SetSashVisible(wxSASH_TOP, True)
        self.bottom_sashLayoutWindow.SetOrientation(wxLAYOUT_HORIZONTAL)
        self.bottom_sashLayoutWindow.SetDefaultSize(wxSize(713, 153))
        EVT_SASH_DRAGGED(self.bottom_sashLayoutWindow,
              wxID_FRAME_WINDOWBOTTOM_SASHLAYOUTWINDOW,
              self.OnBottom_sashLayoutWindowSashDragged)

        self.tree = wxTreeCtrl(id=wxID_FRAME_WINDOW_TREE,
              name='tree', parent=self.left_sashLayoutWindow,
              pos=wxPoint(0, 0), size=wxSize(240, 632),
              style=wxTR_LINES_AT_ROOT | wxTR_SINGLE | wxTR_EDIT_LABELS | wxTR_HAS_BUTTONS | wxTR_HIDE_ROOT)
        self.tree.SetImageList(self.image_list)
        self.tree.SetToolTipString('')
        EVT_TREE_BEGIN_LABEL_EDIT(self.tree, wxID_FRAME_WINDOW_TREE,
              self.OnTreeTreeBeginLabelEdit)
        EVT_TREE_END_LABEL_EDIT(self.tree, wxID_FRAME_WINDOW_TREE,
              self.OnTreeTreeEndLabelEdit)
        EVT_TREE_ITEM_ACTIVATED(self.tree, wxID_FRAME_WINDOW_TREE,
              self.OnTreeTreeItemActivated)
        EVT_TREE_SEL_CHANGED(self.tree, wxID_FRAME_WINDOW_TREE,
              self.OnTreeTreeSelChanged)
        EVT_RIGHT_DOWN(self.tree, self.OnTreeRightDown)

        self.output_text = wxTextCtrl(id=wxID_FRAME_WINDOWOUTPUT_TEXT,
              name='output_text', parent=self.bottom_sashLayoutWindow,
              pos=wxPoint(0, 0), size=wxSize(712, 152),
              style=wxTE_READONLY | wxTE_MULTILINE, value='')
        self.output_text.SetInsertionPoint(0)
        self.output_text.SetToolTipString('')

        self._init_coll_tool_bar_Tools(self.tool_bar)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.init_funcs()

    def OnFrame_windowIdle(self, event):
        log_msg = util.pop_log_msg()

        while len(log_msg)>0:
            if self.curr_log_line < self.max_log_line:
                self.curr_log_line = self.curr_log_line + 1
            else:
                line_length = self.output_text.GetLineLength(0)
                self.output_text.Remove(0, line_length + 2)

            if log_msg[-1] != '\n' and log_msg[-1] != '\r':
                log_msg = log_msg + '\n'
            self.output_text.AppendText(log_msg)

            log_msg = util.pop_log_msg()

    def OnFrame_windowClose(self, event):
        self.OnCMD_save_all(event)
        self.Destroy()

    def OnFrame_windowSize(self, event):
        wxLayoutAlgorithm().LayoutMDIFrame(self)
        self.GetClientWindow().Refresh()

    def OnTool_barTool_new_caseTool(self, event):
        return self.OnCMD_new_case(event)

    def OnTool_barTool_new_msgTool(self, event):
        return self.OnCMD_new_msg(event)

    def OnTool_barTool_closeTool(self, event):
        frame = self.GetActiveChild()
        return self.OnCMD_close(event, frame)

    def OnTool_barTool_close_allTool(self, event):
        return self.OnCMD_close_all(event)

    def OnTool_barTool_saveTool(self, event):
        frame = self.GetActiveChild()
        return self.OnCMD_save(event, frame)

    def OnTool_barTool_save_allTool(self, event):
        return self.OnCMD_save_all(event)

    def OnTool_barTool_backupTool(self, event):
        return self.OnCMD_backup(event)

    def OnTool_barTool_clearTool(self, event):
        return self.OnCMD_clear(event)

    def OnTool_barTool_copyTool(self, event):
        return self.OnCMD_copy(event)

    def OnTool_barTool_pasteTool(self, event):
        return self.OnCMD_paste(event)

    def OnTool_barTool_deleteTool(self, event):
        return self.OnCMD_delete(event)

    def OnTool_barTool_renameTool(self, event):
        return self.OnCMD_rename(event)

    def OnTool_barTool_runTool(self, event):
        return self.OnCMD_run()

    def OnFileItem_new_caseMenu(self, event):
        return self.OnCMD_new_case(event)

    def OnFileItem_new_msgMenu(self, event):
        return self.OnCMD_new_msg(event)

    def OnFileItem_closeMenu(self, event):
        frame = self.GetActiveChild()
        return self.OnCMD_close(event, frame)

    def OnFileItem_close_allMenu(self, event):
        return self.OnCMD_close_all(event)

    def OnFileItem_saveMenu(self, event):
        frame = self.GetActiveChild()
        return self.OnCMD_save(event, frame)

    def OnFileItem_save_allMenu(self, event):
        return self.OnCMD_save_all(event)

    def OnFileItem_backupMenu(self, event):
        return self.OnCMD_backup(event)

    def OnFileItem_clearMenu(self, event):
        return self.OnCMD_clear(event)

    def OnFileItem_exitMenu(self, event):
        self.OnCMD_save_all(event)
        self.Destroy()

    def OnWorkItem_runMenu(self, event):
        return self.OnCMD_run()

    def OnEditItem_copyMenu(self, event):
        return self.OnCMD_copy(event)

    def OnEditItem_pasteMenu(self, event):
        return self.OnCMD_paste(event)

    def OnEditItem_deleteMenu(self, event):
        return self.OnCMD_delete(event)

    def OnEditItem_renameMenu(self, event):
        return self.OnCMD_rename(event)

    def OnLeft_sashLayoutWindowSashDragged(self, event):
        if event.GetDragStatus() == wxSASH_STATUS_OUT_OF_RANGE:
            return

        eID = event.GetId()
        if eID == wxID_FRAME_WINDOWLEFT_SASHLAYOUTWINDOW:
            self.left_sashLayoutWindow.SetDefaultSize(wxSize(event.GetDragRect().width, 0))

        wxLayoutAlgorithm().LayoutMDIFrame(self)
        self.GetClientWindow().Refresh()

    def OnBottom_sashLayoutWindowSashDragged(self, event):
        if event.GetDragStatus() == wxSASH_STATUS_OUT_OF_RANGE:
            return

        eID = event.GetId()
        if eID == wxID_FRAME_WINDOWBOTTOM_SASHLAYOUTWINDOW:
            self.bottom_sashLayoutWindow.SetDefaultSize(wxSize(0, event.GetDragRect().height))

        wxLayoutAlgorithm().LayoutMDIFrame(self)
        self.GetClientWindow().Refresh()

    def OnTreeItem_new_caseMenu(self, event):
        return self.OnCMD_new_case(event)

    def OnTreeItem_new_msgMenu(self, event):
        return self.OnCMD_new_msg(event)

    def OnTreeItem_copyMenu(self, event):
        return self.OnCMD_copy(event)

    def OnTreeItem_pasteMenu(self, event):
        return self.OnCMD_paste(event)

    def OnTreeItem_deleteMenu(self, event):
        return self.OnCMD_delete(event)

    def OnTreeItem_runMenu(self, event):
        return self.OnCMD_run()

    def OnTreeTreeBeginLabelEdit(self, event):
        node = event.GetItem()

        #save the begin edit label of node
        self.begin_edit_node_label = event.GetLabel()

        #get parent node
        parent_node = self.tree.GetItemParent(node)
        if parent_node:
            parent_label = self.tree.GetItemText(parent_node)
            #if case tree node is edited
            if parent_label == self.case_root_label:
                os.chdir(self.case_dir)
                if not os.path.exists(self.begin_edit_node_label + ".py"):
                    fp = open(self.begin_edit_node_label + ".py", "a")
                    fp.write("")
                    fp.close()
                os.chdir(self.home_dir)
                return
            #if msg tree node is edited
            elif parent_label == self.msg_root_label:
                (msg_lst, found) = util.get_msg_tpl(self.begin_edit_node_label)
                if found == False:
                    util.add_msg_tpl(self.begin_edit_node_label)
                return
            #if device tree node cann't be edited
            elif parent_label == self.device_root_label:
                return

    def OnTreeTreeEndLabelEdit(self, event):
        node = event.GetItem()

        #get the end edit label of node
        label = event.GetLabel()

        #get parent node
        parent_node = self.tree.GetItemParent(node)
        if parent_node:
            parent_label = self.tree.GetItemText(parent_node)
            #if case tree node is edited
            if parent_label == self.case_root_label:
                #if user hasn't modify label or modify label to null, the get label is null
                if label != "":
                    os.chdir(self.case_dir)
                    #if already exist same name testcase
                    if os.path.exists(label + ".py"):
                        dlg = wxMessageDialog(self, "it's already had a same name testcase!", 
                            'notice', wxOK | wxCENTRE |wxICON_EXCLAMATION )
                        dlg.ShowModal()
                        dlg.Destroy()
                        event.Veto()
                        self.tree.EditLabel(node)
                    else:
                        os.rename(self.begin_edit_node_label+".py", label+".py")
                        #check the open frame
                        if self.case_frame.has_key(self.begin_edit_node_label):
                            frame = self.case_frame[self.begin_edit_node_label]
                            frame.title = label
                            if frame.is_changed == False:
                                frame.SetTitle(label)
                            else:
                                frame.SetTitle(label + "*")
                            del self.case_frame[self.begin_edit_node_label]
                            self.case_frame[label] = frame
                    os.chdir(self.home_dir)
                    return
                else:
                    event.Veto()
                    return
            #if msg tree node is edited
            elif parent_label == self.msg_root_label:
                #if user hasn't modify label or modify label to null, the get label is null
                if label != "":
                    (msg_lst, found) = util.get_msg_tpl(label)
                    if found == True:
                        dlg = wxMessageDialog(self, "it's already had a same name msg template!!", 
                            'notice', wxOK | wxCENTRE |wxICON_EXCLAMATION )
                        dlg.ShowModal()
                        dlg.Destroy()
                        event.Veto()
                        self.tree.EditLabel(node)
                    else:
                        #backup msg.ini file
                        cfg_file_path = self.home_dir + "\\msg.ini"
                        win32file.CopyFile(cfg_file_path, cfg_file_path + ".bak", False)
                        (msg_lst, found) = util.get_msg_tpl(self.begin_edit_node_label)
                        util.del_msg_tpl(self.begin_edit_node_label)
                        util.add_msg_tpl(label)
                        if found == True:
                            util.set_msg_tpl(label, msg_lst)
                        self.update_msg_tpl()
                        #check the open frame
                        if self.msg_frame.has_key(self.begin_edit_node_label):
                            frame = self.msg_frame[self.begin_edit_node_label]
                            frame.title = label
                            if frame.is_changed == False:
                                frame.SetTitle(label)
                            else:
                                frame.SetTitle(label + "*")
                            del self.msg_frame[self.begin_edit_node_label]
                            self.msg_frame[label] = frame
                else:
                    event.Veto()
                    return
            #if device tree node cann't be edited
            elif parent_label == self.device_root_label:
                return

    def OnTreeTreeItemActivated(self, event):
        #get node that event happen
        node = event.GetItem()

        #get node text
        label = self.tree.GetItemText(node)
        if label == self.case_root_label or label == self.msg_root_label or label == self.device_root_label:
            return

        #get parent node
        parent_node = self.tree.GetItemParent(node)
        if parent_node:
            parent_label = self.tree.GetItemText(parent_node)
            #if case tree node is clicked
            if parent_label == self.case_root_label:
                if not self.case_frame.has_key(label):
                    self.select_node_label = label
                    frame = case_window.create(self)
                    self.case_frame[label] = frame
                    util.g_observer.publish(util.OB_EVT_WINDOWS_CREATE)
                else:
                    self.case_frame[label].Activate()
                return
            #if msg tree node is clicked
            elif parent_label == self.msg_root_label:
                if not self.msg_frame.has_key(label):
                    self.select_node_label = label
                    frame = msg_window.create(self)
                    self.msg_frame[label] = frame
                    util.g_observer.publish(util.OB_EVT_WINDOWS_CREATE)
                else:
                    self.msg_frame[label].Activate()
                return
            #if device tree node is clicked
            elif parent_label == self.device_root_label:
                if self.device_frame == None:
                    self.select_node_label = label
                    frame = device_window.create(self)
                    self.device_frame = frame
                    util.g_observer.publish(util.OB_EVT_WINDOWS_CREATE)
                else:
                    self.device_frame.Activate()
                return

    def OnTreeTreeSelChanged(self, event):
        util.g_observer.publish(util.OB_EVT_TREE_SEL_CHANGED, event)

    def OnTreeRightDown(self, event):
        self.tree.PopupMenu(self.Tree, event.GetPosition())

    def OnCMD_new_case(self, event):
        new_case_seq = 1
        new_case_rule = r"new case([0-9]*)"

        new_case_seq = self.OnUtil_find_usable_seq(self.case_root_node, new_case_rule)

        if new_case_seq > 1:
            new_case_name = "new case" + str(new_case_seq)
        elif new_case_seq == 1:
            new_case_name = "new case"

        #create new case node, and set it to edit status
        node = self.tree.AppendItem(self.case_root_node, new_case_name)
        self.tree.SetItemImage(node, 0, wxTreeItemIcon_Normal)
        self.tree.SetItemImage(node, 0, wxTreeItemIcon_Selected)

        self.tree.EditLabel(node)

    def OnCMD_new_msg(self, event):
        new_msg_seq = 1
        new_msg_rule = r"new msg([0-9]*)"

        new_msg_seq = self.OnUtil_find_usable_seq(self.msg_root_node, new_msg_rule)

        if new_msg_seq > 1:
            new_msg_name = "new msg" + str(new_msg_seq)
        elif new_msg_seq == 1:
            new_msg_name = "new msg"

        #create new msg node, and set it to edit status
        node = self.tree.AppendItem(self.msg_root_node, new_msg_name)
        self.tree.SetItemImage(node, 0, wxTreeItemIcon_Normal)
        self.tree.SetItemImage(node, 0, wxTreeItemIcon_Selected)

        self.tree.EditLabel(node)

    def OnCMD_close(self, event, frame=None):
        if frame == None:
            return

        label = frame.title
        #check if the frame is changed
        if frame.is_changed == True:
            dlg_m = wxMessageDialog(self, 'do you want to save the %s?\n'%label,
                'notice', wxYES_NO |wxYES_DEFAULT | wxCANCEL |wxCENTRE |wxICON_EXCLAMATION )
            temp_id = dlg_m.ShowModal()
            if temp_id == wxID_CANCEL:
                dlg_m.Destroy()
                return
            dlg_m.Destroy()
            if temp_id == wxID_YES:
                self.OnCMD_save(event, frame)

        self.OnUtil_clear_frame(label)
        frame.Destroy()
        util.g_observer.publish(util.OB_EVT_WINDOWS_CLOSE)

    def OnCMD_close_all(self, event):
        #close the case frame
        for label in self.case_frame.keys():
            frame = self.case_frame[label]
            #active the closing frame
            frame.Activate()
            self.OnCMD_close(event, frame)

        #close the msg frame
        for label in self.msg_frame.keys():
            frame = self.msg_frame[label]
            #active the closing frame
            frame.Activate()
            self.OnCMD_close(event, frame)

        #close the device frame
        label = self.device_name
        frame = self.device_frame
        if frame != None:
            #active the closing frame
            frame.Activate()
            self.OnCMD_close(event, frame)

    def OnCMD_save(self, event, frame=None):
        if frame == None:
            return

        #check if the frame is changed
        if frame.is_changed == True:
            label = frame.title
            #save case frame
            if self.case_frame.has_key(label):
                script = frame.OnUtil_get_content()
                script_path = self.case_dir + "\\" + label + ".py"
                #check writable
                if os.access(script_path, os.W_OK) != 1:
                    os.chmod(script_path, stat.S_IWRITE)
                #backup case script
                win32file.CopyFile(script_path, script_path + ".bak", False)
                #write case script into the file
                fp = open(script_path, "w")
                fp.write(script)
                fp.close()
            #save msg frame
            elif self.msg_frame.has_key(label):
                msg_lst = frame.OnUtil_get_content()
                cfg_file_path = self.home_dir + "\\msg.ini"
                #backup msg.ini file
                win32file.CopyFile(cfg_file_path, cfg_file_path + ".bak", False)
                #write msg template into the msg.ini
                util.set_msg_tpl(label, msg_lst)
                self.update_msg_tpl()
            #save device frame
            elif self.device_name == label:
                (local_number, local_ip, local_port, local_rtp_ip, local_rtp_port, remote_number, remote_ip, \
                    remote_port, remote_rtp_ip, remote_rtp_port) = frame.OnUtil_get_content()
                cfg_file_path = self.home_dir + "\\device.ini"
                #backup device.ini file
                win32file.CopyFile(cfg_file_path, cfg_file_path + ".bak", False)
                #write device cfg into the device.ini
                util.set_device_info(local_number, local_ip, local_port, local_rtp_ip, local_rtp_port, \
                    remote_number, remote_ip, remote_port, remote_rtp_ip, remote_rtp_port)
                #update device param and restart sip/rtp thread
                self.update_device_param()
            frame.is_changed = False
            frame.SetTitle(label)
            util.g_observer.publish(util.OB_EVT_WINDOWS_SAVED)

    def OnCMD_save_all(self, event):
        #save the case frame
        for label in self.case_frame.keys():
            frame = self.case_frame[label]
            #active the saving frame
            frame.Activate()
            self.OnCMD_save(event, frame)

        #save the msg frame
        for label in self.msg_frame.keys():
            frame = self.msg_frame[label]
            #active the saving frame
            frame.Activate()
            self.OnCMD_save(event, frame)

        #save the device frame
        label = self.device_name
        frame = self.device_frame
        if frame != None:
            #active the saving frame
            frame.Activate()
            self.OnCMD_save(event, frame)

    def OnCMD_backup(self, event):
        #backup all testcase
        curr_time = util.get_curr_time()
        bak_path = self.bak_dir + "\\" + curr_time
        util.copy_dir(self.case_dir, bak_path)

    def OnCMD_clear(self, event):
        self.output_text.Clear()
        self.curr_log_line = 0

    def OnCMD_copy(self, event):
        #get node that already selected
        node = self.tree.GetSelections()[0]

        #get node text
        label = self.tree.GetItemText(node)
        if label == self.case_root_label or label == self.msg_root_label \
            or label == self.device_root_label or label == self.device_name:
            return

        #get parent node
        parent_node = self.tree.GetItemParent(node)
        if parent_node:
            parent_label = self.tree.GetItemText(parent_node)
            #if case or msg tree node is copy
            if parent_label == self.case_root_label or parent_label == self.msg_root_label:
                self.clipboard_node_label = label
                self.clipboard_parent_node_label = parent_label

    def OnCMD_paste(self, event):
        if self.clipboard_node_label == "":
            return

        #if case tree node is paste:
        if self.clipboard_parent_node_label == self.case_root_label:
            #find usable case tree node seq
            case_rule = r"%s([0-9]*)"%self.clipboard_node_label
            case_seq = self.OnUtil_find_usable_seq(self.case_root_node, case_rule)
            if case_seq > 1:
                paste_case_name = self.clipboard_node_label + str(case_seq)
            elif new_case_seq == 1:
                paste_case_name = self.clipboard_node_label
            #create the case node
            node = self.tree.AppendItem(self.case_root_node, paste_case_name)
            self.tree.SetItemImage(node, 0, wxTreeItemIcon_Normal)
            self.tree.SetItemImage(node, 0, wxTreeItemIcon_Selected)
            #copy the case file
            src_script_path = self.case_dir + "\\" + self.clipboard_node_label + ".py"
            dst_script_path = self.case_dir + "\\" + paste_case_name + ".py"
            win32file.CopyFile(src_script_path, dst_script_path, False)
        #if msg tree node is paste:
        elif self.clipboard_parent_node_label == self.msg_root_label:
            #find usable msg tree node seq
            msg_rule = r"%s([0-9]*)"%self.clipboard_node_label
            msg_seq = self.OnUtil_find_usable_seq(self.msg_root_node, msg_rule)
            if msg_seq > 1:
                paste_msg_name = self.clipboard_node_label + str(msg_seq)
            elif new_case_seq == 1:
                paste_msg_name = self.clipboard_node_label
            #create the msg node
            node = self.tree.AppendItem(self.msg_root_node, paste_msg_name)
            self.tree.SetItemImage(node, 0, wxTreeItemIcon_Normal)
            self.tree.SetItemImage(node, 0, wxTreeItemIcon_Selected)
            #backup msg.ini file
            cfg_file_path = self.home_dir + "\\msg.ini"
            win32file.CopyFile(cfg_file_path, cfg_file_path + ".bak", False)
            #copy the msg
            util.add_msg_tpl(paste_msg_name)
            (msg_lst, found) = util.get_msg_tpl(self.clipboard_node_label)
            if found == True:
                util.set_msg_tpl(paste_msg_name, msg_lst)
            self.update_msg_tpl()

    def OnCMD_delete(self, event):
        #get node that already selected
        node = self.tree.GetSelections()[0]

        #get node text
        label = self.tree.GetItemText(node)
        if label == self.case_root_label or label == self.msg_root_label \
            or label == self.device_root_label or label == self.device_name:
            return

        #get parent node
        parent_node = self.tree.GetItemParent(node)
        if parent_node:
            parent_label = self.tree.GetItemText(parent_node)
            #if case tree node is delete
            if parent_label == self.case_root_label:
                self.tree.Delete(node)
                del_script_path = self.case_dir + "\\" + label + ".py"
                if os.access(del_script_path, os.W_OK) != 1:
                    os.chmod(del_script_path, stat.S_IWRITE)
                os.remove(del_script_path)
            #if msg tree node is delete
            elif parent_label == self.msg_root_label:
                self.tree.Delete(node)
                #backup msg.ini file
                cfg_file_path = self.home_dir + "\\msg.ini"
                win32file.CopyFile(cfg_file_path, cfg_file_path + ".bak", False)
                util.del_msg_tpl(label)
                self.update_msg_tpl()

    def OnCMD_rename(self, event):
        #get node that already selected
        node = self.tree.GetSelections()[0]
        self.tree.EditLabel(node)

    def OnCMD_run(self):
        #get node that already selected
        node = self.tree.GetSelections()[0]

        #get node text
        label = self.tree.GetItemText(node)
        if label == self.case_root_label or label == self.msg_root_label or label == self.device_root_label:
            return

        #get parent node
        parent_node = self.tree.GetItemParent(node)
        if parent_node:
            parent_label = self.tree.GetItemText(parent_node)
            #if case tree node is clicked
            if parent_label == self.case_root_label:
                pyfile = self.case_dir + "\\" + label + ".py"
                runner.g_runner.run_script(pyfile)
                return

    def OnUtil_clear_frame(self, label):
        #delete the frame handler
        if self.case_frame.has_key(label):
            del self.case_frame[label]
        elif self.msg_frame.has_key(label):
            del self.msg_frame[label]
        elif self.device_name == label:
            self.device_frame = None

    def OnUtil_find_usable_seq(self, node=None, rule=""):
        if node == None or rule == "":
            util.TRACE("[%s.%s] input param is incorrect!"%(__name__, util.func()))
            return 0

        usable_seq = 1
        seq_lst = []
        cookie = 0

        #get the first child from the tree
        (item, cookie) = self.tree.GetFirstChild(node, cookie)
        while item:
            #if already exist, remember the sequence
            label = self.tree.GetItemText(item)
            m = re.match(rule, label)
            if m != None:
                seq = m.group(1)
                if seq != "":
                    seq_lst.append(eval(seq))
                else:
                    seq_lst.append(1)

            (item, cookie) = self.tree.GetNextChild(node, cookie)

        for seq in range(1, self.max_number):
            if not seq in seq_lst:
                usable_seq = seq
                break

        return usable_seq

    def init_funcs(self):
        #current log lines
        self.curr_log_line = 0
        #the max log lines
        self.max_log_line = 100

        #the max subtree node number
        self.max_number = 100

        #msg template
        self.msg_disc = {}

        #device param
        self.local_number = 0
        self.remote_number = 0
        self.remote_ip = ""
        self.remote_port = 0
        self.local_ip = ""
        self.local_port = 0
        self.local_rtp_port = 0

        #root dir
        self.home_dir = os.getcwd()
        #case dir
        self.case_dir = os.getcwd() + "\\case"
        #rtp dir
        self.rtp_dir = os.getcwd() + "\\rtp"
        #bak dir
        self.bak_dir = os.getcwd() + "\\bak"
        #device name
        self.device_name = "iad"

        #tree root node
        self.root_node = None

        #case tree root node label
        self.case_root_label = "test case"
        #case tree root node
        self.case_root_node = None
        #case frame id disc
        self.case_frame = {}

        #msg tree root node label
        self.msg_root_label = "msg"
        #msg tree root node
        self.msg_root_node = None
        #msg frame id disc
        self.msg_frame = {}

        #device tree root node label
        self.device_root_label = "device"
        #device tree root node
        self.device_root_node = None
        #device frame id
        self.device_frame = None

        #the select node label
        self.select_node_label = ""
        #the begin edit node label
        self.begin_edit_node_label = ""

        #the clipboard node label
        self.clipboard_node_label = ""
        #the clipboard parent node label
        self.clipboard_parent_node_label = ""

        #register observer handler, subscribe event need to observe
        util.g_observer.register(util.OB_MOD_MENU_BAR, self.menu_bar_evt_handler)
        util.g_observer.subscribe(util.OB_MOD_MENU_BAR, util.OB_EVT_INIT_FINISHED)
        util.g_observer.subscribe(util.OB_MOD_MENU_BAR, util.OB_EVT_TREE_SEL_CHANGED)
        util.g_observer.subscribe(util.OB_MOD_MENU_BAR, util.OB_EVT_WINDOWS_CREATE)
        util.g_observer.subscribe(util.OB_MOD_MENU_BAR, util.OB_EVT_WINDOWS_CLOSE)
        util.g_observer.subscribe(util.OB_MOD_MENU_BAR, util.OB_EVT_WINDOWS_CHANGED)
        util.g_observer.subscribe(util.OB_MOD_MENU_BAR, util.OB_EVT_WINDOWS_SAVED)

        util.g_observer.register(util.OB_MOD_TOOL_BAR, self.tool_bar_evt_handler)
        util.g_observer.subscribe(util.OB_MOD_TOOL_BAR, util.OB_EVT_INIT_FINISHED)
        util.g_observer.subscribe(util.OB_MOD_TOOL_BAR, util.OB_EVT_TREE_SEL_CHANGED)
        util.g_observer.subscribe(util.OB_MOD_TOOL_BAR, util.OB_EVT_WINDOWS_CREATE)
        util.g_observer.subscribe(util.OB_MOD_TOOL_BAR, util.OB_EVT_WINDOWS_CLOSE)
        util.g_observer.subscribe(util.OB_MOD_TOOL_BAR, util.OB_EVT_WINDOWS_CHANGED)
        util.g_observer.subscribe(util.OB_MOD_TOOL_BAR, util.OB_EVT_WINDOWS_SAVED)

        util.g_observer.register(util.OB_MOD_TREE, self.tree_evt_handler)
        util.g_observer.subscribe(util.OB_MOD_TREE, util.OB_EVT_INIT_FINISHED)

        #init every module
        self.update_msg_tpl()
        self.update_device_param()
        self.update_dir()
        self.init_tree()
        self.init_case_tree()
        self.init_msg_tree()
        self.init_device_tree()

        util.g_observer.publish(util.OB_EVT_INIT_FINISHED)

        self.Maximize(true)

    def menu_bar_evt_handler(self, event=util.OB_EVT_INVALID, param=None):
        if event == util.OB_EVT_INVALID:
            return

        #the main frame initialize finished
        if event == util.OB_EVT_INIT_FINISHED:
            self.File.Enable(wxID_FRAME_WINDOWFILEITEM_NEW_CASE, True)
            self.File.Enable(wxID_FRAME_WINDOWFILEITEM_NEW_MSG, True)
            self.File.Enable(wxID_FRAME_WINDOWFILEITEM_CLOSE, False)
            self.File.Enable(wxID_FRAME_WINDOWFILEITEM_CLOSE_ALL, False)
            self.File.Enable(wxID_FRAME_WINDOWFILEITEM_SAVE, False)
            self.File.Enable(wxID_FRAME_WINDOWFILEITEM_SAVE_ALL, False)
            self.File.Enable(wxID_FRAME_WINDOWFILEITEM_BACKUP, True)
            self.File.Enable(wxID_FRAME_WINDOWFILEITEM_CLEAR, True)
            self.File.Enable(wxID_FRAME_WINDOWFILEITEM_EXIT, True)

            self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_COPY, False)
            self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_PASTE, False)
            self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_DELETE, False)
            self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_RENAME, False)

            self.Work.Enable(wxID_FRAME_WINDOWWORKITEM_RUN, False)

            self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_NEW_CASE, True)
            self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_NEW_MSG, True)
            self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_COPY, False)
            self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_PASTE, False)
            self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_DELETE, False)
            self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_RUN, False)
            return
        #one tree node have been selected
        elif event == util.OB_EVT_TREE_SEL_CHANGED:
            tree_event = param
            node = tree_event.GetItem()
            label = self.tree.GetItemText(node)
            if label == self.case_root_label or label == self.msg_root_label \
                or label == self.device_root_label or label == "":
                self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_COPY, False)
                self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_PASTE, False)
                self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_DELETE, False)
                self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_RENAME, False)

                self.Work.Enable(wxID_FRAME_WINDOWWORKITEM_RUN, False)

                self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_COPY, False)
                self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_PASTE, False)
                self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_DELETE, False)
                self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_RUN, False)
                return

            parent_node = self.tree.GetItemParent(node)
            if parent_node:
                parent_label = self.tree.GetItemText(parent_node)
                #if case tree node is selected
                if parent_label == self.case_root_label:
                    self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_COPY, True)
                    self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_PASTE, True)
                    self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_DELETE, True)
                    self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_RENAME, True)

                    self.Work.Enable(wxID_FRAME_WINDOWWORKITEM_RUN, True)

                    self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_COPY, True)
                    self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_PASTE, True)
                    self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_DELETE, True)
                    self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_RUN, True)
                    return
                #if msg tree node is selected
                elif parent_label == self.msg_root_label:
                    self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_COPY, True)
                    self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_PASTE, True)
                    self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_DELETE, True)
                    self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_RENAME, True)

                    self.Work.Enable(wxID_FRAME_WINDOWWORKITEM_RUN, False)

                    self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_COPY, True)
                    self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_PASTE, True)
                    self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_DELETE, True)
                    self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_RUN, False)
                    return
                #if device tree node is selected
                elif parent_label == self.device_root_label:
                    self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_COPY, False)
                    self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_PASTE, False)
                    self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_DELETE, False)
                    self.Edit.Enable(wxID_FRAME_WINDOWEDITITEM_RENAME, False)

                    self.Work.Enable(wxID_FRAME_WINDOWWORKITEM_RUN, False)

                    self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_COPY, False)
                    self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_PASTE, False)
                    self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_DELETE, False)
                    self.Tree.Enable(wxID_FRAME_WINDOWTREEITEM_RUN, False)
                    return
        #one sub frame have been created
        elif event == util.OB_EVT_WINDOWS_CREATE:
            self.File.Enable(wxID_FRAME_WINDOWFILEITEM_CLOSE, True)
            self.File.Enable(wxID_FRAME_WINDOWFILEITEM_CLOSE_ALL, True)
            return
        #one sub frame have beed closed
        elif event == util.OB_EVT_WINDOWS_CLOSE:
            found = False
            if len(self.case_frame) > 0:
                found = True
            if len(self.msg_frame) > 0:
                found = True
            if self.device_frame != None:
                found = True

            if found == False:
                self.File.Enable(wxID_FRAME_WINDOWFILEITEM_CLOSE, False)
                self.File.Enable(wxID_FRAME_WINDOWFILEITEM_CLOSE_ALL, False)
            return
        #one sub frame have been changed
        elif event == util.OB_EVT_WINDOWS_CHANGED:
            self.File.Enable(wxID_FRAME_WINDOWFILEITEM_SAVE, True)
            self.File.Enable(wxID_FRAME_WINDOWFILEITEM_SAVE_ALL, True)
            return
        #one sub frame have been saved
        elif event == util.OB_EVT_WINDOWS_SAVED:
            found = False
            for frame in self.case_frame.keys():
                if self.case_frame[frame].is_changed == True:
                    found = True
            for frame in self.msg_frame.keys():
                if self.msg_frame[frame].is_changed == True:
                    found = True
            if self.device_frame != None and self.device_frame.is_changed == True:
                found = True

            if found == False:
                self.File.Enable(wxID_FRAME_WINDOWFILEITEM_SAVE, False)
                self.File.Enable(wxID_FRAME_WINDOWFILEITEM_SAVE_ALL, False)
            return

    def tool_bar_evt_handler(self, event=util.OB_EVT_INVALID, param=None):
        if event == util.OB_EVT_INVALID:
            return

        #the main frame initialize finished
        if event == util.OB_EVT_INIT_FINISHED:
            self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_NEW_CASE, True)
            self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_NEW_MSG, True)
            self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_CLOSE, False)
            self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_CLOSE_ALL, False)
            self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_SAVE, False)
            self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_SAVE_ALL, False)
            self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_BACKUP, True)
            self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_CLEAR, True)
            self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_COPY, False)
            self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_PASTE, False)
            self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_DELETE, False)
            self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_RENAME, False)
            self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_RUN, False)
            return
        #one tree node have been selected
        elif event == util.OB_EVT_TREE_SEL_CHANGED:
            tree_event = param
            node = tree_event.GetItem()
            label = self.tree.GetItemText(node)
            if label == self.case_root_label or label == self.msg_root_label \
                or label == self.device_root_label or label == "":
                self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_COPY, False)
                self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_PASTE, False)
                self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_DELETE, False)
                self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_RENAME, False)
                self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_RUN, False)
                return

            parent_node = self.tree.GetItemParent(node)
            if parent_node:
                parent_label = self.tree.GetItemText(parent_node)
                #if case tree node is selected
                if parent_label == self.case_root_label:
                    self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_COPY, True)
                    self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_PASTE, True)
                    self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_DELETE, True)
                    self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_RENAME, True)
                    self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_RUN, True)
                    return
                #if msg tree node is selected
                elif parent_label == self.msg_root_label:
                    self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_COPY, True)
                    self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_PASTE, True)
                    self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_DELETE, True)
                    self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_RENAME, True)
                    self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_RUN, False)
                    return
                #if device tree node is selected
                elif parent_label == self.device_root_label:
                    self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_COPY, False)
                    self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_PASTE, False)
                    self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_DELETE, False)
                    self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_RENAME, False)
                    self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_RUN, False)
                    return
        #one sub frame have been created
        elif event == util.OB_EVT_WINDOWS_CREATE:
            self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_CLOSE, True)
            self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_CLOSE_ALL, True)
            return
        #one sub frame have beed closed
        elif event == util.OB_EVT_WINDOWS_CLOSE:
            found = False
            if len(self.case_frame) > 0:
                found = True
            if len(self.msg_frame) > 0:
                found = True
            if self.device_frame != None:
                found = True

            if found == False:
                self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_CLOSE, False)
                self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_CLOSE_ALL, False)
            return
        #one sub frame have been changed
        elif event == util.OB_EVT_WINDOWS_CHANGED:
            self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_SAVE, True)
            self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_SAVE_ALL, True)
            return
        #one sub frame have been saved
        elif event == util.OB_EVT_WINDOWS_SAVED:
            found = False
            for frame in self.case_frame.keys():
                if self.case_frame[frame].is_changed == True:
                    found = True
            for frame in self.msg_frame.keys():
                if self.msg_frame[frame].is_changed == True:
                    found = True
            if self.device_frame != None and self.device_frame.is_changed == True:
                found = True

            if found == False:
                self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_SAVE, False)
                self.tool_bar.EnableTool(wxID_FRAME_WINDOWTOOL_BARTOOL_SAVE_ALL, False)
            return

    def tree_evt_handler(self, event=util.OB_EVT_INVALID, param=None):
        if event == util.OB_EVT_INVALID:
            return

        if event == util.OB_EVT_INIT_FINISHED:
            self.tree.Expand(self.case_root_node)
            self.tree.Expand(self.msg_root_node)
            self.tree.Expand(self.device_root_node)
            return

    def update_msg_tpl(self):
        msg_disc = util.get_all_msg_tpl()
        codec.g_codec.set_msg_disc(msg_disc)
        self.msg_disc = msg_disc

    def update_device_param(self):
        (local_number, local_ip, local_port, local_rtp_ip, local_rtp_port, remote_number, \
            remote_ip, remote_port, remote_rtp_ip, remote_rtp_port) = util.get_device_info()

        com.iad.set_local_number(local_number)
        if local_ip != "" and local_port != 0:
            com.iad.restart_sip(local_ip, local_port)
        if local_rtp_ip != "" and local_rtp_port != 0:
            com.iad.restart_rtp(local_rtp_ip, local_rtp_port)
        com.iad.set_remote_number(remote_number)
        com.iad.set_remote_ip(remote_ip)
        com.iad.set_remote_port(remote_port)
        com.iad.set_remote_rtp_ip(remote_rtp_ip)
        com.iad.set_remote_rtp_port(remote_rtp_port)

        self.local_number = local_number
        self.local_ip = local_ip
        self.local_port = local_port
        self.local_rtp_ip = local_rtp_ip
        self.local_rtp_port = local_rtp_port
        self.remote_number = remote_number
        self.remote_ip = remote_ip
        self.remote_port = remote_port
        self.remote_rtp_ip = remote_rtp_ip
        self.remote_rtp_port = remote_rtp_port

    def update_dir(self):
        codec.g_rtp.set_home_dir(self.home_dir)
        codec.g_rtp.set_rtp_dir(self.rtp_dir)

    def init_tree(self):
        self.root_node = self.tree.AddRoot("Root")

    def init_case_tree(self):
        #add case dirtory
        self.case_root_node = self.tree.AppendItem(self.root_node, self.case_root_label)
        self.tree.SetItemImage(self.case_root_node, 13, wxTreeItemIcon_Normal)
        self.tree.SetItemImage(self.case_root_node, 13, wxTreeItemIcon_Selected)
        self.tree.SetItemImage(self.case_root_node, 14, wxTreeItemIcon_Expanded)
        self.tree.SetItemImage(self.case_root_node, 14, wxTreeItemIcon_SelectedExpanded)

        #get file list under case dirtory
        os.chdir(self.case_dir)
        case_list = os.listdir(self.case_dir)
        case_list.sort()

        #strip all file without .py postfix
        case_list2 = []
        for case in case_list:
            if os.path.isfile(case) and case[-3:] == ".py":
                case_list2.append(case[:-3])

        #add case into node tree
        for case in case_list2:
            node = self.tree.AppendItem(self.case_root_node, case)
            self.tree.SetItemImage(node, 0, wxTreeItemIcon_Normal)
            self.tree.SetItemImage(node, 0, wxTreeItemIcon_Selected)

        os.chdir(self.home_dir)

    def init_msg_tree(self):
        #add msg dirtory
        self.msg_root_node = self.tree.AppendItem(self.root_node, self.msg_root_label)
        self.tree.SetItemImage(self.msg_root_node, 13, wxTreeItemIcon_Normal)
        self.tree.SetItemImage(self.msg_root_node, 13, wxTreeItemIcon_Selected)
        self.tree.SetItemImage(self.msg_root_node, 14, wxTreeItemIcon_Expanded)
        self.tree.SetItemImage(self.msg_root_node, 14, wxTreeItemIcon_SelectedExpanded)

        #add msg template into node tree
        if len(self.msg_disc) > 0:
            for key in self.msg_disc.keys():
                node = self.tree.AppendItem(self.msg_root_node, key)
                self.tree.SetItemImage(node, 0, wxTreeItemIcon_Normal)
                self.tree.SetItemImage(node, 0, wxTreeItemIcon_Selected)

    def init_device_tree(self):
        #add device dirtory
        self.device_root_node = self.tree.AppendItem(self.root_node, self.device_root_label)
        self.tree.SetItemImage(self.device_root_node, 13, wxTreeItemIcon_Normal)
        self.tree.SetItemImage(self.device_root_node, 13, wxTreeItemIcon_Selected)
        self.tree.SetItemImage(self.device_root_node, 14, wxTreeItemIcon_Expanded)
        self.tree.SetItemImage(self.device_root_node, 14, wxTreeItemIcon_SelectedExpanded)

        #add device into node tree
        node = self.tree.AppendItem(self.device_root_node, self.device_name)
        self.tree.SetItemImage(node, 0, wxTreeItemIcon_Normal)
        self.tree.SetItemImage(node, 0, wxTreeItemIcon_Selected)


