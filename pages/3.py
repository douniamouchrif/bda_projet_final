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
#from procedure import query1

question = "Écrivez une procédure stockée qui fait ce calcul à partir de la population des communes."

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

def layout () :
 html.Div([
    html.Div(id='query-results')  # Div pour afficher les résultats des requêtes
])
 
"""def display_query_results():
    # Exécuter les requêtes et obtenir les résultats ici
    # Dans cet exemple, nous affichons simplement les requêtes sans les exécuter

    # Créer des éléments HTML pour afficher les résultats
    results_div = html.Div([
        html.H2("Résultats des requêtes"),
        html.P("Résultat de la requête 1: " + str(query1)),
    
        # Ajoutez des résultats supplémentaires ici
    ])
    
    return results_div

# Callback pour mettre à jour les résultats des requêtes
@callback(
    Output('query-results', 'children'),
    [Input('query-results', 'id')]  # Ajoutez un Input spécial pour déclencher le callback au démarrage de l'application
)
def update_query_results(trigger):
    return display_query_results()"""