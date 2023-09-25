import tkinter as tk

def main():
    # Create the main application window
    root = tk.Tk()

    # Button labels
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', 'C', '=', '+'
    ]

    # Create and place buttons in a grid
    row_val = 1
    col_val = 0

    # Create buttons and arrange them in a grid
    for button in buttons:
        if button == '=':
            button_color = 'black'
        else:
            button_color = 'black'
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 16), bg=button_color, fg='white').grid(row=row_val, column=col_val)
        col_val += 1 #increments col value by one
        if col_val > 3: 
            col_val = 0
            row_val += 1

    # Create a text widget for displaying input and results
    screen = tk.Text(root, height=2, width=20, font=("Arial", 20))
    screen.grid(row=0, column=0, columnspan=4)
    screen.config(bg='orange', fg='black')  # Set the background and foreground color for the label

    def clickbutton(event):
        text = event.widget.cget("text") #event.widget references the widget that triggered the event. .cget("text") used to get the "text" property of the widget. the whole line retrieves the text displayed on the widget that was clicked and assigns it to the variable
        if text == "=":
            try:
                # Get the expression from the Text widget
                expression = screen.get("1.0", tk.END).strip() #.get("1.0", tk.END) method is used to retrieve the content of the Text widget. The arguments "1.0" and tk.END specify the range of text to retrieve. "1.0" means the first character of the first line, and tk.END means the end of the text in the widget. So, this retrieves all the text in the Text widget. .strip()  is used to remove leading and trailing whitespace 
                if expression:
                    result = str(eval(expression)) #takes a mathematical expression as a string, evaluates it to get the numeric result, and converts that result into a string
                    screen.delete(1.0, tk.END) #deletes all the text content within the Text widget
                    screen.insert(tk.END, result) #inserts text content into a tkinter Text widget named screen. .insert(index, text): This method is called on the Text widget screen to insert text content at a specified index. screen.insert(tk.END, result) inserts the text stored in the result variable at the end of the Text widget's content
                else:
                    screen.delete(1.0, tk.END)
            except Exception as e:
                # Handle errors by displaying "Error" in the Text widget
                screen.delete(1.0, tk.END)
                screen.insert(tk.END, "Error")
        elif text == "C":
            # Clear the Text widget
            screen.delete(1.0, tk.END)
        else:
            # Insert the button text into the Text widget
            screen.insert(tk.END, text)

    # Bind the clickbutton function to mouse clicks on all child widgets of the main window
    for button in root.winfo_children(): #for button in root.winfo_children(): loop allows you to iterate through all the child widgets of the main tkinter window
        button.bind("<Button-1>", clickbutton) #<Button-1> represents the left mouse button click event. .bind(event, function): This method is used to bind a particular event to a function for a widget.

    # Start the main event loop
    root.mainloop() #fundamental part of any tkinter-based GUI application. It is used to start the main event loop, which is responsible for handling user interactions and managing the GUI elements of application.  This function effectively keeps the tkinter application running and responsive to user actions until the main window is closed

if __name__ == "__main__":
    main()