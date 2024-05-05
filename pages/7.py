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

question = "Montrer l'intérêt des index sur plusieurs exemples. Vérifiez-le. Analyser aussi une requête qui liste les communes avec moins de 5000 habitants. Créer un index sur l'attribut population et refaites la manipulation. Vérifier que le SGBD fait les sélections individuelles avant de calculer les jointures."

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Définition du layout de votre application Dash
def layout():
    return html.Div([
        html.Div(id='query-results7')  # Div pour afficher les résultats des requêtes
    ])

"""@callback(
    Output('query-results7', 'children'),
    [Input('query-results7', 'id')]  
)
def update_query_results(trigger):
    return display_query_results()"""