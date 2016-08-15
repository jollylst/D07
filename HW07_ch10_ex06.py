# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(l):
	if len(l) <= 1:
		return True
	else:
		for i in range(len(l) - 1):
			if l[i + 1] < l[i]:
				return False 
		return True


def main():
	pass
if __name__ == "__main__":
	main()
