from tkinter import *
import random

class BillApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.title("Billing Software")

        # ====== Variables ======
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        self.c_bill_no = StringVar(value=str(random.randint(1000, 9999)))
        self.total_bill = StringVar()

        # Items and Prices
        items = [
            ("Gobi_Manchurian", 189), ("Chilli_Chicken", 240), ("Chicken_Lollipop", 240),
            ("Paneer_Tikkas", 200), ("Chicken_Curry_Rice", 300), ("Mutton_Curry_Rice", 350),
            ("Prawn_Curry_Rice", 300), ("Egg_Curry_Rice", 400), ("Butter_Naan", 45),
            ("Butter_Roti", 35), ("Cheese_Garlic_Naan", 80), ("Keema_Naan", 50),
            ("Channa_Masala", 160), ("Kadhai_Paneer", 240), ("Mutton_Chicken", 280),
            ("Mutton_Biryani", 320), ("Chicken_Biryani", 270), ("EggVeg_Biryani", 200),
            ("JeeraSteamed_Rice", 150), ("Water_Bottle", 20), ("SaltSweet_Lassi", 40),
            ("Juices", 80), ("Lemon_SodaWater", 45)
        ]
        self.prices = dict(items)
        self.vars = {name: IntVar() for name, _ in items}

        # ====== Color Theme ======
        bg_color = "#4E342E"       # Brown background
        entry_bg = "#D7CCC8"       # Light beige input
        label_fg = "#FFEB3B"       # Bright yellow for labels
        text_fg = "#FFFFFF"
        btn_color = "#6D4C41"      # Deep brown for buttons

        # ====== Title ======
        Label(self.root, text="RESTAURANT BILLING SYSTEM", bd=12, relief=GROOVE,
              fg="white", bg=bg_color, font=("Helvetica", 30, "bold"), pady=3).pack(fill=X)

        # ====== Customer Details ======
        F1 = LabelFrame(self.root, text="Customer Details", font=("Helvetica", 13, "bold"),
                        fg=label_fg, bg=bg_color, relief=GROOVE, bd=10)
        F1.place(x=0, y=80, relwidth=1)

        Label(F1, text="Customer Name", bg=bg_color, fg=text_fg, font=("Helvetica", 15)).grid(row=0, column=0, padx=10, pady=5)
        Entry(F1, bd=6, bg=entry_bg, textvariable=self.cus_name).grid(row=0, column=1, ipady=4, ipadx=30)

        Label(F1, text="Phone No", bg=bg_color, fg=text_fg, font=("Helvetica", 15)).grid(row=0, column=2, padx=20)
        Entry(F1, bd=6, bg=entry_bg, textvariable=self.c_phone).grid(row=0, column=3, ipady=4, ipadx=30)

        Label(F1, text="Bill No.", bg=bg_color, fg=text_fg, font=("Helvetica", 15)).grid(row=0, column=4, padx=20)
        Entry(F1, bd=6, bg=entry_bg, textvariable=self.c_bill_no).grid(row=0, column=5, ipadx=30, ipady=4)

        # ====== Item Frames ======
        def create_frame(x, y, title, items):
            F = LabelFrame(self.root, text=title, bd=10, relief=GROOVE,
                           bg=bg_color, fg=label_fg, font=("Helvetica", 13, "bold"))
            F.place(x=x, y=y, width=325, height=220)
            for idx, name in enumerate(items):
                Label(F, text=name.replace('_', ' '), font=("Helvetica", 12), fg=text_fg, bg=bg_color).grid(row=idx, column=0, padx=5, pady=10)
                Entry(F, bd=5, bg=entry_bg, textvariable=self.vars[name]).grid(row=idx, column=1, ipady=2, ipadx=1)

        create_frame(5, 180, "Starters", ["Gobi_Manchurian", "Chilli_Chicken", "Chicken_Lollipop", "Paneer_Tikkas"])
        create_frame(5, 400, "Specials", ["Chicken_Curry_Rice", "Mutton_Curry_Rice", "Prawn_Curry_Rice", "Egg_Curry_Rice"])
        create_frame(330, 180, "Breads", ["Butter_Naan", "Butter_Roti", "Cheese_Garlic_Naan", "Keema_Naan"])
        create_frame(330, 400, "Curries", ["Channa_Masala", "Kadhai_Paneer", "Mutton_Chicken", "Mutton_Biryani"])
        create_frame(655, 400, "Beverages", ["Water_Bottle", "SaltSweet_Lassi", "Juices", "Lemon_SodaWater"])

        # ====== Bill Area ======
        F3 = Frame(self.root, bd=10, relief=GROOVE, bg=bg_color)
        F3.place(x=960, y=180, width=325, height=450)
        Label(F3, text="Bill Area", font=("Helvetica", 14, "bold"), bg=bg_color, fg=label_fg, bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        self.txt = Text(F3, yscrollcommand=scroll_y.set, bg="#3E2723", fg="white", font=("Courier", 10), insertbackground="white")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        # ====== Bill Menu ======
        F4 = LabelFrame(self.root, text="Bill Menu", bd=10, relief=GROOVE,
                        bg=bg_color, fg=label_fg, font=("Helvetica", 13, "bold"))
        F4.place(x=0, y=600, relwidth=1, height=145)

        Label(F4, text="Total", font=("Helvetica", 15), fg=text_fg, bg=bg_color).grid(row=0, column=0, padx=10)
        Entry(F4, bd=6, bg=entry_bg, textvariable=self.total_bill).grid(row=0, column=1, ipady=2, ipadx=5)

        Button(F4, text="Generate Bill", bg=btn_color, fg="white", font=("Helvetica", 12, "bold"), bd=7,
               command=self.bill_area).grid(row=0, column=2, padx=30, ipadx=20)
        Button(F4, text="Clear", bg=btn_color, fg="white", font=("Helvetica", 12, "bold"), bd=7,
               command=self.clear).grid(row=0, column=3, padx=30, ipadx=20)
        Button(F4, text="Exit", bg="red", fg="white", font=("Helvetica", 12, "bold"), bd=7,
               command=self.exit_app).grid(row=0, column=4, padx=30, ipadx=20)

        self.welcome_soft()

    # ====== Function Definitions ======
    def total(self):
        sm = sum(var.get() * self.prices[name] for name, var in self.vars.items())
        self.total_bill.set(f"Rs. {sm}")
        return sm

    def welcome_soft(self):
        self.txt.delete('1.0', END)
        self.txt.insert(END, " WELCOME TO THE RESTAURANT\n")
        self.txt.insert(END, f"\nBill No. : {self.c_bill_no.get()}")
        self.txt.insert(END, f"\nCustomer Name : {self.cus_name.get()}")
        self.txt.insert(END, f"\nPhone No. : {self.c_phone.get()}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END, "\nProduct           Qty     Price")
        self.txt.insert(END, "\n===================================\n")

    def clear(self):
        for var in self.vars.values():
            var.set(0)
        self.total_bill.set('')
        self.welcome_soft()

    def bill_area(self):
        self.welcome_soft()
        for name, var in self.vars.items():
            qty = var.get()
            if qty > 0:
                price = self.prices[name]
                self.txt.insert(END, f"\n{name.replace('_',' '):18}{qty:<8}{qty * price:>5}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END, f"\nGrand Total : Rs. {self.total()}")
        self.txt.insert(END, "\n===================================")

    def exit_app(self):
        self.root.destroy()

# ====== Launch App ======
if __name__ == "__main__":
    root = Tk()
    app = BillApp(root)
    root.mainloop()
