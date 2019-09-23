import tkinter
import tkinter.messagebox
import datetime as d
import winsound


#функция установки времени (обновление каждые 6000 мс)
def time():
    global f
    if f == 0:
        now = d.datetime.now()
        hh = now.hour
        mm = now.minute
        counter1.set(convert(hh))
        counter2.set(convert(mm))
        window.after(6000, time)


#конвертируем дату в нужный формат
def convert(val):
    if val < 9:
        return "0" + str(val)
    else:
        return str(val)


#кнопка А
def start():
    global f

    if f == 0:
        time()

    else:
        now = d.datetime.now()
        h = int(counter1.get())
        m = int(counter2.get())

        if h == now.hour and m == now.minute:
            f = 0
            time()

        elif h <= now.hour and m <= now.minute:
            tkinter.messagebox.showinfo('Warning', 'This time is not available today')
            f = 0
            time()

        else:
            current_time = now.hour * 60 + now.minute
            alarm_time = h * 60 + m
            tkinter.messagebox.showinfo('Alarm clock', 'The time was successfully set')
            window.after((alarm_time - current_time) * 60000,  wind)

        f = 0
#кнопка H
def click1():
    global f
    f = 1
    n = int(counter1.get())
    if n < 23:
        if n < 9:
            counter1.set("0" + str(n+1))
        else:
            counter1.set(str(n + 1))
    else:
        counter1.set("00")


#кнопка M
def click2():
    global f
    f = 1
    m = int(counter2.get())
    if m < 59:
        if m < 9:
            counter2.set("0" + str(m + 1))
        else:
            counter2.set(str(m + 1))
    else:
        counter2.set("00")
        counter1.set(str(int(counter1.get()) + 1))


#звук будильника
def wind():
    winsound.Beep(1000, 5000)
    global f
    f = 0
    time()


#интерфейс программы
if __name__ == '__main__':
    window = tkinter.Tk()
    window.geometry('240x110')
    window.title('Alarm clock')
    window.configure(bg="#FFE4E1")

    top_frame = tkinter.Frame()
    bottom_frame = tkinter.Frame()

    top_frame.pack()
    bottom_frame.pack()

    counter1 = tkinter.StringVar()
    counter1.set("00")
    counter2 = tkinter.StringVar()
    counter2.set("00")
    f = 0

    button1 = tkinter.Button(bottom_frame, text='H',  width=5, bg="#F08080", command=click1)
    button1.pack(side="left")

    label1 = tkinter.Label(top_frame, font='Times 40', fg='#DB7093',   textvariable=counter1)
    label1.pack(side="left")

    button2 = tkinter.Button(bottom_frame, text='M', width=5, bg="#F08080", command=click2)
    button2.pack(side="left")

    label2 = tkinter.Label(top_frame, text=':', font='Times 40', fg='#DB7093')
    label2.pack(side="left")

    label3 = tkinter.Label(top_frame, font='Times 40', fg='#DB7093', textvariable=counter2)
    label3.pack(side="left")

    button3 = tkinter.Button(bottom_frame, text='A', width=5, bg="#F08080", command=start)
    button3.pack(side="right")

    window.mainloop()
