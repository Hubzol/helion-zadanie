from bs4 import BeautifulSoup

with open("helion.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

books = soup.find_all("div", class_="book-info")

titles = []
prices = []

for book in books:
    title = book.find("h2").text.strip()
    price = book.find("div", class_="price").text.strip().split()[0] 

    titles.append(title)
    prices.append(float(price.replace(",", ".")))

average_price = sum(prices) / len(prices)

for title, price in zip(titles, prices):
    if price > average_price:
        print(f"Tytuł: {title}, Cena: {price}")

with open("books_info.html", "w", encoding="utf-8") as file:
    file.write("<html><head><title>Książki</title></head><body>")
    for title, price in zip(titles, prices):
        if price > average_price:
            file.write(f"<p><strong>Tytuł:</strong> {title}, <strong>Cena:</strong> {price} zł</p>")
    file.write("</body></html>")
