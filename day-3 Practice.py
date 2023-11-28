# import requests
# from bs4 import BeautifulSoup




# # class Itti_Scraper:

# #     def __init__(self)
# #         self.url="https://itti-website-nine.vercel.app/laptops-by-brands/lenovo-laptops-nepal/legion"

# #     def scrape_laptops()
    
        
# url="https://merolagani.com/StockQuote.aspx"
# r= requests.get(url)
# source_code = r.text

# soup = BeautifulSoup(source_code)


# listing_div = soup.findAll("div", {
# 	"class": "table-responsive"})

# for listing in listing_div:
# 	print(listing.text.strip())


#calculator
class Calculator:

	def add(self, a, b):
		return a + b

	def subtract(self, a, b):
		return a - b

	def multiply(self, a, b):
		return a * b

	def division(self,a, b):
		try:
			return a / b
		except:
			return "Division by Zero Error"

while True:
	a = float(input("Enter first number \n "))
	b = float(input("Enter second number \n"))
	op = input("Enter operator \n")

	c = Calculator()
	#print(a, b, op)
	if op == '*':
		result = c.multiply(a, b)
	elif op == '/':
		result = c.division(a, b)
	elif op == '+':
		result = c.add(a, b)
	elif op == '-':
		result = c.subtract(a, b)

	print("Result :: ", result)


