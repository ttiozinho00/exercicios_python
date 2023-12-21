# Importando as bibliotecas necessárias
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Inicializando a aplicação Dash
app = dash.Dash(__name__)

# Layout do Dashboard
app.layout = html.Div([
    html.H1("Dashboard Interativo em Python"),
    dcc.Input(id='input', value='', type='text', debounce=True),
    html.Div(id='output'),
    dcc.Graph(id='scatter-plot')
])

# Callback para atualizar a saída e o gráfico com base na entrada do usuário
@app.callback(
    [Output(component_id='output', component_property='children'),
     Output(component_id='scatter-plot', component_property='figure')],
    [Input(component_id='input', component_property='value')]
)
def update_output_div(input_value):
    if input_value == '':
        return '', px.scatter(x=[], y=[], labels={'x': 'X', 'y': 'Y'}, title='Gráfico de Dispersão')
    else:
        # Gera dados para o gráfico de dispersão com base na entrada do usuário
        x_data = [len(input_value)]
        y_data = [ord(char) for char in input_value]

        # Cria o gráfico de dispersão usando Plotly Express
        scatter_plot = px.scatter(x=x_data, y=y_data, labels={'x': 'Comprimento da Entrada', 'y': 'Valor ASCII'},
                                  title='Gráfico de Dispersão')

        return f'Você digitou: "{input_value}"', scatter_plot

# Rodando o servidor web
if __name__ == '__main__':
    app.run_server(debug=True)
