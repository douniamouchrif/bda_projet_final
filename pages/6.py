# Dash imports
import dash
from dash import html, dcc, Input, Output, State
from dash import register_page, callback
from dash import ctx, no_update, ALL
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output

# Dash extensions
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
#from plan_exe import exe_query1, explain_results

question = "Comparer et expliquer le coût d'exécution de différentes requêtes. Faites apparaître les différents algorithmes de jointure ou différentes stratégies de tri en jouant en particulier sur la cardinalité des relations."

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Définition du layout de votre application Dash
def layout():
    return html.Div([
        html.Div(id='query-results6')  # Div pour afficher les résultats des requêtes
    ])

"""@callback(
    Output('query-results6', 'children'),
    [Input('query-results6', 'id')]  
)
def update_query_results(trigger):
    return display_query_results()"""