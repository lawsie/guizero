from guizero import App, MenuBar

def file_open():
    print("Open")

def file_exit():
    print("Exit")
    app.destroy()

def edit_copy():
    print("Copy")

def edit_cut():
    print("Cut")

def edit_paste():
    print("Paste")

app = App()
menubar = MenuBar(app,
                  toplevel=["File", "Edit"],
                  options=[
                      [ ["Open", file_open], ["Exit", file_exit] ],
                      [ ["Copy", edit_copy], ["Cut", edit_cut], ["Paste", edit_paste] ]
                  ])
app.display()
