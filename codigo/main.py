from tkinter import Tk, Menu

def about():
    print("calling about")

def main():
    root = Tk()

    #criando o menu
    menubar=Menu(root)
    root.config(menu=menubar)

    #criando os sub-menu
    subMenu=Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=subMenu)

    #menubar->file->new project
    subMenuNew=Menu(menubar, tearoff=0)
    subMenu.add_cascade(label="New Project", menu=subMenuNew, state="disable")
    subMenuNew.add_command(label="Python project")
    subMenuNew.add_command(label="Java project")

    subMenu.add_command(label="Exit")

    #subMenu.entryconfig("New Project", state="normal")

    

    

    subMenuHelp=Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=subMenuHelp)
    subMenuHelp.add_command(label="About", command=about)



    root.geometry("400x400+0+0")
    root.mainloop()

if __name__ == "__main__":
    main()

