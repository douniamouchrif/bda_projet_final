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
from triggers import query5,query6,query7

question = "Automatisez au maximum les calculs de population quand une nouvelle année de recensement est ajoutée au niveau des communes. Factorisez au maximum le code avec des procédures stockées. "

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

def layout () :
 html.Div([
    html.Div(id='query-results')  
])
 
"""def display_query_results():
    results_div = html.Div([
        html.H2("Résultats des requêtes"),
        html.P("Résultat de la requête 1: " + str(query5)),
        html.P("Résultat de la requête 2: " + str(query6)),
        html.P("Résultat de la requête 3: " + str(query7)),
    ])
    
    return results_div

# Callback pour mettre à jour les résultats des requêtes
@callback(
    Output('query-results', 'children'),
    [Input('query-results', 'id')]  # Ajoutez un Input spécial pour déclencher le callback au démarrage de l'application
)
def update_query_results(trigger):
    return display_query_results()"""