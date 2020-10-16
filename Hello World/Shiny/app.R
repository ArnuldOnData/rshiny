library(shiny)

ui <- fluidPage("My First Web-App in Shiny")

server <- function(input, output){
}


shinyApp(ui = ui, server = server)
