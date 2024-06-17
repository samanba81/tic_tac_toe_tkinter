from tkinter.messagebox import showinfo  # create info window
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")  # you can change it to -> ["blue", "green", "dark-blue", "sweetkind"]

turnX = True  # this is default turn


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Create Widgets
        labelState = customtkinter.CTkLabel(self, text="Turn X", width=100)
        button1 = customtkinter.CTkButton(master=self, text="", width=50, height=50,
                                          command=lambda: button_function(button1))
        button2 = customtkinter.CTkButton(master=self, text="", width=50, height=50,
                                          command=lambda: button_function(button2))
        button3 = customtkinter.CTkButton(master=self, text="", width=50, height=50,
                                          command=lambda: button_function(button3))
        button4 = customtkinter.CTkButton(master=self, text="", width=50, height=50,
                                          command=lambda: button_function(button4))
        button5 = customtkinter.CTkButton(master=self, text="", width=50, height=50,
                                          command=lambda: button_function(button5))
        button6 = customtkinter.CTkButton(master=self, text="", width=50, height=50,
                                          command=lambda: button_function(button6))
        button7 = customtkinter.CTkButton(master=self, text="", width=50, height=50,
                                          command=lambda: button_function(button7))
        button8 = customtkinter.CTkButton(master=self, text="", width=50, height=50,
                                          command=lambda: button_function(button8))
        button9 = customtkinter.CTkButton(master=self, text="", width=50, height=50,
                                          command=lambda: button_function(button9))
        buttonStartX = customtkinter.CTkButton(master=self, text="Start With X", width=50, height=50,
                                               command=lambda: empty_bord("X"))
        buttonStartO = customtkinter.CTkButton(master=self, text="Start With O", width=50, height=50,
                                               command=lambda: empty_bord("O"))

        # Location Widgets
        labelState.grid(row=0, column=1, ipady=15)
        button1.grid(row=1, column=0, padx=10, pady=10)
        button2.grid(row=1, column=1, padx=10, pady=10)
        button3.grid(row=1, column=2, padx=10, pady=10)
        button4.grid(row=2, column=0, padx=10, pady=10)
        button5.grid(row=2, column=1, padx=10, pady=10)
        button6.grid(row=2, column=2, padx=10, pady=10)
        button7.grid(row=3, column=0, padx=10, pady=10)
        button8.grid(row=3, column=1, padx=10, pady=10)
        button9.grid(row=3, column=2, padx=10, pady=10)

        buttonStartX.grid(row=4, column=0, padx=100, pady=10, columnspan=3)
        buttonStartO.grid(row=5, column=0, padx=100, pady=10, columnspan=3)

        defaultButtonColor = button1.cget('fg_color')  # get button color for restart

        def button_function(button: customtkinter.CTkButton):
            """ user click button on board """
            global turnX
            if button and button.cget("text") == "":  # check button not used yet
                button.configure(text="X" if turnX else "O")  # change text button to X-O
                have_winner = check_win("X" if turnX else "O")  # check winner using turn
                if not have_winner:  # check we have winner
                    turnX = False if turnX else True  # if we don't have winner yet change turn
                    labelState.configure(text=f'Turn {"X" if turnX else "O"}')  # change label to Turn X-O
                else:
                    message = f"{"X" if turnX else "O"} is Winner"  # have winner create message for user
                    print(message)  # print message to log system
                    showinfo("info", message)  # show message using messagebox window to user
                    labelState.configure(text=message)  # show message to user using label

        def check_win(check: str) -> bool:
            """ check winner - change button colors - use end game """
            # check all case of have winner using check turn
            if button1.cget("text") == button2.cget("text") and button2.cget("text") == button3.cget(
                    "text") and button1.cget("text") == check:
                end_game()
                button1.configure(fg_color='green')
                button2.configure(fg_color='green')
                button3.configure(fg_color='green')
                return True
            if button4.cget("text") == button5.cget("text") and button5.cget("text") == button6.cget(
                    "text") and button4.cget("text") == check:
                end_game()
                button4.configure(fg_color='green')
                button5.configure(fg_color='green')
                button6.configure(fg_color='green')
                return True
            if button7.cget("text") == button8.cget("text") and button8.cget("text") == button9.cget(
                    "text") and button7.cget("text") == check:
                end_game()
                button7.configure(fg_color='green')
                button8.configure(fg_color='green')
                button9.configure(fg_color='green')
                return True
            if button1.cget("text") == button4.cget("text") and button4.cget("text") == button7.cget(
                    "text") and button1.cget("text") == check:
                end_game()
                button1.configure(fg_color='green')
                button4.configure(fg_color='green')
                button7.configure(fg_color='green')
                return True
            if button2.cget("text") == button5.cget("text") and button5.cget("text") == button8.cget(
                    "text") and button2.cget("text") == check:
                end_game()
                button2.configure(fg_color='green')
                button5.configure(fg_color='green')
                button8.configure(fg_color='green')
                return True
            if button1.cget("text") == button5.cget("text") and button5.cget("text") == button9.cget(
                    "text") and button1.cget("text") == check:
                end_game()
                button1.configure(fg_color='green')
                button5.configure(fg_color='green')
                button9.configure(fg_color='green')
                return True
            if button3.cget("text") == button5.cget("text") and button5.cget("text") == button7.cget(
                    "text") and button3.cget("text") == check:
                end_game()
                button3.configure(fg_color='green')
                button5.configure(fg_color='green')
                button7.configure(fg_color='green')
                return True
            return False  # if we don't have winner return false

        def end_game():
            """ change button color and state """
            button1.configure(fg_color='red', state='disabled')
            button2.configure(fg_color='red', state='disabled')
            button3.configure(fg_color='red', state='disabled')
            button4.configure(fg_color='red', state='disabled')
            button5.configure(fg_color='red', state='disabled')
            button6.configure(fg_color='red', state='disabled')
            button7.configure(fg_color='red', state='disabled')
            button8.configure(fg_color='red', state='disabled')
            button9.configure(fg_color='red', state='disabled')

        def empty_bord(starter: str):
            """ restart bord game to default start """
            print(f"start with {starter}")
            global turnX
            button1.configure(fg_color=defaultButtonColor, text="", state='normal')
            button2.configure(fg_color=defaultButtonColor, text="", state='normal')
            button3.configure(fg_color=defaultButtonColor, text="", state='normal')
            button4.configure(fg_color=defaultButtonColor, text="", state='normal')
            button5.configure(fg_color=defaultButtonColor, text="", state='normal')
            button6.configure(fg_color=defaultButtonColor, text="", state='normal')
            button7.configure(fg_color=defaultButtonColor, text="", state='normal')
            button8.configure(fg_color=defaultButtonColor, text="", state='normal')
            button9.configure(fg_color=defaultButtonColor, text="", state='normal')
            labelState.configure(text=f'Turn {starter}')
            turnX = starter == "X"


if __name__ == "__main__":
    app = App()
    app.geometry("300x400")
    app.mainloop()
