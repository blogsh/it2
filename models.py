from numpy import *

def exercise37(n = 1000):
	A = 0
	B = 1
	C = 2
	D = 3

	state = random.choice([A, B, C, D])

	for _ in range(n):
		if state == A:
			state = B
			yield 1
		if state == B:
			if random.random() < 0.5:
				state = B
				yield 1
			else:
				state = C
				yield 0
		if state == C:
			state = D
			yield 0
		if state == D:
			if random.random() < 0.5:
				state = D
				yield 0
			else:
				state = A
				yield 1

def crystal(n = 1000):
	A = 0
	B = 1

	state = random.choice([A, B])

	for _ in range(n):
		if state == A:
			state = B
			yield 0
		if state == B:
			state = A 
			yield 1

def gas(n = 1000):
	A = 0
	B = 1

	state = random.choice([A, B])

	for _ in range(n):
		if random.random() < 0.5:
			state = A
			yield 0
		else:
			state = B
			yield 1

def homework(n = 1000):
	A = 0
	B = 1
	C = 2
	D = 3
	E = 4

	state = random.choice([A, B, C, D, E])

	for _ in range(n):
		if state == A:
			if random.random() < 0.5: 
				state = B
				yield 1
			else:
				state = E
				yield 0
		if state == B:
			state = C
			yield 0
		if state == C:
			state = D
			yield 0
		if state == D:
			state = A
			yield 1
		if state == E:
			state = C
			yield 0
