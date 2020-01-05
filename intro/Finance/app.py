import os
import logging

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
# app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# # Make sure API key is set
# if not os.environ.get("API_KEY"):
#     raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Need to show - symbol, name, shares, current price, total, cash, grand total
    # symbol - from transactions filtred by the current user loged in via user id
    # share name - from transactions matched to symbol
    # shares - from transactions counted by sum() function
    # current price - from look up via symbol for each symbol
    # total - shares * current price for each stock
    # cash = from users via userId
    # grand total = total for each stock + cash

    stock = dict()
    portfolio = list()
    userId = session['user_id']
    userInfo = db.execute("SELECT cash FROM users WHERE id = :userId", userId = userId)
    cash = int(userInfo[0]['cash'])
    grandtotal = cash
    transactInfo = db.execute("SELECT symbol, sum(shares) FROM transactions WHERE id = :userId GROUP BY symbol", userId = userId)
    for row in transactInfo:
        if row['sum(shares)'] > 0:
            stock = lookup(row['symbol'])
            stock["shares"] = row['sum(shares)']
            stock["total"] = (stock["shares"] * stock["price"])
            grandtotal += int(stock["total"])
            stock["total"] = usd(stock["total"])
            stock["price"] = usd(stock["price"])
            portfolio.append(stock)
    cash = usd(cash)
    grandtotal = usd(grandtotal)

    return render_template("index.html", portfolio = portfolio, cash = cash, grandtotal = grandtotal)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = (request.form.get("shares"))
        if not symbol:
            return apology("Please Enter Symbol", 400)
        if not shares:
            return apology("Please Enter Shares", 400)

        # validate symbol
        symbolInfo = dict()
        symbolInfo = lookup(symbol)
        if symbolInfo == None:
            return apology("INVALID SYMBOL", 400)

        # validate shares as positive number
        try:
            shares = int(shares)
        except:
            return apology("Enter Valid Shares", 400)
        if shares < 1:
            return apology("Share Must Be Greater Than Or Equal To 1", 400)

        # info to insert into transactions table
        userId = session["user_id"]
        price = symbolInfo["price"]

        # check if user can afford the stock purchase
        userInfo = db.execute("SELECT cash FROM users WHERE id = :userId", userId = userId)
        total = shares * price
        if total > userInfo[0]['cash']:
            return apology("Can't Afford", 400)

        symbol = symbolInfo["symbol"]
        #shares
        buy_sell = "B"

        # insert into table transaction
        try:
            _buy = db.execute("INSERT INTO transactions (id, price, symbol, shares, buy_sell) VALUES (:userId, :price, :symbol, :shares, :buy_sell)",
                                    userId=userId, price=price, symbol=symbol, shares=shares, buy_sell=buy_sell)
            cash = userInfo[0]['cash'] - total
            _userUpdateCash = db.execute("UPDATE users SET cash = :cash WHERE id = :userId", cash=cash, userId=userId)
        except:
            return apology("INTERNAL SERVER ERROR - 01", 500)
        flash("Bought!")
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    return jsonify("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    userId = session["user_id"]
    transactions = db.execute("SELECT symbol, shares, buy_sell, price, transacted FROM transactions WHERE id = :userId", userId = userId)
    for record in transactions:
        record["price"] = usd(record["price"])
        if record['buy_sell'] == 'S':
            record['shares'] = -record['shares']
            # logging.info(f"type(record['shares'] = {type(record['shares'])}")
            record['buy_sell'] = 'Sold'
        else:
            record['buy_sell'] = 'Bought'

    return render_template("history.html", transactions = transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("MISSING SYMBOL", 400)
        symbolInfo = dict()
        symbolInfo = lookup(symbol)
        if symbolInfo == None:
            return apology("INVALID SYMBOL", 400)
        name = symbolInfo['name']
        price = usd(symbolInfo['price'])
        symbol = symbolInfo['symbol']
        return render_template("quoted.html", name = name, price = price, symbol = symbol)
    else:
        return render_template("quote.html") # if requested via get



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Please Provide Username", 403)
        elif not password:
            return apology("Please Provide Password", 403)
        elif not confirmation:
            return apology("Please Provide Your Password Again", 403)

        if not password == confirmation:
            return apology("Passwords Do Not Match", 403)

        # checkUsername = db.execute("SELECT username FROM users WHERE username = :username", username = username)
        # if not len(checkUsername) == 0:
        #     return apology("Username Already Exists", 403)

        hashPw = generate_password_hash(password)


        newUser = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hashPw)", username=username, hashPw=hashPw)
        if not newUser:
            return apology("Username Already Exists", 403)

        # Remember which user has logged in
        # Query database for username
        try:
            rows = db.execute("SELECT * FROM users WHERE username = :username",
                              username=username)
        except:
            return apology("INTERNAL SERVER ERROR - 02", 500)
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash("You are Registered!!")
        return redirect("/")

        # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        userId = session["user_id"]
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        if not symbol:
            return apology("PLease Enter Symbol", 400)
        elif not shares:
            return apology("Please Enter Shares", 400)
        elif shares < 1:
            return apology("INVALID SHARES", 400)

        userStocks = db.execute("SELECT symbol, sum(shares) FROM transactions WHERE id = :userId GROUP BY symbol", userId = userId)

        found = False
        stockSell = dict()
        for stock in userStocks:
            if symbol == stock['symbol']:
                found = True
                stockSell['symbol'] = stock['symbol']
                stockSell['shares'] = stock['sum(shares)']

        if found == False:
            return apology("You Don't Own This Stock", 400)
        elif shares > stockSell['shares']:
            return apology("Too Many Stocks", 400)

        stockSell['price'] = (lookup(stockSell['symbol']))['price']
        buy_sell = 'S'
        _sell = db.execute("INSERT INTO transactions (id, symbol, shares, price, buy_sell) VALUES (:userId, :symbol, :shares, :price, :buy_sell)",
                            userId = userId, symbol = stockSell['symbol'], shares = -shares, price = stockSell['price'], buy_sell = buy_sell)

        userCash = db.execute("SELECT cash FROM users WHERE id = :userId", userId = userId)

        cash = userCash[0]['cash'] + (stockSell['price'] * shares)

        _userUpdate = db.execute("UPDATE users SET cash = :cash WHERE id = :userId", cash = cash, userId = userId)

        flash("SOLD!")
        return redirect("/")

    else:
        userId = session["user_id"]
        stocks = db.execute("SELECT symbol, sum(shares) FROM transactions WHERE id = :userId GROUP BY symbol HAVING sum(shares) > 0", userId = userId)

        return render_template("sell.html", stocks = stocks)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name + '-00', e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
