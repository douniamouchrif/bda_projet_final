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

question = "Dans un programme réalisé dans le langage de votre choix (de préférence C, C++, Java ou Python), réalisez au moins trois requêtes."

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Définition du layout de votre application Dash
def layout():
    return html.Div([
        html.Div(id='query-results')  # Div pour afficher les résultats des requêtes
    ])

# Définition de la fonction pour afficher les résultats des requêtes
def display_query_results():
    results_div = html.Div([
        html.H2("Résultats des requêtes"),
        html.P("Requête 1 : liste des départements d'une région donnée : " + str(query_1)),
        html.P("Résultat de la requête 1 : " + str(results_1)),
        html.P("Requête 2 : liste des communes de plus de X habitants d'un département donné en 2020 : " + str(query_2)),
        html.P("Résultat de la requête 2 : " + str(results_2)),
        html.P("Requête 3 : la région la plus peuplée : " + str(query_3)),
        html.P("Résultat de la requête 3 : " + str(result_3)),
        html.P("Requête 4 : la région la moins peuplée : " + str(query_4)),
        html.P("Résultat de la requête 4 : " + str(result_4)),
        html.P("Requête 5 : les 10 communes les plus peuplées d'un département en 2020 : " + str(query_5)),
        html.P("Résultat de la requête 5 : " + str(results_5)),
        html.P("Requête 6 : les 10 communes les moins peuplées d'un département en 2020 : " + str(query_6)),
        html.P("Résultat de la requête 6 : " + str(results_6)),
        html.P("Requête 7 : le nombre total de mariages pour la 1ère fois par type de couple dans le département spécifié : " + str(query_7)),
        html.P("Résultat de la requête 7 : " + str(results_7)),
    ])

    return results_div

@callback(
    Output('query-results', 'children'),
    [Input('query-results', 'id')]  
)
def update_query_results(trigger):
    return display_query_results()


