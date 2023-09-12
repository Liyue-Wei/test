import tkinter as tk

win = tk.Tk()
win.geometry("600x700")
win.title("Offline Email Sender")
win.resizable(0, 0)

def settings():
    win_2 = tk.Tk()
    win_2.geometry("380x260")
    win_2.title("smtp/tcp settings")

    def finish():
        global smtp_set, tcp_set, pass_set
        smtp_set = smtp.get()
        tcp_set = tcp.get()
        pass_set = password.get()
        # print("{}, {}, {}".format(smtp, tcp, password))
        print("{}, {}, {}".format(smtp_set, tcp_set, pass_set))
        win_2.destroy()

    class GUI_interface():
        global smtp, tcp, password
        smtp = tk.StringVar()
        tcp = tk.StringVar()
        password = tk.StringVar()

        tk.Label(win_2, text="SMTP", font=("微軟正黑體", 16)).place(x=10, y=10)
        tk.Entry(win_2, font=("微軟正黑體", 14), width=32, textvariable=smtp).place(x=10, y=40)
        tk.Label(win_2, text="TCP", font=("微軟正黑體", 16)).place(x=10, y=70)
        tk.Entry(win_2, font=("微軟正黑體", 14), width=32, textvariable=tcp).place(x=10, y=100)
        tk.Label(win_2, text="Password", font=("微軟正黑體", 16)).place(x=10, y=130)
        tk.Entry(win_2, font=("微軟正黑體", 14), width=32, show="*", textvariable=password).place(x=10, y=160)
        tk.Button(win_2, text="finish", font=("微軟正黑體", 14), command=finish).place(x=300, y=200)

    win_2.mainloop()

# def finish():
#     global smtp_set, tcp_set, pass_set
#     smtp_set = smtp.get()
#     tcp_set = tcp.get()
#     pass_set = password.get()
#     # print("{}, {}, {}".format(smtp, tcp, password))
#     print("{}, {}, {}".format(smtp_set, tcp_set, pass_set))
#     win.destroy()

class GUI_interface():
    # global smtp, tcp, password
    # smtp = tk.StringVar()
    # tcp = tk.StringVar()
    # password = tk.StringVar()

    # class GUI_interface():
    #     tk.Label(win, text="SMTP", font=("微軟正黑體", 16)).place(x=10, y=10)
    #     tk.Entry(win, font=("微軟正黑體", 14), width=32, textvariable=smtp).place(x=10, y=40)
    #     tk.Label(win, text="TCP", font=("微軟正黑體", 16)).place(x=10, y=70)
    #     tk.Entry(win, font=("微軟正黑體", 14), width=32, textvariable=tcp).place(x=10, y=100)
    #     tk.Label(win, text="Password", font=("微軟正黑體", 16)).place(x=10, y=130)
    #     tk.Entry(win, font=("微軟正黑體", 14), width=32, show="*", textvariable=password).place(x=10, y=160)
    #     tk.Button(win, text="finish", font=("微軟正黑體", 14), command=finish).place(x=300, y=200)
    tk.Button(win, text="smtp/tcp settings", font=("微軟正黑體", 14), command=settings).place(x=5, y=650)

win.mainloop()