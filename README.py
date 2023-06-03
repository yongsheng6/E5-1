# E5-1
# 导入模块
import time
import tkinter as tk
import winsound

# 定义Timer类，用于设置和更新专注时钟的状态和时间
class Timer:
    def __init__(self):
        # 初始化状态和时间
        self.state = "focus" # 状态有focus, break, long_break三种
        self.focus_time = 25 * 60 # 专注时间为25分钟
        self.break_time = 5 * 60 # 休息时间为5分钟
        self.long_break_time = 15 * 60 # 长休息时间为15分钟
        self.cycle = 0 # 记录完成的专注周期数
        self.time_left = self.focus_time # 剩余时间，默认为专注时间

    def update(self):
        # 更新剩余时间和状态
        if self.time_left > 0:
            # 如果剩余时间大于0，减少1秒
            self.time_left -= 1
        else:
            # 如果剩余时间等于0，切换状态并播放提示音
            winsound.Beep(440, 1000) # 播放频率为440Hz，持续时间为1秒的声音
            if self.state == "focus":
                # 如果当前状态是专注，增加完成的周期数，并根据周期数切换到休息或长休息状态
                self.cycle += 1
                if self.cycle % 4 == 0:
                    # 如果完成了4个周期，切换到长休息状态，并重置剩余时间为长休息时间
                    self.state = "long_break"
                    self.time_left = self.long_break_time
                else:
                    # 如果没有完成4个周期，切换到休息状态，并重置剩余时间为休息时间
                    self.state = "break"
                    self.time_left = self.break_time
            else:
                # 如果当前状态是休息或长休息，切换到专注状态，并重置剩余时间为专注时间
                self.state = "focus"
                self.time_left = self.focus_time

    def reset(self):
        # 重置状态和时间
        self.state = "focus"
        self.time_left = self.focus_time

# 定义Clock类，用于创建和控制时钟的界面和逻辑
class Clock:
    def __init__(self):
        # 创建一个Timer对象
        self.timer = Timer()
        # 创建一个tkinter对象
        self.root = tk.Tk()
        # 设置窗口标题和大小
        self.root.title("Focus Clock")
        self.root.geometry("300x200")
        # 创建一个标签，用于显示剩余时间
        self.label = tk.Label(self.root, text=self.format_time(self.timer.time_left), font=("Arial", 32))
        # 将标签放置在窗口中央
        self.label.pack(expand=True)
        # 创建一个按钮，用于重置时钟
        self.button = tk.Button(self.root, text="Reset", command=self.reset)
        # 将按钮放置在窗口底部
        self.button.pack(side=tk.BOTTOM)
        # 创建一个定时器事件，每隔1秒调用一次tick函数
        self.root.after(1000, self.tick)

    def tick(self):
        # 更新时钟的状态和时间
        self.timer.update()
        # 更新标签的文本，显示剩余时间和状态
        self.label.config(text=self.format_time(self.timer.time_left) + "\n" + self.timer.state.capitalize())
        # 重新创建一个定时器事件，每隔1秒调用一次tick函数
        self.root.after(1000, self.tick)

    def reset(self):
        # 重置时钟的状态和时间
        self.timer.reset()
        # 更新标签的文本，显示剩余时间和状态
        self.label.config(text=self.format_time(self.timer.time_left) + "\n" + self.timer.state.capitalize())

    def format_time(self, seconds):
        # 格式化时间，将秒数转换为分:秒的形式
        minutes = seconds // 60
        seconds = seconds % 60
        return "{:02d}:{:02d}".format(minutes, seconds)

    def start(self):
        # 启动主循环
        self.root.mainloop()

# 在主函数中创建一个Clock对象，并启动主循环
def main():
    clock = Clock()
    clock.start()

# 如果是直接运行本文件，调用主函数
if __name__ == "__main__":
    main()
