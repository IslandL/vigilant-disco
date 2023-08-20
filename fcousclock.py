import time

def focus_timer(minutes):
    # 将分钟转换为秒
    seconds = minutes * 60
    # 循环计时，直到秒数为零
    while seconds:
        # 将秒数分解为分钟和秒
        mins, secs = divmod(seconds, 60)
        # 格式化时间显示
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # 在同一行打印时间
        print(timer, end="\r")
        # 暂停一秒
        time.sleep(1)
        # 减少一秒
        seconds -= 1
    # 打印提示信息
    print("Time's up!")

if __name__ == "__main__":
    # 获取用户输入的分钟数
    minutes = int(input("Enter the number of minutes to focus: "))
    # 调用专注时钟函数
    focus_timer(minutes)
