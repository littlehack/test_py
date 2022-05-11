import win32gui
import win32api
import win32con
import time
import win32clipboard as w

def FindRoom(chatroom):
    win = win32gui.FindWindow(None, chatroom)
    try:
        if win != 0:
            win32gui.ShowWindow(win, win32con.SW_SHOWMINIMIZED)
            win32gui.ShowWindow(win, win32con.SW_SHOWNORMAL)
            win32gui.ShowWindow(win, win32con.SW_SHOW)
            # 第二个参数是置顶，前两个数字是位置，后两个数字是大小，最后一个是显示，200,100值指在屏幕窗口位置，500,600指chatrom窗口大小
            win32gui.SetWindowPos(win, win32con.HWND_TOPMOST, 200, 100, 500, 600, win32con.SWP_SHOWWINDOW)
            # 获取控制
            win32gui.SetForegroundWindow(win)
            time.sleep(0.5)
        else:
            print('找不到该窗口，请双击联系人%s，保证其是一个单独的窗口' % (chatroom))
        # exit()
    except Exception as e:
        print(e)
        exit()
    return  win

# def setText(aString):
#     w.OpenClipboard()
#     w.EmptyClipboard()
#     w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
#     w.CloseClipboard()
# def zhanTie():
#     win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
#     win32api.keybd_event(86, 0, 0, 0)  # v键位码是86
#     win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
#     win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
def huiche():
    win32api.keybd_event(18, 0, 0, 0)  # Alt键位码
    win32api.keybd_event(83, 0, 0, 0)  # s键位码
    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
# def sendText(chatrooms,text):
#     for chatroom in chatrooms:
#         FindWindow(chatroom)
#         setText(" "+text)
#         zhanTie()
#         huiche()
# #
#方法2，直接发消息，不需要复制粘贴
if __name__ == "__main__":
    try:
        handle = FindRoom('文件传输助手')
        win32gui.SetForegroundWindow(handle)
        # 发送的信息必须要转换成ASCII
        data = "No"
        st=[ord(s) for s in data]
        for x in st:
            win32gui.PostMessage(handle,win32con.WM_CHAR,x,0)
            huiche()
        print('{%s-%s}已经发送' %(data,str(time.strftime("%D/%X"))))
    except:
        pass

# FindWindow("王宝儿")