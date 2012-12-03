# undersample on disk

# use a generator to count y

def count_y(filename):
	with open(filename, 'r') as f:
		y_column = (line.split(',')[-1] for line in f)
		counter = collections.Counter((i.strip() for i in y_column))
		return counter
