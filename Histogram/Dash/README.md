This will create an interactive histogram. You will have a slider on the left and a histogram on the right. 
Histogram generates a standard normal distribution from the number of values you select using the 
slider.

# How to use

First, make sure you have Python installed. Then we will do it in a few steps:

 - Create a virtual environment
 - Install **Dash** in the virtual environment
 - Run the program 
 

**NOTE**: I use https://en.wikipedia.org/wiki/Arch_Linux . If you use some other OS then you need to search a bit for how you can do the 
                 same on your OS.  

 
## Creating a virtual environment
 
 I don't like to pollute the systemwide installation of Python. Unless there is a package I am gonna use every day (**iPython** e.g.), 
 for general day-to-day development I like to keep the systemwide Python untouched. When we want to play with a lot of stuff, we
 generally break and re-install a lot of stuff and virtual environments are great for such kind of work. Sure it takes more space but it 
 keeps your Python installation and your OS clean. 
 
 As of Python 3.5, **venv** is the recommended tool for creating virtual environments. Open a terminal or X-terminal and do this:

`python -m venv python-slider`
`cd python-slider`
`source bin/activate`

It will change your terminal prompt to this:

![picture](https://i.postimg.cc/YCGGm8jy/Screenshot-from-2020-10-18-12-47-30.png)

You can verify that you are in a local Python environment:

![picture](https://i.postimg.cc/P5SCcc9x/Screenshot-from-2020-10-18-12-50-07.png)

Then we will upgrade **pip** and install **wheel**, **Dash** and **Pandas**:

`pip install --upgrade pip`

`pip install wheel`

`pip install dash`

`pip install pandas` 



## Running the app

Just copy the *app.py* into the virtual environment you created above and then do:

`python app.py`

and it will start the web-server:

![picture](https://i.postimg.cc/8zHjr5Ss/Screenshot-from-2020-10-18-13-06-50.png)

You can just copy-paste the given address in your browser: `http://127.0.0.1:8050/`. Don't worry about the warning. 
We are running the server in debug mode which is okay when we are doing development. This is how it will  look like:

![picture](https://i.postimg.cc/qRnhbHY3/Screenshot-from-2020-10-18-12-31-06.png)

Dash automatically refreshes the page. You can change the values on the slider and notice how the histogram changes with it. 

More info here:

https://plotly.com/dash/
