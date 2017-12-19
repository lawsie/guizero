## Common methods

These methods can be called upon any guizero widget.

| Method        | Takes     |  Description                |
| ------------- | --------- |  -------------------------- |
| after(time, command)   | time (int), command (function name)   | Schedules a **single** call to `command` after `time` milliseconds. (To repeatedly call the same command, use `repeat()`)  |
| repeat(time, command)  | time (int), command (function name)  | Repeats `command` every `time` milliseconds. This is useful for scheduling a function to be regularly called, for example updating a value read from a sensor.   |
| cancel(command)   | command (function name) | Cancels a scheduled call to `command`    |
| destroy()   | -  | Destroys the widget    |
| disable()  | - | Disables the widget so that it is "greyed out" and cannot be interacted with   |
| enable()  | -  | Enables the widget   |
| focus()  | -  | Gives focus to the widget (e.g. focusing a `TextBox` so that the user can type inside it)  |
| hide()  | -   | Hides the widget from view. This method will unpack the widget from the layout manager.   |
| show()  | - | Displays the widget   |
