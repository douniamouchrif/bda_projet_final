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
from plan_exe import explain_results_1,nom_region,exe_query1,num_dep,seuil_population,exe_query2,explain_results_2,exe_query3,explain_results_3,exe_query4,explain_results_4,exe_query5,explain_results_5,exe_query6,explain_results_6,code_departement,exe_query7,explain_results_7

question = "Comparer et expliquer le coût d'exécution de différentes requêtes. Faites apparaître les différents algorithmes de jointure ou différentes stratégies de tri en jouant en particulier sur la cardinalité des relations."

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Définition du layout de votre application Dash
def layout():
    return html.Div([
        html.Div(id='query-results6')  # Div pour afficher les résultats des requêtes
    ])

formatted_results = [', '.join(map(str, row)) for row in explain_results_1]
formatted_results_2 = [', '.join(map(str, row)) for row in explain_results_2]
formatted_results_3 = [', '.join(map(str, row)) for row in explain_results_3]
formatted_results_4 = [', '.join(map(str, row)) for row in explain_results_4]
formatted_results_5 = [', '.join(map(str, row)) for row in explain_results_5]
formatted_results_6 = [', '.join(map(str, row)) for row in explain_results_6]
formatted_results_7 = [', '.join(map(str, row)) for row in explain_results_7]

text_with_line_breaks = "Utilisation d'une jointure entre Departement et Region basée sur num_reg." \
                         "Filtre sur nom_reg = 'Nouvelle-Aquitaine'." \
                         "Exécution efficace avec un coût faible (cost=0.16..18.63) et un temps d'exécution rapide (Execution Time: 0.163 ms)."
def display_query_results():
    results_div = html.Div([
        html.H2("Plan d'exécution de la 1ère requête : "),
        html.P("Nom de la région sélectionnée : "),
        html.Pre(nom_region),
        html.Pre(exe_query1),
        html.Div(id='query-results6', children=[html.Pre(result) for result in formatted_results]),
        html.P("Analyse : "),
        html.P(html.Span(text_with_line_breaks, style={"white-space": "pre-line"})),
        html.H2("Plan d'exécution de la 2ème requête : "),
        html.P("Carastéristiques de la requête: "),
        html.Pre(num_dep),
        html.Pre(seuil_population),
        html.Pre(exe_query2),
        html.Pre(exe_query2),
        html.Div(id='query-results6', children=[html.Pre(result) for result in formatted_results_2]),
        html.H2("Plan d'exécution de la 3ème requête : "),
        html.Pre(exe_query3),
        html.Div(id='query-results6', children=[html.Pre(result) for result in formatted_results_3]),
        html.H2("Plan d'exécution de la 4ème requête : "),
        html.Pre(exe_query4),
        html.Div(id='query-results6', children=[html.Pre(result) for result in formatted_results_4]),
        html.H2("Plan d'exécution de la 5ème requête : "),
        html.Pre(exe_query5),
        html.Div(id='query-results6', children=[html.Pre(result) for result in formatted_results_5]),
        html.H2("Plan d'exécution de la 6ème requête : "),
        html.Pre(exe_query6),
        html.Div(id='query-results6', children=[html.Pre(result) for result in formatted_results_6]),
        html.H2("Plan d'exécution de la 7ème requête : "),
        html.Pre(code_departement),
        html.Pre(exe_query7),
        html.Div(id='query-results6', children=[html.Pre(result) for result in formatted_results_7]),
        html.H4("Analyse de la requête 7 :"),
        html.P([
            "- Agrégation par type_couple avec SUM(nb_mar) pour obtenir le total de mariages par type de couple dans un département spécifique.",
            "- Filtre sur dep = '1177' et id_stat = 'MAR21AGE_2'.",
            "- Exécution rapide (Execution Time: 0.514 ms)."
        ]),
        html.H4("Analyse générale :"),
        html.P([
            "- Toutes les requêtes ont des jointures entre au moins deux tables, parfois plus. Ces jointures peuvent être un point critique pour les performances.",
            "- Chaque requête comporte des 'WHERE' qui filtrent les données en fonction de certaines conditions.",
            "- Plusieurs requêtes utilisent des fonctions d'agrégation comme SUM pour calculer des effectifs totaux.",
            "- Certaines requêtes ont un tri des résultats, soit pour présenter les données (ORDER BY), soit pour limiter le nombre de résultats (LIMIT).",
            html.Hr(),
            "Pour conclure, les requêtes ont des schémas d'accès aux données similaires mais avec des besoins de traitement différents selon ceux rappelés ci-dessus. Une attention aux détails d'indexation, d'optimisation des requêtes ou encore des performances, contribuera à améliorer les performances de notre système de base de données."
        ]),

       ])

    return results_div

@callback(
    Output('query-results6', 'children'),
    [Input('query-results6', 'id')]  
)
def update_query_results(trigger):
    return display_query_results()