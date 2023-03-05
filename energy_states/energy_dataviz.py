import plotly.express as px
import plotly.io as pio
import pandas as pd
# import dash
# from dash import dcc
# from dash import html

def consumed_graph():
    """
    Create a bar graph that compares the selected state(s) based on the cleaned 
    Total Energy Consumed per Capita data from the U.S. Energy Information
    Administration (EIA).
    
    Returns:
        A bar graph (figure) based on the cleaned Energy Consumed data  
    """
    title_section = "<b>Energy Consumed by State</b>"
    clean_consumed_data = pd.read_csv(
            "energy_states/eia_states_data/cleaned_data/cleaned_consumed.txt"
)
    #FYI .columns[2] is the Consumed, CO2 Emissions, Expenditures, or Production
    #   for each each State & DC;
    #   .columns[3] is the percentage of the total U.S. output for .columns[2] 
    bar_graph = create_graph(clean_consumed_data, 
            clean_consumed_data.columns[2], 
            clean_consumed_data.columns[3], 
            title_section
)
    
    return bar_graph


def emissions_graph():
    """
    Create a bar graph that compares the selected state(s) based on the cleaned 
    Carbon Dioxide Emissions data from the U.S. Energy Information
    Administration (EIA).
    
    Returns:
        A bar graph (figure) based on the cleaned CO2 Emissions data  
    """
    title_section =  "<b>Carbon Dioxide Emissions by State</b>"
    clean_emissions_data =  pd.read_csv(
            "energy_states/eia_states_data/cleaned_data/cleaned_emissions.txt"
)
    #Comment on lines 22-24 describes .columns[2] & .columns[3]
    bar_graph = create_graph(clean_emissions_data, 
            clean_emissions_data.columns[3], 
            clean_emissions_data.columns[2], 
            title_section
)
    
    return bar_graph


def expenditures_graph():
    """
    Create a bar graph that compares the selected state(s) based on the cleaned 
    Total Energy Expenditures per Capita data from the U.S. Energy Information
    Administration (EIA).
    
    Returns:
        A bar graph (figure) based on the cleaned Energy Expenditures data   
    """
    title_section = "<b>Energy Expenditures by State</b>"
    clean_expenditures_data =  pd.read_csv(
            "energy_states/eia_states_data/cleaned_data/cleaned_expenditures.txt"
)
    #Comment on lines 22-24 describes .columns[2] & .columns[3]
    bar_graph = create_graph(clean_expenditures_data, 
            clean_expenditures_data.columns[2], 
            clean_expenditures_data.columns[3], 
            title_section
)
    
    return bar_graph


def production_graph():
    """
    Create a bar graph that compares the selected state(s) based on the cleaned 
    Total Energy Production data from the U.S. Energy Information Administration
    (EIA).
    
    Returns:
        A bar graph (figure) based on the cleaned Energy Production data 
    """
    title_section = "<b>Energy Production by State</b>"
    clean_production_data =  pd.read_csv(
            "energy_states/eia_states_data/cleaned_data/cleaned_production.txt"
)
    #Comment on lines 22-24 describes .columns[2] & .columns[3]
    bar_graph = create_graph(clean_production_data, 
            clean_production_data.columns[3], 
            clean_production_data.columns[2], 
            title_section
)
    
    return bar_graph


def create_graph(data, y_variable, added_hover_variable, title_section):
    """
    Create a bar graph.
    
    Input:
        data (dataframe): The dataframe that is the basis for the graph
        y_variable (string): The name of the column to be the dependent (y)
            variable of the graph
        added_hover_variable (string): The name of the column to be added to the
            bar(s) of the graph when the user's mouse is hovering over it
        title_section (string): The title for the bar graph
    
    Returns:
        
    """
    fig = px.bar(data, x = "State", y = y_variable, text = "Rank",  
            color = "State", color_discrete_sequence = ["mediumpurple", "red"], 
            #Patterns assist those who are colorbind
            pattern_shape = "State", pattern_shape_sequence=["+", "x"],
            hover_data = [added_hover_variable]
)
    
    #This moves the "Rank" column info ontop of the bar graph instead of inside
    fig.update_traces(textposition = 'outside', textfont = dict(size = 12.5))
    
    fig.update_layout(showlegend = False,  font = dict(size = 15),
            title = {"text": title_section
            , "y": 0.95, "x": 0.5, "xanchor": "center", "yanchor": "top"}, 
            yaxis = dict(title = y_variable, title_font = dict(size = 16), 
            automargin = True)
)
    
    return fig


# app = dash.Dash()

# app.layout = html.Div([
#     dcc.Graph(id = "Energy Consumed", figure = consumed_graph())
# ])

# app.run_server(debug=True, use_reloader=False) 
# if __name__ == '__main__':
#     app.run_server()

def create_graph_png(graph, path):
    """
    Take a bar graph and save it to the prescribed path.
    
    Inputs:
        graph (figure)
        path (string): A string to where the graph should be saved
    """
    #Be sure to ($ pip3 install -U kaleido) to use the following line then 
    # ($ pip3 uninstall -y kaleido) to prevent potential issues
    graph_png = pio.to_image(graph, format = 'png')
    
    with open(path, "wb") as f:
        f.write(graph_png)


def intialize_graph_pngs():
    """
    Intialize each bar graph function and input the result into the 
    create_graph_png function.
    """
    create_graph_png(consumed_graph(), 
            "energy_states/eia_states_figures/consumed_graph.png")
    create_graph_png(emissions_graph(),
            "energy_states/eia_states_figures/emissions_graph.png")
    create_graph_png(expenditures_graph(),
            "energy_states/eia_states_figures/expenditures_graph.png")
    create_graph_png(production_graph(),
            "energy_states/eia_states_figures/production_graph.png")


#run function from cd 30122-project-the-cody-bills within a poetry shell
#   poetry run python energy_states/energy_dataviz.py
intialize_graph_pngs()