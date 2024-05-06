# Dash imports
import dash
from dash import html, dcc, Input, Output, State
from dash import register_page, callback
from dash import ctx, no_update, ALL
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output
from plan_exe_index import query1,index_details,query2,query3,query4

# Dash extensions
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify

question = "Montrer l'intérêt des index sur plusieurs exemples. Vérifiez-le. Analyser aussi une requête qui liste les communes avec moins de 5000 habitants. Créer un index sur l'attribut population et refaites la manipulation. Vérifier que le SGBD fait les sélections individuelles avant de calculer les jointures."

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
formatted_results = [', '.join(map(str, row)) for row in index_details]
# Définition du layout de votre application Dash
def layout():
    return html.Div([
        html.Div(id='query-results7')  # Div pour afficher les résultats des requêtes
    ])

def display_query_results():
    results_div = html.Div([
        html.H2("Requête pour vérifier qu'une clé primaire est un index, sur la table région : "),
        html.Pre(query1),
        #html.Div(id='query-results7', children=[html.Pre(result) for result in formatted_results])
        html.H2("Requête qui liste les communes avec moins de 5000 habitants en 2020 sans index supplémentaire : "),
        html.Pre(query2),
        html.H2("Création de l'index + Requête précédente : "),
        html.H3("Création de l'index sur l'attribut valeur de la table Pop_Commune : "),
        html.Pre(query3),
        html.H3("Requête qui liste les communes avec moins de 5000 habitants en utilisant l'index : "),
        html.Pre(query4)
    ])

    return results_div

@callback(
    Output('query-results7', 'children'),
    [Input('query-results7', 'id')]  
)
def update_query_results(trigger):
    return display_query_results()