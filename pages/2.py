"""import dash
from dash import html, dcc, Input, Output, State
from dash import register_page, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from vues import view1,view2, df_pop_dep,df_pop_reg

question = "Créer deux vues (cf commande CREATE OR REPLACE VIEW) qui donnent la population des départements et des régions pour les différentes années ainsi que les indicateurs existants."

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

def layout():
    return html.Div([
        html.Div(id='query-results2')  # Div pour afficher les résultats des requêtes
    ])


def display_query_results():
    results_div = html.Div([
        html.H2("Les vues"),

        html.H3("Vue 1"),
        html.Pre(view1),
        html.Table([
            html.Thead(
                html.Tr([html.Th("num_departement"), html.Th("departement"), html.Th("id_stat"), html.Th("libelle_indicateur"), html.Th("population")])
            ),
            html.Tbody([
                html.Tr([html.Td(row[0]), html.Td(row[1]), html.Td(row[2]), html.Td(row[3]), html.Td(row[4])])
                for row in df_pop_dep.itertuples()
            ])
        ]),

        html.H3("Vue 2"),
        html.Pre(view2),
        html.Table([
            html.Thead(
                html.Tr([html.Th("num_region"), html.Th("region"), html.Th("id_stat"), html.Th("libelle_indicateur"), html.Th("population")])
            ),
            html.Tbody([
                html.Tr([html.Td(row[0]), html.Td(row[1]), html.Td(row[2]), html.Td(row[3]), html.Td(row[4])])
                for row in df_pop_reg.itertuples()
            ])
        ]),

    ])

    return results_div


@callback(
    Output('query-results2', 'children'),
    [Input('query-results2', 'id')] 
)
def update_query_results(trigger):
    return display_query_results()"""