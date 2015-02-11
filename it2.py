from numpy import *
import itertools as it
import matplotlib.pyplot as plt
import multiprocessing as mp
import models

def count_pattern(pattern, data):
	pattern = ''.join([str(i) for i in pattern])
	data = ''.join([str(i) for i in data])

	index = 0
	n = 0

	try: 
		while True:
			index = data.index(pattern, index + 1)
			n += 1
	except ValueError:
		return n

def stats(n, data):
	print("Start %d" % n)
	patterns = [''.join([str(pi) for pi in p]) for p in it.product(*([[0,1]]*n))]
	counts = [count_pattern(pattern, data) for pattern in patterns]
	freqs = array(counts) / sum(counts)
	
	idx = where(freqs > 0.0)

	print("Finish %d" % n)
	return sum(freqs[idx] * log2(1.0 / freqs[idx]))

if __name__ == '__main__':
	model = models.homework

	data = array(list(model(1000)))
	m = [0, 1, 2, 3, 4, 5, 6, 7, 8]

	pool = mp.Pool(8)
	res = [pool.apply_async(stats, (m, data)) for m in m]

	pool.close()
	pool.join()

	Sm = [res.get() for res in res]

	mk = m[2:]
	k = [-Sm[m] + 2 * Sm[m-1] - Sm[m-2] for m in mk]

	mk = [1] + mk
	k = [log2(2) - Sm[1]] + k

	print(k)

	eta = sum((array(mk) - 1) * array(k))
	print('eta =', eta)

	plt.subplot(2, 1, 1)
	plt.plot(m, Sm, 'bx-')
	plt.xlabel('$m$')
	plt.ylabel('$S_m$')
	plt.grid(True)

	k = array(k)
	k[where(k < 0.0)] = 0.0

	plt.subplot(2, 1, 2)
	plt.plot(mk, k, 'bx-')
	plt.xlabel('$m$')
	plt.ylabel('$k_m$')
	plt.grid(True)
	plt.show()
