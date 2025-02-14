import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# Add an import for pandas_datareader and datetime
import pandas_datareader.data as web
from datetime import datetime, date, timedelta
import os
import pandas as pd
api_key="3b95092f416ab61b6ac479d5e5c13f1fc1c6245e"
app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.Div([html.H3('Enter a stock symbol:',style={'paddingRight':'30px'}),
        dcc.Input(
        id='my_ticker_symbol',
        value='TSLA',
        style={'fontSize':24, 'width':75}
        )],style={'display':'inline-block', 'verticalAlign':'top'}
    ),
    html.Div([
            html.H3('Select start and end dates:'),
            dcc.DatePickerRange(
            id='my_date_picker',
            min_date_allowed = datetime(2015, 1, 1),
            max_date_allowed = datetime.today(),
            start_date = datetime(2018, 1, 1),
            end_date = datetime.today()
        )
    ], style={'display':'inline-block'}),
    dcc.Graph(
        id='my_graph',
        figure={
            'data': [
                {'x': [1,2], 'y': [3,1]}
            ]
        }
    )
])
@app.callback(
    Output('my_graph', 'figure'),
    [Input('my_ticker_symbol', 'value'),
     Input('my_date_picker', 'start_date'),
     Input('my_date_picker', 'end_date')
    ])
def update_graph(stock_ticker, start_date, end_date):
    # Use datareader and datetime to define a DataFrame
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')


    # We can provide other datetime examples here. 
    # For instance, to get the last 90 days stock activity:
    # start = datetime.today()-timedelta(days=90)
    # end = datetime.today()

    df = web.get_data_tiingo(stock_ticker,start=start,end=end, api_key=api_key)
    #print(df.head())

    # Obtener los valores de la segunda columna del MultiIndex
    fechas = df.index.get_level_values(1)
    fechas = pd.to_datetime(fechas).date
    
    # Change the output data
    fig = {
        'data': [
            {'x': fechas, 'y': df.close}
        ],
        'layout': {'title':stock_ticker}
    }
    return fig

if __name__ == '__main__':
    app.run_server()
