A program to print "Hello World". 

I use command-line REPL (R interpreter) to write code. By default "browser" is an empty string in R interpereter on Linux. 
So, you need to set browser option before you run this program. You can use Chrome or whatever you like:

`> options(browser="firefox")`

Then install Shiny (it will take a while), import it and run the program:

`> install.packages("shiny")`

`> library(shiny)`

`> runApp("app.R")`

It will automatically open the browser and show you the "Hello World" like this:

![picture](https://i.postimg.cc/C5NS4xTR/Screenshot-from-2020-10-17-08-46-17.png)

Port number is just a random port number chosen by Shiny. To understand why we have used "ui" and "server", go to this offical docs page:  https://shiny.rstudio.com/tutorial/written-tutorial/lesson1/

