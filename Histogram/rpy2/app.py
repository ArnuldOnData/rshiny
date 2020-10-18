import rpy2
from rpy2.robjects.packages import importr

base = importr('base')
utils = importr('utils')
utils.chooseCRANmirror(ind=1)
utils.install_packages('shiny')
shiny = importr('shiny')

base.options(browser="firefox")

# Create the slider

rpy2.robjects.r('''ui <- fluidPage(
  titlePanel("Graph a standard normal distribution\n"),
  sidebarLayout(sidebarPanel(sliderInput(inputId = "random_numbers",
                  label = "Slide this to increase/decrease the number of values:",
                  min = 1,
                  max = 100,
                  value = 30)),
        mainPanel(plotOutput(outputId = "distPlot"))))''')


# Create the histogram
rpy2.robjects.r('''server <- function(input, output) {
    output$distPlot <- renderPlot({
      dist <- rnorm(input$random_numbers)
      hist(dist, col = "#75AADB", border = "white")
    })
  }''')


r_ui =  rpy2.robjects.globalenv['ui']
r_server =  rpy2.robjects.globalenv['server']

appcall = shiny.shinyApp(ui = r_ui, server = r_server)
print(appcall)
