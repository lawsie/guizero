# Auto pack or grid position the element
# INTERNAL ONLY
def auto_pack(self, master, grid, align):

    # If the master widget specifies grid, don't pack, otherwise auto pack
    # You always pack the tk object NOT the guizero object
    if master.layout_manager != "grid":
        self.tk.pack()
    else:

        # If they failed to specify grid coords
        if grid is None:
            error_format("Missing grid reference for " + self.description + ".\n" +
            "Please add a grid reference to make this object appear.")

        # They didn't specify 2 coords
        elif len(grid) != 2:
            error_msg = self.description + " has no grid position argument.\n"
            error_msg += "This widget will not be displayed!\n"
            error_msg += "Should be: List of two grid coordinates [row, column]"
            error_format(error_msg)
        else:

            # If no alignment, just place in grid with center align default
            if align is None:
                self.tk.grid(row=grid[0], column=grid[1])
            else:
                # Conversion to child friendly specifications (diags?)
                directions = {"top": "N", "bottom": "S", "left": "W", "right": "E"}
                align_this = "W" # Default to align left if they didn't specify something valid

                try:
                    align_this = directions[align]
                except KeyError:
                    error_msg = "Invalid align value ('"+ str(align) +"') for " + self.description + "\nShould be: top, bottom, left, right"
                    error_format(error_msg)

                # Place on grid
                self.tk.grid(row=grid[0], column=grid[1], sticky=align_this)


# Lambda-izer for making it easy to pass arguments with function calls
# without having to know what lambda does
def with_args( func_name, *args):
    return lambda: func_name(*args)



# Format errors in a pretty way
def error_format(error_message):
    print("------------------------------------------------------------")
    print("*** GUIZERO WARNING ***" )
    print(error_message)
    print("------------------------------------------------------------")

def deprecated(message):
    print("*** DEPRECATED: " + message)
