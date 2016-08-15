# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_all(t):
	res = []
	for s in t:
		res.append(s.capitalize())
	return res

def capitalize_nested(nested_list):
	new_list = []
	for i in nested_list:
		if type(i) == list:
			new_list.append(capitalize_all(i))
		else:
			new_list.append(i.capitalize())
	return new_list

def main():
	pass
if __name__ == "__main__":
	main()
