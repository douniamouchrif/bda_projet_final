# Importations nécessaires
import dash
from dash import html
from dash.dependencies import Output, Input, State
from triggers import query5,query6,query7

print(query7)
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