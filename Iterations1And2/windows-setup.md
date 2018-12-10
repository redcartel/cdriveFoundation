
Install the Windows Linux Subsystem:

[https://docs.microsoft.com/en-us/windows/wsl/install-win10]

You will likely have to restart your computer.

In the Microsoft Store, download and install Ubuntu 18.04

Launch Ubuntu 18.04, it will prompt you to create a username and password

Once you have done that execute the following command

sudo apt update

(sudo is the linux version of 'run as Administrator,' it will usually prompt you for your
password)

And then

sudo apt upgrade

Sometimes, on some machines, this process is *very* slow. Be patient,
I haven't seen it actually crash yet, but it can take over an hour.

Now type

sudo apt install python3 python3-pip

Finally type

nano ~/.bashrc

In this file, go all the way to the bottom and add the following lines:

alias python=python3
alias pip=pip3

Press control-O to save the file and then control-X to exit

type

bash

now type

python

It should launch the interpreter and tell you you are using a version that starts with 3

OK! You are done with Linux setup, you can close it.

Now download and install Visual Studio Code.

Go to view -> extensions and then install

Python (by Microsoft)
Code Runner (by Jun Han)
Markdown Preview Enhanced (by Yiyi Wang)

Now go to File->Preferences->Settings

Make sure "User Settings" is selected and then click on the three 
dots on the upper right hand corner and select "open settings.json"

Copy and paste the following json dictionary into the right hand panel, this
should be the entire contents of that panel:

{
   "workbench.colorTheme": "Default High Contrast",
    "editor.quickSuggestions": false,
    "editor.suggestOnTriggerCharacters": false,
    "editor.wordBasedSuggestions": false,
    "editor.quickSuggestionsDelay": 1000000,
    "editor.tabCompletion": false,
    "python.linting.enabled": false,
    "editor.parameterHints.enabled": false,
    "code-runner.respectShebang": true,
    "code-runner.runInTerminal": true,
    "window.zoomLevel": 2,
    "terminal.integrated.shell.windows": "C:\\Windows\\System32\\bash.exe",
}