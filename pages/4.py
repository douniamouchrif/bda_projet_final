import dash
from dash import html, dcc, Input, Output, State
from dash import register_page, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from triggers import query5, query6, query7

question = "Faire en sorte que les tables REGIONS et DEPARTEMENTS ne soit pas modifiables. Ajoutez un trigger qui utilise la procédure stockée précédente pour mettre à jour la population d'un département/région quand la population d'une ville est mise à jour."

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

def layout():
    return html.Div([
        html.Div(id='query-results4')  # Div pour afficher les résultats des requêtes
    ])

def display_query_results():
    results_div = html.Div([
        html.P("Faire en sorte que les tables REGIONS et DEPARTEMENTS ne soient pas modifiables. Il faut bloquer les commandes INSERT, UPDATE et DELETE :"),
        html.P(query5),
        html.P(query6),
        html.P("Ajoutez un trigger qui utilise la procédure stockée précédente pour mettre à jour la population d'un département/région quand la population d'une ville est mise à jour :"),
        html.P(query7),
    ])

    return results_div

@callback(
    Output('query-results4', 'children'),
    [Input('query-results4', 'id')]  
)
def update_query_results(trigger):
    return display_query_results()