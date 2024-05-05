import dash
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
        html.H2("Les view"),
        html.P("View 1: " + view1),
        html.P("Résultat View 1: "+ str(df_pop_dep)),
        html.P("View 2: " + view2),
        html.P("Résultat View 1: "+ str(df_pop_reg)),
    ])
    
    return results_div

@callback(
    Output('query-results2', 'children'),
    [Input('query-results2', 'id')] 
)
def update_query_results(trigger):
    return display_query_results()