import pyodbc
import pandas as pd
import matplotlib.pyplot as plt

# ======================================
# 🔗 CONEXÃO COM SQL SERVER
# ======================================

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-6LI134P;'  # seu servidor
    'DATABASE=ecommerce;'      # seu banco
    'Trusted_Connection=yes;'
)

# ======================================
# 💰 RECEITA POR MÊS
# ======================================

query = """
SELECT created_at, price_usd
FROM order_items
"""

df = pd.read_sql(query, conn)

# tratar datas
df['created_at'] = pd.to_datetime(df['created_at'])
df['mes'] = df['created_at'].dt.to_period('M')

# agrupar
receita_mes = df.groupby('mes')['price_usd'].sum()

print("\n📊 Receita por mês:")
print(receita_mes)

# gráfico
receita_mes.plot()
plt.title("Receita por mês")
plt.xlabel("Mês")
plt.ylabel("Receita")
plt.show()

# ======================================
# 🛍️ PRODUTOS MAIS VENDIDOS
# ======================================

query_prod = """
SELECT 
    p.product_name,
    COUNT(*) AS total_vendido
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_vendido DESC
"""

df_prod = pd.read_sql(query_prod, conn)

print("\n🏆 Top produtos:")
print(df_prod.head())

# gráfico
df_prod.head(10).plot(
    x='product_name',
    y='total_vendido',
    kind='bar'
)

plt.title("Top Produtos")
plt.xticks(rotation=45)
plt.show()

# ======================================
# 📊 TAXA DE CONVERSÃO
# ======================================

query_conv = """
SELECT 
    COUNT(DISTINCT o.order_id) * 1.0 /
    COUNT(DISTINCT ws.website_session_id) AS conversao
FROM website_sessions ws
LEFT JOIN orders o
    ON ws.website_session_id = o.website_session_id
"""

df_conv = pd.read_sql(query_conv, conn)

print("\n📈 Taxa de conversão:")
print(df_conv)

# ======================================
# 🔚 FINAL
# ======================================

conn.close()
