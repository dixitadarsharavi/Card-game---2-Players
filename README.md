# Card game for 2 players:

A command line tool that demonstrates a card game between 2 players.

## Prerequisites:

- Minimum python version required(Python3)

## Setting up the environment:

- Extract the zip folder.
- Navigate to the root of the project directory.
- File system structure:
    - cardgamecli folder: It contains the source code of the application.
        - __init.py__: It is a empty file to tell Python that directory contains a package.
        - __main.py__: It is the entry point of my application. This file is used by the setup.py file in the root directory.
    - install.sh: This file is used to install the application in the local system. In the root directory of the CLI source code, running "pip3 install ." will    install this app using instructions provided in setup.py. Instead of manually running this command everytime, it will be useful to run it as a shell script.
    - README.md file: It gives brief introduction about the command line tool along with its usage and testing instructions.
    - setup.py:  I am importing the setup function from the setuptools package and calling it with a few parameters. The packages argument is just a list that indicates all of the include packages. In this project I have used only one which is cardgamecli. "entry_points" indicates what the runnable application will be called, and when run what exactly should be invoked. When command cardgamecli is executed it will run the main function in the __main__ module.
    - test_cardgamecli.py: This has the unit test cases for our application.

- Provide rights to execute install.sh (if not provided) ,using the below command in your terminal
``` sh      
 chmod 755 install.sh
```
- Run the script file using the below command,
``` sh      
 ./install.sh
```
- Run the below command to execute cardgamecli tool from terminal
``` sh      
 cardgamecli
```

Unit Test: In order to carry out unit tests, execute the below command

``` sh
python3 -m  unittest
```

Lastly, to uninstall the the CLI tool use this command,
``` sh      
pip3 uninstall cardgamecli
```