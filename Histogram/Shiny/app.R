library(shiny)

# Create the slider
ui <- fluidPage(
  titlePanel("Graph a standard normal distribution\n"),
  sidebarLayout(
    sidebarPanel(
      sliderInput(inputId = "random_numbers",
                  label = "Slide this to increase/decrease the number of values:",
                  min = 1,
                  max = 100,
                  value = 30)

    ),

    mainPanel(
      plotOutput(outputId = "distPlot")

    )
  )
)


# Create the histogram
# It is reactive to the input from "ui" function.
# It just draws numbers from a standard normal distribution
server <- function(input, output) {
    output$distPlot <- renderPlot({
      dist <- rnorm(input$random_numbers)
      hist(dist, col = "#75AADB", border = "white")
    })
  }


shinyApp(ui = ui, server = server)