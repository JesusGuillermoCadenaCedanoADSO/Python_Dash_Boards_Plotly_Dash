import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import requests

app = dash.Dash()

app.layout = html.Div([
    html.Div([
        html.Pre(
            id='counter_text',
            children='Active flights worldwide:'
        ),
        dcc.Interval(
            id='interval-component',
            interval=6000,  # 6000 milliseconds = 6 seconds
            n_intervals=0
        )
    ])
])

@app.callback(Output('counter_text', 'children'),
              Input('interval-component', 'n_intervals'))
def update_layout(n):
    url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1\
           &mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
    # Encabezado falso para simular un navegador
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    # Verifica si la solicitud fue exitosa
    if res.status_code == 200:
        data = res.json()
        print("datos json")
        print(data)
        # Verifica si "stats" está en la respuesta
        if "stats" in data and "total" in data["stats"]:
            counter = 0
            for element in data["stats"]["total"]:
                counter += data["stats"]["total"][element]
            return f'Active flights worldwide: {counter}'
        else:
            # Si no se encuentra "stats" o "total", mostrar mensaje informativo
            return 'No se pudo obtener la cuenta de vuelos. La estructura de datos ha cambiado.'
    else:
        # Si la solicitud falla, mostrar el código de estado HTTP
        return f'Error en la solicitud: {res.status_code}'

if __name__ == '__main__':
    app.run_server()
