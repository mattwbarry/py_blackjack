from random import shuffle

y = 'y'
n = 'n'

class Blackjack():

	def __init__(self, players=4):
		self.deck = [
			{ 'number': '2', 'suit': 'hearts', 'value': 2 },
			{ 'number': '3', 'suit': 'hearts', 'value': 3 },
			{ 'number': '4', 'suit': 'hearts', 'value': 4 },
			{ 'number': '5', 'suit': 'hearts', 'value': 5 },
			{ 'number': '6', 'suit': 'hearts', 'value': 6 },
			{ 'number': '7', 'suit': 'hearts', 'value': 7 },
			{ 'number': '8', 'suit': 'hearts', 'value': 8 },
			{ 'number': '9', 'suit': 'hearts', 'value': 9 },
			{ 'number': '10', 'suit': 'hearts', 'value': 10 },
			{ 'number': 'jack', 'suit': 'hearts', 'value': 10 },
			{ 'number': 'queen', 'suit': 'hearts', 'value': 10 },
			{ 'number': 'king', 'suit': 'hearts', 'value': 10 },
			{ 'number': 'ace', 'suit': 'hearts', 'value': 1 },
			{ 'number': '2', 'suit': 'diamonds', 'value': 2 },
			{ 'number': '3', 'suit': 'diamonds', 'value': 3 },
			{ 'number': '4', 'suit': 'diamonds', 'value': 4 },
			{ 'number': '5', 'suit': 'diamonds', 'value': 5 },
			{ 'number': '6', 'suit': 'diamonds', 'value': 6 },
			{ 'number': '7', 'suit': 'diamonds', 'value': 7 },
			{ 'number': '8', 'suit': 'diamonds', 'value': 8 },
			{ 'number': '9', 'suit': 'diamonds', 'value': 9 },
			{ 'number': '10', 'suit': 'diamonds', 'value': 10 },
			{ 'number': 'jack', 'suit': 'diamonds', 'value': 10 },
			{ 'number': 'queen', 'suit': 'diamonds', 'value': 10 },
			{ 'number': 'king', 'suit': 'diamonds', 'value': 10 },
			{ 'number': 'ace', 'suit': 'diamonds', 'value': 1 },
			{ 'number': '2', 'suit': 'clubs', 'value': 2 },
			{ 'number': '3', 'suit': 'clubs', 'value': 3 },
			{ 'number': '4', 'suit': 'clubs', 'value': 4 },
			{ 'number': '5', 'suit': 'clubs', 'value': 5 },
			{ 'number': '6', 'suit': 'clubs', 'value': 6 },
			{ 'number': '7', 'suit': 'clubs', 'value': 7 },
			{ 'number': '8', 'suit': 'clubs', 'value': 8 },
			{ 'number': '9', 'suit': 'clubs', 'value': 9 },
			{ 'number': '10', 'suit': 'clubs', 'value': 10 },
			{ 'number': 'jack', 'suit': 'clubs', 'value': 10 },
			{ 'number': 'queen', 'suit': 'clubs', 'value': 10 },
			{ 'number': 'king', 'suit': 'clubs', 'value': 10 },
			{ 'number': 'ace', 'suit': 'clubs', 'value': 1 },
			{ 'number': '2', 'suit': 'spades', 'value': 2 },
			{ 'number': '3', 'suit': 'spades', 'value': 3 },
			{ 'number': '4', 'suit': 'spades', 'value': 4 },
			{ 'number': '5', 'suit': 'spades', 'value': 5 },
			{ 'number': '6', 'suit': 'spades', 'value': 6 },
			{ 'number': '7', 'suit': 'spades', 'value': 7 },
			{ 'number': '8', 'suit': 'spades', 'value': 8 },
			{ 'number': '9', 'suit': 'spades', 'value': 9 },
			{ 'number': '10', 'suit': 'spades', 'value': 10 },
			{ 'number': 'jack', 'suit': 'spades', 'value': 10 },
			{ 'number': 'queen', 'suit': 'spades', 'value': 10 },
			{ 'number': 'king', 'suit': 'spades', 'value': 10 },
			{ 'number': 'ace', 'suit': 'spades', 'value': 1 },
		]

		shuffle(self.deck)

		# generate players
		self.players = []
		for player_id in range(players):
			self.players.append(Player(player_id))

		# deal hand to each player and start the game
		self.deal()



	def deal(self):
		for player in self.players:
			player.hand['face-down'].append(self.deck.pop())
			player.hand['face-up'].append(self.deck.pop())
			# check for auto winner
			if player.check_win_lose() == 1:
				return player.add_points(), player.id
		
		return self.play()

	def play(self):
		max_val = 0
		winner = None
		# while list of players has not been exhausted
		for player in self.players:
			# keep asking for hits until denial
			hit = self.ask_hit(player)
			while hit == 'y':
				self.deal_single(player)
				# check if won or lost
				victory = player.check_win_lose()
				if victory == 0:
					hit = 'n'
					print 'you lose. your points add to ' + str(player.add_points())
				elif victory == 1:
					hit = 'n'
					return self.check_for_winner()
				else:
					hit = self.ask_hit(player)
		# return player with the highest score
		return self.check_for_winner()

	def ask_hit(self, player):
		print '----------------------------------------------------'
		print 'player id ' + str(player.id)
		print 'your cards are: ' + player.view_own_cards()
		print 'your points are: ' + str(player.add_points())
		hit = input('take a hit? (y/n)')
		return hit

	def deal_single(self, player):
		player.hand['face-up'].append(self.deck.pop())
		print 'you were dealt a ' + player.hand['face-up'][-1]['number'] + ' of ' + player.hand['face-up'][-1]['suit']

	def check_for_winner(self):
		max_val = 0
		winner = None
		for player in self.players:
			points = player.add_points()
			if 21 in points:
				return 21, player.id
			else:
				for point in points:
					if point > max_val and point <= 21:
						max_val = point
						winner = player
		if max_val == 0:
			return False
		print 'winner is ' + str(winner.id) + ' with ' + str(max_val) + ' points!'
		return max_val, winner.id

class Player():

	def __init__(self, id=0):
		self.id = id
		self.hand = {'face-down': [], 'face-up': []}

	def add_points(self):
		cards = self.hand['face-down'] + self.hand['face-up']
		aces = 0
		total = 0
		totals = []

		for card in cards:
			if card['value'] == 1:
				aces += 1

			total += card['value']

		totals.append(total)

		for ace in range(aces):
			total += 10
			totals.append(total)

		# return list of possible totals
		return totals

	def check_win_lose(self):
		points = self.add_points()
		if min(points) > 21:
			# player loses
			return 0
		elif 21 in points:
			# player wins
			return 1
		else:
			return points

	def view_own_cards(self):
		card_text = ''
		cards = self.hand['face-down'] + self.hand['face-up']
		for card in cards:
			card_text += card['number'] + ' of ' + card['suit'] + '\n'
		return card_text

	def view_others_cards(self, me):
		cards_down = ''
		cards_up = ''
		for player in self.players:
			if player != me:
				cards_down = len(player.hand['face-down'])
				for card in player.hand['face-up']:
					cards_up += card['number'] + ' of ' + card['suit'] + '\n'
				print 'player ' + player.id + ' has ' + str(cards_down) + ' cards face down'
				print 'player ' + player.id + ' is showing: ' + cards_up