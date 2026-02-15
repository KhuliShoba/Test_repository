#!/usr/bin/env python3
# filepath: noncence2_web.py
# Minimal browser UI for Nike warehouse inventory (no external dependencies)

import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse, unquote_plus
import html

INVENTORY_FILE = "inventory.txt"

class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_value(self):
        return self.cost * self.quantity

    def to_csv(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"

class NikeWarehouse:
    def __init__(self):
        self.shoes = []

    def add_shoe(self, shoe):
        if self.search_by_code(shoe.code):
            return False
        self.shoes.append(shoe)
        return True

    def search_by_code(self, code):
        for s in self.shoes:
            if s.code.lower() == code.lower():
                return s
        return None

    def remove_shoe(self, code):
        s = self.search_by_code(code)
        if s:
            self.shoes.remove(s)
            return True
        return False

    def update_shoe(self, old_code, new_shoe):
        s = self.search_by_code(old_code)
        if not s:
            return False
        # ensure new code not used by different shoe
        if new_shoe.code.lower() != old_code.lower() and self.search_by_code(new_shoe.code):
            return False
        s.country = new_shoe.country
        s.code = new_shoe.code
        s.product = new_shoe.product
        s.cost = new_shoe.cost
        s.quantity = new_shoe.quantity
        return True

    def lowest_quantity_shoe(self):
        return min(self.shoes, key=lambda s: s.quantity) if self.shoes else None

    def highest_quantity_shoe(self):
        return max(self.shoes, key=lambda s: s.quantity) if self.shoes else None

    def total_value_all(self):
        return sum(s.get_value() for s in self.shoes)

    def load_from_file(self, fname=INVENTORY_FILE):
        self.shoes.clear()
        if not os.path.exists(fname):
            return
        with open(fname, 'r', encoding='utf-8') as f:
            next(f, None)  # skip header
            for line in f:
                if not line.strip():
                    continue
                parts = [p.strip() for p in line.strip().split(',')]
                if len(parts) != 5:
                    continue
                try:
                    s = Shoe(parts[0], parts[1], parts[2], float(parts[3]), int(parts[4]))
                    if not self.search_by_code(s.code):
                        self.shoes.append(s)
                except ValueError:
                    continue

    def save_to_file(self, fname=INVENTORY_FILE):
        with open(fname, 'w', encoding='utf-8') as f:
            f.write("Country,Code,Product,Cost,Quantity\n")
            for s in self.shoes:
                f.write(s.to_csv() + "\n")

    def html_table(self):
        if not self.shoes:
            return "<p>No shoes in inventory.</p>"
        rows = []
        rows.append("<tr><th>Country</th><th>Code</th><th>Product</th><th>Cost</th><th>Qty</th><th>Value</th></tr>")
        for s in self.shoes:
            rows.append("<tr>" +
                        f"<td>{html.escape(s.country)}</td>" +
                        f"<td>{html.escape(s.code)}</td>" +
                        f"<td>{html.escape(s.product)}</td>" +
                        f"<td>R{ s.cost:.2f }</td>" +
                        f"<td>{ s.quantity }</td>" +
                        f"<td>R{ s.get_value():.2f }</td>" +
                        "</tr>")
        return "<table border='1' cellpadding='4'>" + "\n".join(rows) + "</table>"

warehouse = NikeWarehouse()
warehouse.load_from_file()

INDEX_HTML = """<!doctype html>
<html><head><meta charset="utf-8"><title>Nike Warehouse Manager</title>
<style>
body{font-family:Arial,Helvetica,sans-serif;margin:12px}
.container{display:flex;gap:24px}
.left{flex:1}
.right{width:320px}
input,select{width:100%}
table{border-collapse:collapse}
th{background:#eee}
.notice{padding:6px;background:#f5f5f5;border:1px solid #ddd;margin:8px 0}
</style>
</head><body>
<h1>Nike Warehouse Manager</h1>
<div class="container">
<div class="left">
<h2>Inventory</h2>
{table}
<form method="get" action="/refresh"><button type="submit">Refresh</button></form>
</div>
<div class="right">
<h2>Quick actions</h2>
<div class="notice">
<form method="post" action="/add">
<p><b>Add new shoe</b></p>
<label>Country<br><input name="country"></label><br>
<label>Code<br><input name="code"></label><br>
<label>Product<br><input name="product"></label><br>
<label>Cost<br><input name="cost"></label><br>
<label>Quantity<br><input name="quantity"></label><br>
<button type="submit">Add Shoe</button>
</form>
</div>

<div class="notice">
<form method="get" action="/search">
<p><b>Search by code</b></p>
<label>Code<br><input name="code"></label><br>
<button type="submit">Search</button>
</form>
</div>

<div class="notice">
<form method="post" action="/delete">
<p><b>Delete by code</b></p>
<label>Code<br><input name="code"></label><br>
<button type="submit">Delete</button>
</form>
</div>

<div class="notice">
<form method="get" action="/extremes">
<p><b>Lowest / Highest quantity</b></p>
<button name="which" value="low" type="submit">Lowest</button>
<button name="which" value="high" type="submit">Highest</button>
</form>
</div>

<div class="notice">
<form method="get" action="/total">
<p><b>Total inventory value</b></p>
<button type="submit">Calculate</button>
</form>
</div>

<div class="notice">
<form method="post" action="/save">
<button type="submit">Save to inventory.txt</button>
</form>
</div>

</div>
</div>
<hr>
<small>Runs on Python built‑in HTTP server. Data loaded/saved to inventory.txt</small>
</body></html>
"""

class Handler(BaseHTTPRequestHandler):
    def send_html(self, html_body, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html_body.encode('utf-8'))

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        qs = parse_qs(parsed.query)
        if path in ("/", "/index.html", "/refresh"):
            body = INDEX_HTML.format(table=warehouse.html_table())
            self.send_html(body)
        elif path == "/search":
            code = qs.get("code", [""])[0].strip()
            if not code:
                self.send_html("<p>Missing code. <a href='/'>Back</a></p>")
                return
            s = warehouse.search_by_code(code)
            if not s:
                self.send_html(f"<p>Product '{html.escape(code)}' not found. <a href='/'>Back</a></p>")
            else:
                out = "<h2>Search result</h2>"
                out += "<p>" + html.escape(str(s)) + "</p>"
                out += "<p><a href='/edit?code=%s'>Edit this item</a></p>" % html.escape(s.code)
                out += "<p><a href='/'>Back</a></p>"
                self.send_html(out)
        elif path == "/edit":
            code = qs.get("code", [""])[0].strip()
            s = warehouse.search_by_code(code)
            if not s:
                self.send_html(f"<p>Product '{html.escape(code)}' not found. <a href='/'>Back</a></p>")
                return
            form = f"""
            <h2>Edit {html.escape(s.code)}</h2>
            <form method='post' action='/edit'>
            <input type='hidden' name='old_code' value='{html.escape(s.code)}'>
            <label>Country<br><input name='country' value='{html.escape(s.country)}'></label><br>
            <label>Code<br><input name='code' value='{html.escape(s.code)}'></label><br>
            <label>Product<br><input name='product' value='{html.escape(s.product)}'></label><br>
            <label>Cost<br><input name='cost' value='{s.cost}'></label><br>
            <label>Quantity<br><input name='quantity' value='{s.quantity}'></label><br>
            <button type='submit'>Update</button>
            </form>
            <p><a href='/'>Back</a></p>
            """
            self.send_html(form)
        elif path == "/extremes":
            which = qs.get("which", ["low"])[0]
            if which == "high":
                s = warehouse.highest_quantity_shoe()
                label = "Highest quantity"
            else:
                s = warehouse.lowest_quantity_shoe()
                label = "Lowest quantity"
            if not s:
                self.send_html(f"<p>No inventory. <a href='/'>Back</a></p>")
            else:
                self.send_html(f"<h2>{label}</h2><p>{html.escape(str(s))}</p><p><a href='/'>Back</a></p>")
        elif path == "/total":
            total = warehouse.total_value_all()
            self.send_html(f"<h2>Total inventory value</h2><p>R{total:.2f}</p><p><a href='/'>Back</a></p>")
        else:
            self.send_html("<p>Not found. <a href='/'>Back</a></p>", 404)

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(length).decode('utf-8')
        form = parse_qs(data)
        # helper to safely fetch single value
        fv = lambda k: unquote_plus(form.get(k, [""])[0]).strip()
        if path == "/add":
            try:
                country = fv('country')
                code = fv('code')
                product = fv('product')
                cost = float(fv('cost'))
                quantity = int(fv('quantity'))
                if not country or not code or not product:
                    raise ValueError("Country, Code, Product required.")
                if cost < 0 or quantity < 0:
                    raise ValueError("Cost/Quantity must be non-negative.")
                s = Shoe(country, code, product, cost, quantity)
                if not warehouse.add_shoe(s):
                    self.send_html(f"<p>Code {html.escape(code)} already exists. <a href='/'>Back</a></p>")
                    return
                self.send_html(f"<p>Added {html.escape(code)}. <a href='/'>Back</a></p>")
            except ValueError as e:
                self.send_html(f"<p>Error: {html.escape(str(e))}. <a href='/'>Back</a></p>")
        elif path == "/delete":
            code = fv('code')
            if not code:
                self.send_html("<p>Missing code. <a href='/'>Back</a></p>")
                return
            if warehouse.remove_shoe(code):
                self.send_html(f"<p>Deleted {html.escape(code)}. <a href='/'>Back</a></p>")
            else:
                self.send_html(f"<p>Not found: {html.escape(code)}. <a href='/'>Back</a></p>")
        elif path == "/edit":
            old_code = fv('old_code')
            try:
                country = fv('country')
                code = fv('code')
                product = fv('product')
                cost = float(fv('cost'))
                quantity = int(fv('quantity'))
                if not country or not code or not product:
                    raise ValueError("Country, Code, Product required.")
                new_shoe = Shoe(country, code, product, cost, quantity)
                ok = warehouse.update_shoe(old_code, new_shoe)
                if not ok:
                    self.send_html(f"<p>Update failed (code conflict or missing). <a href='/'>Back</a></p>")
                    return
                self.send_html(f"<p>Updated {html.escape(code)}. <a href='/'>Back</a></p>")
            except ValueError as e:
                self.send_html(f"<p>Error: {html.escape(str(e))}. <a href='/'>Back</a></p>")
        elif path == "/save":
            warehouse.save_to_file()
            self.send_html("<p>Saved to inventory.txt. <a href='/'>Back</a></p>")
        else:
            self.send_html("<p>Unknown POST target. <a href='/'>Back</a></p>", 404)

def run(server_class=HTTPServer, handler_class=Handler, port=8000):
    server_address = ('', port)
    print(f"Starting server at http://localhost:{port} ...")
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down...")
        httpd.server_close()

if __name__ == "__main__":
    run()