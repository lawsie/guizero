# guizero

[Version 0.6.0](http://lawsie.github.io/guizero/changelog) (8th Feb 2019)

guizero is designed to allow children to quickly and easily create GUIs for their programs.

If you can download and unzip a file, you can [install guizero](#easy-installation) - **no special permissions or administrator rights are required**.

If you have administrator rights and are connected to the internet, you can use [pip to quickly install guizero](#install-using-pip).

guizero only requires `tkinter` to be installed, which is included with a standard Python installation on all platforms except Linux.

## Easy installation

Use this installation method if you do not have access to a terminal or command prompt on your computer.

1. Click the green "Clone or download" button and then "Download ZIP"

    ![Download the zip](docs-src/docs/images/download-zip.png)

2. Unzip the file

3. Open the `guizero-master` folder, then copy the `guizero` folder and paste it into your home directory

    ![Copy the guizero folder](docs-src/docs/images/copy-guizero.png)

4. That's it! When you write your guizero code, make sure you save it into your home directory.

## Install using pip

If you have administrator rights to your computer and are connected to the internet, you can use pip to quickly install guizero.

### Windows

1. Make sure you have pip installed - follow [this guide](https://projects.raspberrypi.org/en/projects/using-pip-on-windows) if you are not sure.
2. Open a command prompt
3. Type `pip3 install guizero` and press Enter

### Raspberry Pi

1. Open a terminal window
2. Type `sudo pip3 install guizero` and press Enter

### Mac OS
1. Open a terminal (you can search for it in the Launch Pad)

    ![Mac terminal](docs-src/docs/images/mac-terminal.png)

2. Type `sudo pip3 install guizero`

    ![Mac install screenshot](docs-src/docs/images/mac-install.png)

### Linux

1. Open a terminal
2. Install `tkinter` using your distribution's package manager, e.g. `sudo apt install python3-tk`
3. Install guizero using pip by typing `pip3 install guizero` or `sudo pip3 install guizero` if you dont have superuser rights

## Upgrading

- Raspberry Pi/Linux/Mac - `sudo pip3 install guizero --upgrade`
- Windows - `pip3 install guizero --upgrade`

## Mission statement
The aim of guizero is to make the process of creating simple GUIs quick, accessible and understandable for children.

## Aims
* Works with standard Python GUI library (and no need to install other libraries)
* Abstracts away details children find hard (such as Tkinter StringVar() objects)
* Accessible widget naming system to help children to build up a mental model
* Flexible enough to be used for projects up to A-Level standard, yet accessible to primary school children
* Comprehensive and accessible [documentation with examples](https://lawsie.github.io/guizero)
* Helpful error messages

## Documentation

[lawsie.github.io/guizero](https://lawsie.github.io/guizero)

## Contributing

Contributions are very welcome - please see [lawsie.github.io/guizero/contributing](https://lawsie.github.io/guizero/contributing) for notes, build and deployment instructions.

## Issues

All issues should be raise on [github.com/lawsie/guizero/issues](https://github.com/lawsie/guizero/issues)
