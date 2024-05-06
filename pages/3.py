"""# Dash imports
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
from procedure import query1,pop_dep,pop_reg,query2

question = "Écrivez une procédure stockée qui fait ce calcul à partir de la population des communes. N'oubliez pas de modifier au préalable la structure de la base pour accueillir ces nouvelles informations."

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Définition du layout de votre application Dash
def layout():
    return html.Div([
        html.Div(id='query-results3')  # Div pour afficher les résultats des requêtes
    ])

def display_query_results():
    results_div = html.Div([
        html.H3("Modification des tables Departement et Region"),
        html.Pre(pop_dep),
        html.Pre(pop_reg),
        html.H3("Avec l'utilisation des vues créées :"),
        html.Pre(query1),
        html.H3("Sans l'utilisation des vues créées :"),
        html.Pre(query2)
    ])

    return results_div


@callback(
    Output('query-results3', 'children'),
    [Input('query-results3', 'id')]  
)
def update_query_results(trigger):
    return display_query_results()"""
