# Installation

guizero is designed to allow new learners to quickly and easily create GUIs for their programs.

If you can download and unzip a file, you can [install guizero](#easy-install) - **no special permissions or administrator rights are required**.

If you have administrator rights and are connected to the internet, you can [use the command line to install or upgrade guizero](#install-using-command-line) (recommended).

## Easy install

1. Go to the [guizero repository](https://github.com/lawsie/guizero) on GitHub.

2. Click the green "Code" button and then "Download ZIP"

    ![Download the zip](images/download-zip-annotated.png)

3. Open the zip file

4. Open the `guizero-master` folder, then copy the `guizero` folder and paste it into your home directory

    + Windows

        ![Copy the guizero folder in windows](images/copy-guizero-annotated.png)

    + macOS

        ![Copy the guizero folder in macos](images/copy-guizero-macos-annotated.png)

5. That's it! When you write your guizero code, make sure you save it into your home directory.

## Install using command line

You can use the command prompt to install guizero for:

+ [Windows](#windows)
+ [macOS](#macos)
+ [Raspberry Pi](#raspberry-pi)
+ [Linux](#linux)

`pip` can also be used to [install additional features](#additional-features-install) and [upgrade guizero](#upgrading).

### Windows

1. Open a command prompt by clicking **Start** > **Windows System** > **Command Prompt**, or by typing 'command' into the start menu's search bar.

    ![windows command prompt](images/windows_command_prompt_app.png)

2. Type this command to use `pip` to install guizero and press enter:

    ```
    pip3 install guizero
    ```

![windows pip install](images/windows_pip_install.gif)

If you experience problems, have a look at this guide to [_Using pip on Windows_](https://projects.raspberrypi.org/en/projects/using-pip-on-windows).

### macOS

1. Open a terminal window by clicking **Applications** > **Utilities** > **Terminal**, or by typing 'terminal' into the desktop's search bar.

    ![Mac terminal](images/mac-terminal.png)

2. Type this command to use `pip` to install guizero and press enter:

    ```
    pip3 install guizero
    ```

    ![mac pip install](images/mac_pip_install.gif)

### Raspberry Pi

1. Open a terminal window by clicking **Menu** > **Accessories** > **Terminal**.

    ![pi terminal](images/pi-terminal.png)

2. Type this command to use `apt` to install guizero and press enter:

    ```
    sudo apt-get install python3-guizero
    ```

    ![run sudo apt-get install python3-guizero](images/pi_apt_install.gif)

**Note:** The installation available via apt may not be the latest. You can always install the latest version using `pip`.

### Linux

1. Open a terminal
2. Install `tkinter` using your distribution's package manager, e.g. `sudo apt install python3-tk`
3. Install guizero using pip by typing `pip3 install guizero` or `sudo pip3 install guizero` if you don't have superuser rights

    ![linux pip install](images/linux_pip_install.gif)

**Note:** If you are using Debian, you alternatively have the option to install guizero via apt
`sudo apt-get install python3-guizero`

### Install additional features

To use the additional [image features](images.md) of guizero such as:

- JPG image support
- scaling images
- animated gifs

... you will need to install [PIL/pillow (python imaging library)](https://pypi.org/project/Pillow/).

You can install pillow using `pip`:

```
pip3 install guizero[images]
```

Or using `apt` on Raspberry Pi / Linux

```
sudo apt-get install python3-pillow
```

The additional image features are not available to install using the easy install method.

### Upgrading guizero

Depending how you installed guizero will dictate how you should upgrade

Using `pip`:

```
pip3 install guizero --upgrade
```

Using `apt`

```
sudo apt-get install python3-guizero
```

If you installed guizero using the easy install method, to upgrade you should follow the same easy installation steps to download the latest version of guizero, then delete the old guizero folder and replace it with the newest version.
