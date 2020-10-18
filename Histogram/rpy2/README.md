This will create an interactive histogram. You will have a slider on the left and histogram on the right. 
Histogram generates a standard normal distribution from the number of values you select using the 
slider.

It is a Python program calling R functions using **rpy2** package. 


# Preparation

First, create a virtual environment and install necesary packages:

`python -m venv python-rpy2`

`cd python-rpy2`

`source bin/activate`

`pip install --upgrade pip`

`pip install wheel`

`pip install rpy2`

That is all you need. For complete details, see here:

https://github.com/ArnuldOnData/rshiny/blob/main/Histogram/Dash/README.md

As an alternative, you can use my *requirements.txt* too. 


## How to use 

Make sure you have *firefox* installed. If not, then you can change the browser option in *app.py* to your preferred browser. 
Then just copy the file *app.py* in the virtual environment folder you created in last step and do this:

`python app.py`

This is how it will look like:

![picture](https://i.postimg.cc/zBj0xfBy/Screenshot-from-2020-10-18-15-00-34.png)

You can see a slider on the left and a histogram on the right. You can change the values using the slider which will dynamically change the
histogram.  Congratulations. You just ran your R program in Python :-) 




## More Info:

https://shiny.rstudio.com/tutorial/written-tutorial/lesson1/

https://rpy2.github.io/


http://www.alshum.com/shiny-reactive/
