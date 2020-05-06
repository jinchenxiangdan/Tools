import tkinter as tk
import crossref_commons.retrieval

json_data = crossref_commons.retrieval.get_publication_as_json('10.2458/azu_js_rc.55.16189')


def search():
    print("starting search...")

def message(title, msg):
    tk.messagebox.showinfo(title=title, message=msg)
    # show info
    # show warning
    # show error
    # ask question


def main():
    # design a GUI
    window = tk.Tk()
    window.title('DOI-metadata')
    window.geometry('800x600')

    # build a container 
    lable_input = tk.Frame(window)
    lable_input.pack()

    output = tk.Frame(window)
    output.pack()


    # lable
    lable = tk.Label(lable_input, text='DOI').place(x=50, y=250)
    
    # entry
    entry = tk.Entry(lable_input).place(x=100, y=250)
    
    
    # search button 
    button_search = tk.Button(lable_input, text='Search', width=10, bg='blue', command=search)
    button_search.pack()
    
    # Text (output)
    text = tk.Text(output, height=10)
    text.pack()

    # run the GUI
    window.mainloop()

if __name__ == "__main__":
    # main()
    print(json_data)




