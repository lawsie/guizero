# form converted from a tkinter example using 'Box'es for layout
# http://www.dreamincode.net/forums/topic/371440-tkinter-overview-with-a-fixed-width-grid/

from guizero import App, MenuBar, Text, TextBox, Combo, Slider, CheckBox, ButtonGroup, Box, PushButton, info, yesno

# Draw the form using 'guizero' wrapper for tkinter
app = App("Simple Window", 400, 300, layout="grid")

# Setup the functions needed by the GUI controls
def exit_function():
    print("File option")
    app.destroy()

def edit_function():
    print("Edit option")

def do_salaryScale(slider_value):
    salaryLabel.value = "Salary : "+str(slider_value)

def do_fullTimeCheckBox():
    if fullTimeCheckBox.value == 1:
        app.title=("Simple Window (full-time)")
    else:
        app.title=("Simple Window")

def do_jobButtonGroup():
    jobTitleLabel.value = jobButtonGroup.value_text

def do_okPushButton():
    info("Information", "Thank you!")

def do_closePushButton():
    if yesno("Exit?", "Exit program?") == True:
        app.destroy()

menubar = MenuBar(app,
                  toplevel=["File"],
                  options=[
                      [ ["Exit", exit_function] ]
                  ])

# Layout the app controls
firstNameLabel = Text(app, text="First Name", grid=[0,0], align="left", size=10)
lastNameLabel = Text(app, text="Last Name", grid=[0,1], align="left", size=10)
countryLabel = Text(app, text="Country", grid=[0,2], align="left", size=10)
addressLabel = Text(app, text="Address", grid=[0,3], align="left", size=10)

firstNameText = TextBox(app, width=25, grid=[1,0])
lastNameText = TextBox(app, width=25, grid=[1,1])
countryCombo = Combo(app, options=['United Kingdom', 'United States', 'France'], selected='United Kingdom', grid=[1,2])
box = Box(app, grid=[1,3], layout="grid")

addressText1 = TextBox(box, width=25, grid=[0,0])
addressText2 = TextBox(box, width=25, grid=[0,1])
addressText3 = TextBox(box, width=25, grid=[0,2])
addressText4 = TextBox(box, width=25, grid=[0,3])
addressText5 = TextBox(box, width=25, grid=[0,4])
addressText6 = TextBox(box, width=25, grid=[0,5])

jobTitleLabel = Text(app, text="TBA", grid=[1,4], size=10)

salaryLabel = Text(app, text="Salary : ", grid=[2,0], align="left", size=10)
salaryScale = Slider(app, start=10000, end=100000, grid=[2,1], command=do_salaryScale, align="left")

fullTimeCheckBox = CheckBox(app, text="Full-time?", grid=[2,2], command=do_fullTimeCheckBox, align="left")
jobButtonGroup = ButtonGroup(app, options=["Programmer", "Developer", "Web Developer", "Designer"],
                             selected=0, grid=[2,3], command=do_jobButtonGroup, align="left")
box1 = Box(app, grid=[2,4], layout="grid", align="left")
okPushButton = PushButton(box1, text="OK", command=do_okPushButton, grid=[0,0], padx=5, pady=5)
closePushButton = PushButton(box1, text="Close", command=do_closePushButton, grid=[2,0], padx=5, pady=5)


app.display()
