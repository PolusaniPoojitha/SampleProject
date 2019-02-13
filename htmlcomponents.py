import dash
import dash_table
import dash_html_components as html
import pandas as pd

df = pd.read_csv('C:/Users/poopolus/Documents/Poojitha/Optimizer/NationalBudgetSimulator.csv')
df2 = pd.read_csv('C:/Users/poopolus/Documents/Poojitha/Optimizer/Aportion Spends.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Label("National Budget Simulator- Non Core Segment"),
    dash_table.DataTable(
       id='table',
       columns=[{"name": i, "id": i} for i in df.columns],
       data=df.to_dict("rows"),
       style_table={'width': '50%'},),
    dash_table.DataTable(
        id='table2',
        columns=[{"name": i, "id": i} for i in df2.columns],
        data=df2.to_dict("rows"),
        style_table={'width': '50%'})
                        ]
                    )



if __name__ == '__main__':
    app.run_server(debug=True)