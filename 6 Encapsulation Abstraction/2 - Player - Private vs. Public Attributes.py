class Player:
	def __init__(self, username, rank, time_played, id_num):
		self.username = username
		self._rank = rank
		self.__time_played = time_played
		self.__id_num = id_num

player = Player('mario56', 1536, 580, "545454")

print(player._rank) # maneira recomendada

print(player._Player__time_played) # maneira de deixar mais difícil o acesso, mas não torna o atributito privado,
