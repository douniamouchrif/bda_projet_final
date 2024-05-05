# Importations nécessaires
import dash
import dash_html_components as html
from dash.dependencies import Output, Input, State
from requests import results_1, query_2, query_3, query_4, query_5, query_6, query_7

# Création de l'application Dash
app = dash.Dash(__name__)

# Layout de l'application
app.layout = html.Div([
    html.Div(id='query-results'),  # Div pour afficher les résultats des requêtes
])

# Fonction pour afficher les résultats des requêtes
def display_query_results():
    # Exécuter les requêtes et obtenir les résultats ici
    # Dans cet exemple, nous affichons simplement les requêtes sans les exécuter

    # Créer des éléments HTML pour afficher les résultats
    results_div = html.Div([
        html.H2("Résultats des requêtes"),
        html.P("Résultat de la requête 1: " + str(results_1)),
        html.P("Résultat de la requête 2: " + query_2),
        html.P("Résultat de la requête 1: " + query_3),
        html.P("Résultat de la requête 1: " + query_4),
        html.P("Résultat de la requête 1: " + query_5),
        html.P("Résultat de la requête 1: " + query_6),
        html.P("Résultat de la requête 1: " + query_7)
        # Ajoutez des résultats supplémentaires ici
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

