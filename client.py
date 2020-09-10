import sys,time,subprocess
from PyQt5.QtWidgets import (QWidget, QApplication,
                             QPushButton, QLabel, QLineEdit, QGridLayout, QRadioButton, QHBoxLayout, QVBoxLayout,
                             QProgressBar)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QBasicTimer
from subprocess import Popen, PIPE


class MainWin(QWidget):
    def __init__(self):
        super().__init__()

        self.TextBox()

    def TextBox(self):
        # 建立服务器地址输入框
        label = QLabel('服务器地址：')
        address = QLineEdit()

        # 建立连接按钮
        self.btn1 = QPushButton('连接', self)

        def on_btn1_clicked():
            app_dir = "C:\Windows\System32\\vpncmd.exe"
            import os
            p1 = Popen([app_dir], stdout=PIPE, stdin=PIPE, stderr=PIPE)
            #os.startfile(app_dir)
            # 执行命令列表
            cmds = [
                "2",
                "",
                "AccountConnect",
                "新的 VPN 连接"
                "AccountStatusGet"
                "新的 VPN 连接"
            ]

            for m in cmds:
                ## 当将输入发送到行解释器时，不要忘记发送实际的换行符
                p1.stdin.write((m + "\n").encode())
                ## 将数据放入流后，始终刷新流，因为它可能会被缓冲
                p1.stdin.flush()
                # stdout, stderr = p1.communicate()
            while p1.poll() == None:
                # 按行获取日志
                stdout, stderror = p1.communicate()
                print(stdout.decode("utf-8"))
                p1.stdin.write(bytes("dirn", "utf-8"))
                # out = p1.stdout.readline().strip()
                # if out:
                # print(out.decode())
            print(p1.returncode)
            #else:
            #print("fail")
            """
            # 自动跑输入命令
            import pyautogui
            pyautogui.typewrite(["enter"], '0.25')

            # 暂停5秒，定位应用界面
            
            import time
            time.sleep(5)
            # 获取应用坐标，通过鼠标位置获取
            # 获取鼠标位置
            x, y = pyautogui.position()
            # 输入命令
            for i in cmds:
                
                # 解决CMD中中文不可用情况，使用右键复制
                
                # 放置到剪贴板
                import pyperclip
                pyperclip.copy(i)
                # 右键粘贴命令
                pyautogui.click(x=x, y=y, button='right')
                time.sleep(0.5)
                # pyautogui.typewrite([x for x in i], '0.25')
                pyautogui.typewrite(["enter"], '0.25')
            """

        self.btn1.clicked.connect(on_btn1_clicked)

        # 建立断开按钮
        btn2 = QPushButton('断开', self)

        def on_btn2_clicked():
            app_dir = "C:\Windows\System32\\vpncmd.exe"
            import os
            os.startfile(app_dir)
            # 执行命令列表
            cmds = [
                "2",
                "",
                "AccountDisconnect",
                "新的 VPN 连接"
            ]
            # 自动跑输入命令
            import pyautogui
            pyautogui.typewrite(["enter"], '0.25')

            # 暂停5秒，定位应用界面
            import time
            time.sleep(5)
            # 获取应用坐标，通过鼠标位置获取
            # 获取鼠标位置
            x, y = pyautogui.position()
            # 输入命令
            for i in cmds:
                """
                 解决CMD中中文不可用情况，使用右键复制
                """
                # 放置到剪贴板
                import pyperclip
                pyperclip.copy(i)
                # 右键粘贴命令
                pyautogui.click(x=x, y=y, button='right')
                time.sleep(0.5)
                # pyautogui.typewrite([x for x in i], '0.25')
                pyautogui.typewrite(["enter"], '0.25')

        btn2.clicked.connect(on_btn2_clicked)

        # 按钮布局（表单布局）
        grid = QGridLayout()
        grid.setSpacing(30)
        grid.addWidget(label, 1, 0)
        grid.addWidget(address, 1, 1)
        grid.addWidget(self.btn1, 2, 0)
        grid.addWidget(btn2, 2, 2)
        # grid.addWidget(self.pbar, 3, 0)
        self.setLayout(grid)
        #self.show()

        self.initUI()  # 显示窗体内容

       #进度条
    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(160, 160, 200, 25)  # 设置进度条位置及大小
        #self.btn1 = QPushButton('连接', self)
        #self.btn1.move(50, 90)
        self.btn1.clicked.connect(self.doAction)  # 点击按钮时执行的动作函数指定为self.doAction()
        # self.btn.setGeometry(50, 90, 40, 25)

        self.timer = QBasicTimer()  # 构建一个计数器
        self.step = 0  # 设置基数
        self.setGeometry(900, 300, 500, 300)  # 设置整个窗体的大小
        self.setWindowTitle('Softer Ether VPN Client')  # 设置窗口标题
        self.setWindowIcon(QIcon("VPN.ico")) #设置窗口图标
        self.show()
        #self.timerEvent()

    def timerEvent(self, *args, **kwargs):
        if self.step >= 100:
            self.timer.stop()
            #self.btn.setText('完成')
            return
        self.step += 1
        self.pbar.setValue(self.step)  # timer每次重围时将self.step 赋值给pbar
        #self.doAction()

    def doAction(self):
        #if self.timer.isActive():
            #self.timer.stop()
            #self.btn.setText('开始')
        #else:
            self.timer.start(100, self)
            #self.btn1.setText('停止')





if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 所有的PyQt5应用必须创建一个应用（Application）对象。
    # sys.argv参数是一个来自命令行的参数列表。
    ex = MainWin()
    # 建立循环

    sys.exit(app.exec_())
    # 应用进入主循环。在这个地方，事处理件开始执行。主循环用于接收来自窗口触发的事件
