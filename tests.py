# Importations nécessaires
import dash
from dash import html
from dash.dependencies import Output, Input, State
from plan_exe import explain_results

import dash
from dash import html, dcc, Input, Output, State
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


# Créer une application Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
formatted_results = [', '.join(map(str, row)) for row in explain_results]
# Définir la mise en page
app.layout = dbc.Container([
    html.H1("Affichage des résultats de la requête SQL"),
    html.Div(id='query-results', children=[html.Pre(result) for result in formatted_results])
])




if __name__ == '__main__':
    app.run_server(debug=True)

"""
# Création de l'application Dash
app = dash.Dash(__name__)

# Layout de l'application
app.layout = html.Div([
    html.Div(id='query-results'),  # Div pour afficher les résultats des requêtes
])

def display_query_results():
    # Créer des éléments HTML pour afficher les résultats
    results_div = html.Div([
        html.H2("Résultats des requêtes"),
        html.P("Résultat de la requête 1 (Population par département) :"),
        html.Table([
            html.Tr([html.Th(col) for col in df_pop_dep.columns]),
            # Afficher uniquement les trois premières lignes
            *[html.Tr([html.Td(df_pop_dep.iloc[i][col]) for col in df_pop_dep.columns]) for i in range(3)]
        ]),
    ])
    
    return results_div


# Callback pour mettre à jour les résultats des requêtes
@app.callback(
    Output('query-results', 'children'),
    [Input('query-results', 'id')]  # Ajoutez un Input spécial pour déclencher le callback au démarrage de l'application
)
def update_query_results(trigger):
    return display_query_results()

# Point d'entrée principal de l'application
if __name__ == '__main__':
    app.run_server(debug=True)

"""