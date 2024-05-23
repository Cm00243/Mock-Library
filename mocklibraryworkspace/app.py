from flask import Flask, jsonify, render_template
import csv

app = Flask(__name__)

def read_csv(file_path='books.csv'):
    books = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            books.append({
                "title": row['title'],
                "author": row['author'],
                "publisher": row['publisher'],
                "publishing_date": row['publishing_date']
            })
    return books

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books')
def books_page():
    books = read_csv()
    return render_template('books.html', books=books)

@app.route('/api/books')
def get_books():
    books = read_csv()
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)