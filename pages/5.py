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


question = "Automatisez au maximum les calculs de population quand une nouvelle année de recensement est ajoutée au niveau des communes. Factorisez au maximum le code avec des procédures stockées."

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Définition du layout de votre application Dash
def layout():
    return html.Div([
        html.Div(id='query-results5')  # Div pour afficher les résultats des requêtes
    ])

"""@callback(
    Output('query-results5', 'children'),
    [Input('query-results5', 'id')]  
)
def update_query_results(trigger):
    return display_query_results()"""