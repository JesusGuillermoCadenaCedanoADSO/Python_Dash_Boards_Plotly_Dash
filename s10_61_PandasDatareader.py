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
    html.H3('Enter a stock symbol:'),
    dcc.Input(
        id='my_ticker_symbol',
        value='TSLA'
    ),
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
    [Input('my_ticker_symbol', 'value')])
def update_graph(stock_ticker):
    # Use datareader and datetime to define a DataFrame
    start = datetime(2017, 1, 1)
    end = datetime(2017, 12, 31)

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
