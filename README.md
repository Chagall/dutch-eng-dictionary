# Dutch-English Dictionary
A Dutch-to-English, and vice-versa, dictionary I built using Python3 and SQLite3.
The reason I made it was to help me memorize the words I learned while studying Dutch on Duolingo. 
If somehow you seemed to be interested in also using it, follow the instructions below.
**Currently the dictionary is still incomplete in terms of words, since I'm still learning, and it uses a Command-Line Interface (CLI).**

# Instructions:

## Python installation
First of all you need to have Python 3.x installed in your machine. I believe any python 3 version will do, but as a precaution, try to install the latest one.

### If you are using Windows 
Download the [Latest Python 3 Release.](https://www.python.org/downloads/windows/) 
At the time of this writing the latest release is Python 3.5.1

### If you are using a debian based distribution of Linux or Mac OS X
Type the command below inside the Terminal:
> sudo apt-get install python3

### If you are using other types of Linux distributions
The official Python page also provides python's source code, which you can [download here.](https://www.python.org/downloads/source/)

You will have to download the source code, extract it and compile it by yourself. Hopefully there are tons of tutorials on the internet which can help you. Just google: **how to compile python in terminal Linux (or OS X)** and you will find loads of websites that will help you through the process.

**Ps:** Good luck compiling it :p

## SQLite installation (sqlite3)

Now that you have sucessfully installed python, the next step is to relax and chill out. According to [What's New in Python 2.5](https://docs.python.org/2.7/whatsnew/2.5.html#the-sqlite3-package), 
the pysqlite module [(pysqlite.org)](http://www.pysqlite.org/), a wrapper for the SQLite embedded database, has been added to the standard library under the package name sqlite3 .

If you happen to have compiled python's source code, there is a small chance that somehow sqlite3 didn't come with it. It happened to me once when I compiled python myself.

In this case, you can try to type the following command on the terminal:
> pip install sqlite

Pip is an acronym for Python Package Index. In case you don't have it installed, try to download it from the [official website.](https://pypi.python.org/pypi/pip/)

## Running the Dictionary
Now that you have everything you need installed you can start to use the Dictionary.

To run it, navigate through the folders: dutch-eng-dictionary > Object Oriented Implementation (current) > and run Dictionary.py on terminal or with your prefered IDE.


