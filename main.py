from tkinter import *
from random import randint

def main():

    root = Tk()
    root.title('Password Generator')

    def new_rand():
        pwd_entry.delete(0, END)
        pwd_length = int(my_entry.get())

        my_password = ''

        for x in range(pwd_length):
            my_password += chr(randint(33, 126))

        pwd_entry.insert(0, my_password)

    def clipper():
        root.clipboard_clear()
        root.clipboard_append(pwd_entry.get())

    def save():
        my_account_info = my_account_entry.get()
        pwd_entry_info = pwd_entry.get()
        file = open('passdb.txt', 'a')
        file.write(f'''###########################\n
    Email | {my_account_info}
    Password | {pwd_entry_info}\n\n''')
        file.close()

        # interface
    how_many = LabelFrame(root, text='How many Characters')
    how_many.pack(padx=16)
    my_entry = Entry(how_many, font=('Helvetica', 11))
    my_entry.pack(pady=10, padx=10)
    pwd_entry = Entry(root, text='', font=('Helvetica', 11))
    pwd_entry.pack(pady=10)

    my_account = LabelFrame(root, text='Account to save')
    my_account.pack(pady=16)
    my_account_entry = Entry(my_account, font=('Helvetica', 11))
    my_account_entry.pack(pady=10, padx=10)

    in_frame = Frame(root)
    in_frame.pack(pady=10)

        # buttons
    gen_button = Button(in_frame, text='Gen strong Pass', command=new_rand)
    gen_button.grid(row=0, column=0, padx=0)

    clip_button = Button(in_frame, text='Tap to Clipboard', command=clipper)
    clip_button.grid(row=1, column=0, padx=10)

    save_button = Button(in_frame, text='Save password on DB', command=save)
    save_button.grid(row=2, column=0, padx=0)

    root.mainloop()

if __name__ == "__main__":
    main()