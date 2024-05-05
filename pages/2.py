import dash
from dash import html, dcc, Input, Output, State
from dash import register_page, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
#from vues import df_pop_dep, df_pop_reg

question = "Créer deux vues (cf commande CREATE OR REPLACE VIEW) qui donnent la population des départements et des régions pour les différentes années ainsi que les indicateurs existants."

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

def layout () :
 html.Div([
    html.Div(id='query-results')
])
 """
def display_query_results():
    results_div = html.Div([
        html.H2("Résultats des requêtes"),
        html.P("Résultat de la requête 1: " + str(df_pop_dep.head())),
        html.P("Résultat de la requête 2: " + str(df_pop_reg.head())),
    ])
    
    return results_div

@callback(
    Output('query-results', 'children'),
    [Input('query-results', 'id')] 
)
def update_query_results(trigger):
    return display_query_results()"""