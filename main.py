import EncFund as Enc
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    '''
    this class creates window that has is a form to input information.
    the information can be viewed in table with "info" button on the main window.
    '''
    components = {}
    people = []
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry('600x400')
        self.ComponentLayout()
        self.attributes('-topmost', True)
        self.columnconfigure(4)
        self.rowconfigure(7)

    def ComponentLayout(self):
        option = {'padx': 5, 'pady': 5}
        self.emptyRow = ttk.Label(self, text='  \n  ')
        self.emptyRow.grid(row=0, column=0)

        self.infoButton = ttk.Button(self, text='Info')
        self.infoButton.grid(row=0, column = 2)
        self.infoButton.configure(command=self.showInfo)
        #component fram
        self.frame = ttk.LabelFrame(self, text=' info', borderwidth=1)
        self.frame.grid(row=1, column=2,  columnspan=1, sticky="E", **option)
        #name
        self.nameLabel = ttk.Label(self.frame, text="Full Name")
        self.nameLabel.grid(row=1, column=2, sticky="W", **option)

        self.nameEntry = ttk.Entry(self.frame, width=50)
        self.nameEntry.grid(row=1, column=3, sticky="W", **option)
        self.nameEntry.focus()

        #email
        self.emailLabel = ttk.Label(self.frame, text="Email")
        self.emailLabel.grid(row=2, column=2, sticky="W", **option)

        self.emailEntry = ttk.Entry(self.frame, width=50)
        self.emailEntry.grid(row=2, column=3, sticky="W", **option)

        #Phone Number
        self.phoneLabel = ttk.Label(self.frame, text="Phone Number")
        self.phoneLabel.grid(row=3, column=2, sticky="W", **option)

        self.phoneEntry = ttk.Entry(self.frame, width=50)
        self.phoneEntry.grid(row=3, column=3, sticky="W", **option)

        #donation
        self.dntLabel = ttk.Label(self.frame, text="Donation")
        self.dntLabel.grid(row=4, column=2, sticky="W", **option)

        self.dntEntry = ttk.Entry(self.frame, width=50)
        self.dntEntry.grid(row=4, column=3, sticky="W", **option)

        #Add button
        self.addButton = ttk.Button(self, text="Add")
        self.addButton.grid(row=2, column=3, sticky="W", **option)
        self.addButton.configure(command=self.button_clicked)

        #add component entry to dictionary
        self.components["fullName"] = self.nameEntry
        self.components['email'] = self.emailEntry
        self.components['phoneNumber'] = self.phoneEntry
        self.components['donation'] = self.dntEntry
    def button_clicked(self):
        #get info
        info = {}
        info["fullName"] = self.components["fullName"].get()
        info['email'] = self.components['email'].get()
        info['phoneNumber'] = self.components['phoneNumber'].get()
        info['donation'] = self.components['donation'].get()

        Enc.WriteToCSV(info["fullName"], info['email'], info['phoneNumber'], info['donation'])

        #clear the field after getting info
        self.components["fullName"].delete(0, tk.END)
        self.components["email"].delete(0, tk.END)
        self.components["phoneNumber"].delete(0, tk.END)
        self.components["donation"].delete(0, tk.END)

        self.people.append(info)
        #showinfo(self, message="Name: %s  \nEmail: %s \nPhone number: %s"%(info["fullName"], info['email'], info['phoneNumber']) )
        showinfo(self,message="information added")
    def showInfo(self):
        if "infoWindow" in dir(self):
            try:
                if self.infoWindow.state() == "normal": self.infoWindow.focus()
            except Exception as e:
                if "infoWindow" in self.__dict__:
                    print("yes")
                    del self.__dict__["infoWindow"]
                    print(hasattr(self,"infoWindow"))
                self.infoWindow = tk.Toplevel(self)
                self.infoWindow.title("Information window")
                self.infoWindow.geometry("550x350")
                self.infoWindow.focus()
                self.infoWindow.wm_transient(self)
                self.createTable()
        else:
            self.infoWindow = tk.Toplevel(self)
            self.infoWindow.title("Information window")
            self.infoWindow.geometry("550x350")
            self.infoWindow.focus()
            self.infoWindow.wm_transient(self)
            self.createTable()

    def createTable(self):
        tb = ttk.Treeview(self.infoWindow, columns=("c1", "c2", "c3"), show='headings', height=15)
        tb.pack()

        tb['columns'] = ('name', 'email', 'phone')
        tb.column('#0',width=0)
        tb.column('name', anchor=tk.CENTER,width=180, stretch=tk.NO )
        tb.column('email', anchor=tk.CENTER,width=180 , stretch=tk.NO )
        tb.column('phone',anchor=tk.CENTER,width=180, stretch=tk.NO )

        tb.heading('#0', text="",anchor=tk.CENTER)
        tb.heading('name', text="Full Name",anchor=tk.CENTER)
        tb.heading('email', text="Email",anchor=tk.CENTER)
        tb.heading('phone', text="Phone Number",anchor=tk.CENTER)
        for p in self.people:
            tb.insert(parent='', index='end', values=(p["fullName"], p["email"], p["phoneNumber"]))


if __name__ == "__main__":
    app = App()
    app.mainloop()