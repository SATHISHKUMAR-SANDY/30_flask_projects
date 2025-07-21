from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy in-memory data
expenses = []

@app.route('/')
def index():
    category_filter = request.args.get('category')
    if category_filter:
        filtered_expenses = [e for e in expenses if e['category'] == category_filter]
    else:
        filtered_expenses = expenses
    return render_template('index.html', expenses=filtered_expenses, category=category_filter)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        title = request.form['title']
        amount = float(request.form['amount'])
        category = request.form['category']
        expense_id = len(expenses)
        expenses.append({'id': expense_id, 'title': title, 'amount': amount, 'category': category})
        return redirect(url_for('index'))
    return render_template('add_expense.html')

@app.route('/expense/<int:expense_id>')
def expense_detail(expense_id):
    if 0 <= expense_id < len(expenses):
        expense = expenses[expense_id]
        return render_template('expense_detail.html', expense=expense)
    return "Expense not found", 404

if __name__ == '__main__':
    app.run(debug=True,port=9002)
