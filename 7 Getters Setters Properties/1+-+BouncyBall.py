class BouncyBall:

	def __init__(self, price, size, brand):
		self._price = price 
		self._size = size 
		self._brand = brand

# Using property() sintax
	def get_price(self):
		return self._price

	def set_price(self, new_price):
		if isinstance(new_price, int) and new_price > 0:
			self._id_num = new_price
		else:
			print("Please enter a valid price")
	
	def get_size(self):
		return self._size

	def set_size(self, new_size):
		if isinstance(new_size, int) and new_size>0:
			self._id_num = new_size
		else:
			print("Please enter a valid size")

	def get_brand(self):
		return self._brand

	def set_brand(self, new_brand):
		if isinstance(new_brand, str):
			self._id_num = new_brand
		else:
			print("Please enter a valid brand")
	
	price = property(get_price, set_price)
	size = property(get_size, set_size)
	brand = property(get_brand, set_brand)


# Using @property 
	@property
	def price(self):
		return self._price

	@price.setter
	def price(self, new_price):
		if isinstance(new_price, int) and new_price > 0:
			self._price = new_price
		else:
			print("Please enter a valid price")	

	@property
	def size(self):
		return self._size

	@price.setter
	def size(self, new_size):
		if isinstance(new_size, int) and new_size > 0:
			self._price = new_size
		else:
			print("Please enter a valid size")	
	
	@property
	def brand(self):
		return self._brand

	@price.setter
	def size(self, new_brand):
		if isinstance(new_brand, str):
			self._price = new_brand
		else:
			print("Please enter a valid brand")	


	