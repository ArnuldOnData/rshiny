This will create an interactive histogram. You will have a slider on the left and histogram on the right. 
Histogram generates a standard normal distribution from the number of values you select using the 
slider.

# How to use

Open your R interpreter (also known as REPL) and install **Shiny** library if not already done:

`> install.packages("shiny")`

`> library(shiny)`

Set a browser option: 

`> options(browser="firefox")`

`> runApp('app.R')`

You can see a slider on the left and a histogram on the right. You can change the values using the slider which will dynamically change the histogram. This is how it will look like:

![picture](https://i.postimg.cc/PryyCvWL/Screenshot-from-2020-10-18-12-30-33.png)

