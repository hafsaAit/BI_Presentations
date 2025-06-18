# 🦆 DuckDB : Base de Données Analytique Embarquée

**DuckDB** est un SGBD analytique en mémoire sans serveur pour l'analyse de données rapide et efficace.

---

## 📌 Objectifs
* **Simplifier l'analyse locale** : Analyses SQL sur fichiers CSV/Parquet sans infrastructure
* **Démocratiser l'analyse haute performance** : Traitement téraoctets sur machine standard
* **Intégration native** : Compatible Python/R avec formats modernes

## 🛠️ Prérequis
- SQL (niveau intermédiaire)
- Python ou R
- Notions CSV/Parquet/JSON

## 🚀 Installation & Setup

### Installation
```bash
pip install duckdb pandas
```

### Configuration (main.py)
```python
import duckdb
conn = duckdb.connect('demo_database.duckdb')

# Chargement des données
conn.execute("CREATE TABLE customers AS SELECT * FROM read_csv_auto('Data/customer_details.csv')")
conn.execute("CREATE TABLE ecommerce AS SELECT * FROM read_csv_auto('Data/E-commerce_2024.csv')")
conn.execute("CREATE TABLE products AS SELECT * FROM read_csv_auto('Data/product_details.csv')")
```

## 📊 Analyses E-commerce

### Segmentation Client RFM
```sql
WITH customer_metrics AS (
    SELECT 
        c.customer_name,
        DATEDIFF('day', MAX(e.order_date), CURRENT_DATE) as recency,
        COUNT(DISTINCT e.order_id) as frequency,
        SUM(e.quantity * e.price) as monetary
    FROM customers c
    JOIN ecommerce e ON c.customer_id = e.customer_id
    GROUP BY c.customer_id, c.customer_name
)
SELECT 
    customer_name,
    CASE 
        WHEN recency <= 30 AND frequency >= 5 AND monetary >= 1000 THEN 'Champions'
        WHEN recency <= 60 AND frequency >= 3 THEN 'Loyal'
        WHEN recency > 180 THEN 'At Risk'
        ELSE 'Regular'
    END as segment
FROM customer_metrics;
```

### Performance par Catégorie
```sql
SELECT 
    p.category,
    COUNT(*) as orders,
    ROUND(SUM(e.quantity * e.price), 2) as revenue,
    ROUND(AVG(e.quantity * e.price), 2) as avg_order
FROM ecommerce e
JOIN products p ON e.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;
```

## 🔍 Script Principal
```python
def analyze_data():
    conn = duckdb.connect('demo_database.duckdb')
    
    # Top clients
    top_customers = conn.execute("""
        SELECT c.customer_name, SUM(e.quantity * e.price) as total
        FROM customers c JOIN ecommerce e ON c.customer_id = e.customer_id
        GROUP BY c.customer_name ORDER BY total DESC LIMIT 10
    """).fetchdf()
    
    return top_customers
```

## 📁 Structure Projet
- `slides/DruckDB.pdf` - Présentation
- `Demo/main.py` - Script démonstration
- `Data/` - Fichiers CSV (customers, ecommerce, products)

## 🚀 Avantages
- **Performance** : 100x plus rapide que Pandas
- **Simplicité** : Pas de serveur requis
- **Compatibilité** : Python/R natif

## 👥 Auteur(s)
- **Nom** : Essafi Amina & Ouzziki Dounya
- **Encadrant** : Pr. Najdi Lotfi
- **Promotion** : Master Big Data & IA – 2024/2026