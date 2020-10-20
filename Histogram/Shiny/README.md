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



## How it works

A **Shiny** app needs only one file *app.R* which needs to have 3 things:
 - user interface part  - function called *ui* in *app.R*
 - server part  - function called *server* in *app.R*
 - a call to shinyApp() with *ui* and *server* passed as arguments.
 
 *ui* function creates the slider and  receives the input whenever you change it.
 *server* function takes input from *ui* and then creates a standard normal distribution 
 with that value and then displays a histogram of that for you. 


More Info:

https://shiny.rstudio.com/tutorial/written-tutorial/lesson1/

https://www.r-bloggers.com/2013/02/normal-distribution-functions/

https://en.wikipedia.org/wiki/Normal_distribution

https://cran.r-project.org/doc/manuals/r-release/R-lang.html

