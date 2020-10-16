Running a web-server "Hello World" program in Python requires a few steps:
 - Creating a virtual environment
 - Installing "Flask" in the virtual environment
 - Running the python program using Flask
 
 
 # Creating a virtual environment
 
 I don't like to pollute systemwide installation of Python. Unless there is a package I am gonna use everyday (**iPython** e.g.), for general day-to-day stuff, 
 I like to keep the systemwide Python untouched. When we want to play with a lot of stuff, we break and re-install lot of stuff and virtual
 environments are great for such kind of work. Sure it takes more space but it keeps your Python installation and your OS clean. 
 
 As of Python 3.5, **venv** is the recommended tool for creatin virtual environments. These three tools are needed, you can install them using your package manager: Python, venv and pip. Then open a terminal or X-terminal and do this:
 
 `Python -m venv flask-hello`
 
 `cd flask-hello`
 
 `source bin/activate`
 
1st line of code will create a *flask-hello* folder with all the necessary stuff. 3rd line will activate the enviroment. This is how it should look:

![picture](https://i.postimg.cc/mrrrNtwK/Screenshot-from-2020-10-16-22-50-20.png)

You can check to be sure you are running Python local to the virtual environment you just created:

![picture](https://i.postimg.cc/J73G8VG6/Screenshot-from-2020-10-16-22-51-39.png)




# Installing Flask in virutal environment
First upgrade pip and then install Flask:

`pip install --upgrade pip`

`pip install flask`


Now we are ready to run the program:

`export FLASK_APP=hello.py`

`flask run`

This will print some text in terminal and then open a tab/window in your browser immediately:

![picture](https://i.postimg.cc/bwRvXQrZ/Screenshot-from-2020-10-16-23-20-06.png)

![picture](https://i.postimg.cc/FKRN28w6/Screenshot-from-2020-10-16-23-21-37.png)



 https://flask.palletsprojects.com/en/1.1.x/quickstart/
 
 https://docs.python.org/3/library/venv.html


I highly recommend **iPython** interpreter. 
 Use your OS's package manager to install it.
