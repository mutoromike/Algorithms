def runLengthEncoding(string):
    # Write your code here.
    # Input = "AAAAAAAAAAAAABBCCCCDD"
    # Output = "9A4A2B4C2D"
	chars = []
	count = 1
	end = len(string) - 1
	if len(string) == 1:
		return "1"+string
	char_at = 1
	for i, string_ in enumerate(string):
		if i > 0:
			if string_ == string[i-1]:
				if count == 9:
					chars.append(str(count)+string_)
					count = 1
				else:
					count += 1
			if string_ != string[i-1]:
				chars.append(str(count)+string[i-1])
				count = 1
			if i == end:
				chars.append(str(count)+string_)
    return ''.join(chars)
