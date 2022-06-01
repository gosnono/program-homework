import tkinter as tk

def main():
    window = tk.Tk()
    label = tk.Label(text= "Name")
    entry = tk.Entry()
    btn = tk.Button(text="입력", command=lambda: print(entry.get()))
    label.pack()
    entry.pack()
    btn.pack()

    window.mainloop()

if __name__ == "__main__":
    main()

    