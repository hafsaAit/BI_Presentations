

import duckdb
import time
import pandas as pd




# Connexion à une base locale
con = duckdb.connect('ecommerce.duckdb')




con.execute("""
CREATE OR REPLACE VIEW transactions AS 
SELECT * FROM read_csv_auto('E-commerece_2024.csv')
""")

df_products=con.execute("""
CREATE OR REPLACE VIEW products AS 
SELECT * FROM read_csv_auto('product_details.csv')
""")

con.execute("""
CREATE OR REPLACE VIEW client AS 
SELECT * FROM read_csv_auto('customer_details.csv')
""")

#Analyse

#A – Nombre d’interactions par type
print("🔹 Interactions par type :")
df1 = con.execute("""
SELECT "Interaction type", COUNT(*) AS total
FROM transactions
GROUP BY "Interaction type"
ORDER BY total DESC
""").fetchdf()
print(df1)



# B. Top 10 des produits les plus achetés
print("\n🔹 Top 10 produits les plus achetés :")
df2 = con.execute("""
SELECT p."Product Name", COUNT(*) AS nb_ventes
FROM transactions t
JOIN products p ON t."user id" = p."Uniqe Id"
WHERE t."Interaction type" = 'Purchase'
GROUP BY p."Product Name"
ORDER BY nb_ventes DESC
LIMIT 10
""").fetchdf()
print(df2)


# C. Répartition des achats par genre
print("\n🔹 Répartition des achats par genre :")
df3 = con.execute("""
SELECT c.Gender, ROUND(AVG(c.Age), 1) AS age_moyen, COUNT(*) AS nb_achats
FROM client c
GROUP BY c.Gender
ORDER BY nb_achats DESC
""").fetchdf()
print(df3)

# D:calcule le nombre total d'achats par saison
print("\n🔹 Achats selon la saison:")
df6=con.execute("""
SELECT 
    Season, 
    COUNT(*) AS nb_achats
FROM client
GROUP BY Season
ORDER BY nb_achats DESC;
""").fetchdf()
print(df6)

# E:Revenu total par produit
print("\n🔹 Revenu total par produit:")
df7=con.execute("""
SELECT 
    c."Item Purchased", 
    SUM(c."Purchase Amount (USD)") AS total_revenu
FROM client c
GROUP BY c."Item Purchased"
ORDER BY total_revenu DESC
LIMIT 10;
""").fetchdf()
print(df7)


#Mesure de performance avec DuckDB
start = time.time()
con.execute("""
SELECT "Interaction type", COUNT(*) 
FROM transactions 
GROUP BY "Interaction type"
""").fetchall()
end = time.time()
print(f"Temps d'exécution DuckDB : {round(end - start, 4)} secondes")


#Comparaison avec Pandas
#Comparer la performance de DuckDB avec Pandas pour une opération similaire
start = time.time()
df = pd.read_csv('E-commerece_2024.csv') #Charge le fichier CSV dans un DataFrame Pandas.
df.groupby("Interaction type").size() #Effectue do le regroupement que la requête DuckDB
end = time.time()
print(f"Temps d'exécution Pandas : {round(end - start, 4)} secondes")
