from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/products')
def products():
    return render_template('products.html')

if __name__ == "__main__":
    app.run()
