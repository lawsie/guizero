# Auto pack or grid position the element
# INTERNAL ONLY
def auto_pack(widget, master, grid, align):

    # If the master widget specifies grid, don't pack, otherwise auto pack
    # You always pack the tk object NOT the guizero object
    if master._layout_manager != "grid":
        widget.tk.pack()
    else:

        # If they failed to specify grid coords
        if grid is None or type(grid) is not list or len(grid) != 2:
            error_format(widget.description + " will not be displayed because it has a missing or " +
            "incorrect grid reference. The format should be grid=[x, y].")

        else:
            # If no alignment, just place in grid with center align default
            if align is None:
                widget.tk.grid(row=grid[1], column=grid[0])
            else:
                # Conversion to child friendly specifications (diags?)
                directions = {"top": "N", "bottom": "S", "left": "W", "right": "E"}
                align_this = "W" # Default to align left if they didn't specify something valid

                try:
                    align_this = directions[align]
                except KeyError:
                    error_format("Invalid align value ('"+ str(align) +"') for " + widget.description +
                    "\nShould be: top, bottom, left or right")

                # Place on grid
                widget.tk.grid(row=grid[1], column=grid[0], sticky=align_this)


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
