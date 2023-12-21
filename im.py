import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Hey Dohtuuur", style={'text-align': 'center', 'font-size': 60, 'background-color':'darkblue', 'color': 'white' }),
    html.Div(html.Img(src='https://thumbs.dreamstime.com/b/little-girl-saying-hi-illustration-cartoon-74257617.jpg', style={'width': '15%', 'height': '15%', 'margin': 'auto'}), style={'text-align': 'center'}),
    
    html.Div(html.Label("Do you want to know something?", style={'margin': 'auto', 'text-align': 'center', 'font-size': 45})),
    
    dcc.RadioItems(
        id='option-selector',
        options=[
            {'label': 'Yes', 'value': 'Yes'},
            {'label': 'No', 'value': 'No'},
        ],
        value=None,  # Default value
        labelStyle={'display': 'block', 'text-align': 'center', 'font-size': 40},
    ),
    
    html.Div(id='response-message', style={'text-align': 'center', 'margin-top': '20px'}),
    
    # Additional block appearing after selecting "Yes"
    html.Div([
        html.Div(html.Button('So What', id='so-what-button', n_clicks=0, style={'display': 'none', 'font-size': 40, 'text-align': 'center'})),
        html.Div(id='so-what-message', style={'text-align': 'center', 'margin-top': '20px', 'font-size': 40}),
    ]),
])

# Define callback to update the message and enable/disable "So what?" button
@app.callback(
    [Output('response-message', 'children'),
     Output('so-what-button', 'style')],
    [Input('option-selector', 'value')]
)
def update_message(selected_option):
    style = {'color': 'green', 'font-size': 30} if selected_option == 'Yes' else {'color': 'red', 'font-size': 30}  # Color based on the selected option
    if selected_option == 'Yes':
        message = "your Birthday's comiiiiing! Only 8 days left......"
        button_style = {'display': 'block'}
        
    elif selected_option == 'No':
        message = "Error, try again."
        button_style = {'display': 'none'}
        
    else:
        message = ""
        button_style = {'display': 'none'}

    return message, button_style

# Define callback for "So What" button click
@app.callback(
    Output('so-what-message', 'children'),
    [Input('so-what-button', 'n_clicks'),
     Input('option-selector', 'value')]
)
def so_what_message(n_clicks, selected_option):
    if n_clicks > 0 and selected_option == 'Yes':
        return "You Have Not Chosen your Birthday Gift yet."
    else:
        return ""

# Reset the 'n_clicks' property of the "So What" button whenever the option is changed
@app.callback(
    Output('so-what-button', 'n_clicks'),
    [Input('option-selector', 'value')]
)
def reset_so_what_button(selected_option):
    return 0

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
