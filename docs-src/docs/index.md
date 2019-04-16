# Installation

guizero is designed to allow new learners to quickly and easily create GUIs for their programs.

If you can download and unzip a file, you can [install guizero](#easy-install) - **no special permissions or administrator rights are required**.

If you have administrator rights and are connected to the internet, you can use [pip to install guizero](#install-using-pip).

## Easy install

1. Go to the [guizero repository](https://github.com/lawsie/guizero) on GitHub.

2. Click the green "Clone or download" button and then "Download ZIP"

    ![Download the zip](images/download-zip.png)

3. Open the zip file

4. Open the `guizero-master` folder, then copy the `guizero` folder and paste it into your home directory

    + Windows
    ![Copy the guizero folder in windows](images/copy-guizero-annotated.png)

    + macOS
    ![Copy the guizero folder in macos](images/copy-guizero-macos-annotated.png)

5. That's it! When you write your guizero code, make sure you save it into your home directory.

## Install using pip

You can use the command prompt and `pip` to install guizero for:

+ [Windows](#windows)
+ [macOS](#macos)
+ [Raspberry Pi](#raspberry-pi)
+ [Linux](#linux)

`pip` can also be used to [install additional features](#additional-features-install) and [upgrade guizero](#upgrading).

### Windows

1. Open a command prompt by clicking **Start** > **Windows System** > **Command Prompt**, or by typing 'command' into the start menu's search bar.

    ![windows command prompt](images/windows_command_prompt_app.png)

2. Type this command and press enter:

    ```
    pip3 install guizero
    ```

![windows pip install](images/windows_pip_install.gif)

If you experience problems, have a look at this guide to [_Using pip on Windows_](https://projects.raspberrypi.org/en/projects/using-pip-on-windows).

### macOS

1. Open a terminal window by clicking **Applications** > **Utilities** > **Terminal**, or by typing 'terminal' into the desktop's search bar.

    ![Mac terminal](images/mac-terminal.png)

2. Type this command and press enter:

    ```
    pip3 install guizero
    ```

    ![mac pip install](images/mac_pip_install.gif)

### Raspberry Pi

1. Open a terminal window by clicking **Menu** > **Accessories** > **Terminal**.

    ![pi terminal](images/pi-terminal.png)

2. Type this command and press enter:

    ```
    sudo pip3 install guizero
    ```

    ![run pip install guizero](images/pi_pip_install.gif)

### Linux

1. Open a terminal
2. Install `tkinter` using your distribution's package manager, e.g. `sudo apt install python3-tk`
3. Install guizero using pip by typing `pip3 install guizero` or `sudo pip3 install guizero` if you dont have superuser rights

    ![linux pip install](images/linux_pip_install.gif)

### Additional features install

To use the additional [image features](images.md) of guizero such as:

- JPG image support
- scaling images
- animated gifs 

... you will need to install guizero with the pip command:

- Windows / macOS

    ```
    pip3 install guizero[images]
    ```

- Linux / Raspberry Pi

    ```
    sudo pip3 install guizero[images]
    ```

### Upgrading

Upgrade guizero using the pip command 

- Windows / macOS

    ```
    pip3 install guizero --upgrade
    ```

- Linux / Raspberry Pi

    ```
    sudo pip3 install guizero --upgrade
    ```
