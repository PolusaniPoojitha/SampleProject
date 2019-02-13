import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

df = pd.read_csv('C:/Users/poopolus/Documents/Poojitha/Optimizer/NationalBudgetSimulator.csv')
df2 = pd.read_csv('C:/Users/poopolus/Documents/Poojitha/Optimizer/Aportion Spends.csv')
df3 = pd.read_csv('C:/Users/poopolus/Documents/Poojitha/Optimizer/Proportion of Bookings.csv')

app = dash.Dash(__name__)

app.layout = html.Div(style={'float': 'left'}, children=[
                        html.Div(children=[
                                    html.Label("National Budget Simulator- Non Core Segment"),
                                    dash_table.DataTable(
                                                            id='table',
                                                            columns=[{"name": i, "id": i} for i in df.columns],
                                                            data=df.to_dict("rows"),
                                                            style_table={'width': '50%',
                                                                         },),
                                    dash_table.DataTable(
                                                            id='table2',
                                                            columns=[{"name": i, "id": i} for i in df2.columns],
                                                            data=df2.to_dict("rows"),
                                                            style_table={'width': '50%', },),
                                    dash_table.DataTable(
                                                            id='table3',
                                                            columns=[{"name": i, "id": i} for i in df3.columns],
                                                            data=df3.to_dict("rows"),
                                                            style_table={'width': '50%',
                                                                         'float': 'center'}, ),
                                         ]),
                        html.Div(children=[
                                    html.Label("Enter over all budget"),
                                    html.Br(),
                                    dcc.Input(id='input-box', type='text'),
                                    html.Button('Optimize Budget', id='button'),
                                    html.Button('DMA Level Media Mix', id='Dma level media mix')
                                            ])

                      ])


if __name__ == '__main__':
    app.run_server(debug=True)