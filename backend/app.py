from flask import Flask, jsonify, request
from database.db_connect import get_db_connection

app = Flask(__name__)

@app.route('/api/products/<website>')
def get_products(website):
    category = request.args.get('category')
    conn = get_db_connection()
    cursor = conn.cursor()

    if category:
        query = """
            SELECT product_id, product_name, brand_name, price, rating_or_reviews, website_name, category
            FROM {}
            WHERE category = %s
        """.format(website)
        cursor.execute(query, (category,))
    else:
        query = """
            SELECT product_id, product_name, brand_name, price, rating_or_reviews, website_name, category
            FROM {}
        """.format(website)
        cursor.execute(query)

    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    products = []
    for row in rows:
        products.append({
            'product_id': row[0],
            'product_name': row[1],
            'brand_name': row[2],
            'price': row[3],
            'rating_or_reviews': row[4],
            'website_name': row[5],
            'category': row[6]
        })

    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
