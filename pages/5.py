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
from requests import query_1, query_2, query_3, query_4, query_5, query_6, query_7
from requests import results_1, results_2, result_3, result_4, results_5, results_6, results_7

question = "Automatisez au maximum les calculs de population quand une nouvelle année de recensement est ajoutée au niveau des communes. Factorisez au maximum le code avec des procédures stockées. "

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

def layout () :
 html.Div([
    html.Div(id='query-results')  # Div pour afficher les résultats des requêtes
])
 
def display_query_results():
    # Exécuter les requêtes et obtenir les résultats ici
    # Dans cet exemple, nous affichons simplement les requêtes sans les exécuter

    # Créer des éléments HTML pour afficher les résultats
    results_div = html.Div([
        html.H2("Résultats des requêtes"),
        html.P("Résultat de la requête 1: " + str(query_1)),
        html.P("Résultat de la requête 2: " + str(query_2)),
        html.P("Résultat de la requête 3: " + str(query_3)),
        html.P("Résultat de la requête 4: " + str(query_4)),
        html.P("Résultat de la requête 5: " + str(query_5)),
        html.P("Résultat de la requête 6: " + str(query_6)),
        html.P("Résultat de la requête 7: " + str(query_7)),
        # Ajoutez des résultats supplémentaires ici
    ])
    
    return results_div
"""
# Callback pour mettre à jour les résultats des requêtes
@callback(
    Output('query-results', 'children'),
    [Input('query-results', 'id')]  # Ajoutez un Input spécial pour déclencher le callback au démarrage de l'application
)
def update_query_results(trigger):
    return display_query_results()"""