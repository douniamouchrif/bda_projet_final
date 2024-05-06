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

def display_query_results():
    results_div = html.Div([
        html.H2("Résultats des requêtes"),

        html.H3("Requête 1 : liste des départements d'une région donnée"),
        html.Pre(query_1),
        html.Table([
            html.Thead(
                html.Tr([html.Th("num_dep"), html.Th("nom_dep"), html.Th("chef_lieu")])
            ),
            html.Tbody([
                html.Tr([html.Td(row[0]), html.Td(row[1]), html.Td(row[2])])
                for row in results_1
            ])
        ]),

        html.H3("Requête 2 : liste des communes de plus de X habitants d'un département donné en 2020"),
        html.Pre(query_2),
        html.Table([
            html.Thead(
                html.Tr([html.Th("num_com"), html.Th("nom_com"), html.Th("population")])
            ),
            html.Tbody([
                html.Tr([html.Td(row[0]), html.Td(row[1]), html.Td(row[2])])
                for row in results_2
            ])
        ]),

        html.H3("Requête 3 : la région la plus peuplée"),
        html.Pre(query_3),
        html.Table([
            html.Thead(
                html.Tr([html.Th("nom_reg"), html.Th("population_totale")])
            ),
            html.Tbody([
                html.Tr([html.Td(result_3[0]), html.Td(result_3[1])])
            ])
        ]),

        html.H3("Requête 4 : la région la moins peuplée"),
        html.Pre(query_4),
        html.Table([
            html.Thead(
                html.Tr([html.Th("nom_reg"), html.Th("population_totale")])
            ),
            html.Tbody([
                html.Tr([html.Td(result_4[0]), html.Td(result_4[1])])
            ])
        ]),

        html.H3("Requête 5 : les 10 communes les plus peuplées d'un département en 2020"),
        html.Pre(query_5),
        html.Table([
            html.Thead(
                html.Tr([html.Th("nom_com"), html.Th("population")])
            ),
            html.Tbody([
                html.Tr([html.Td(row[0]), html.Td(row[1])])
                for row in results_5
            ])
        ]),

        html.H3("Requête 6 : les 10 communes les moins peuplées d'un département en 2020"),
        html.Pre(query_6),
        html.Table([
            html.Thead(
                html.Tr([html.Th("nom_com"), html.Th("population")])
            ),
            html.Tbody([
                html.Tr([html.Td(row[0]), html.Td(row[1])])
                for row in results_6
            ])
        ]),

        html.H3("Requête 7 : le nombre total de mariages pour la 1ère fois par type de couple dans le département spécifié"),
        html.Pre(query_7),
        html.Table([
            html.Thead(
                html.Tr([html.Th("type_couple"), html.Th("total_mariages")])
            ),
            html.Tbody([
                html.Tr([html.Td(row[0]), html.Td(row[1])])
                for row in results_7
            ])
        ]),

    ])

    return results_div


@callback(
    Output('query-results', 'children'),
    [Input('query-results', 'id')]  
)
def update_query_results(trigger):
    return display_query_results()


