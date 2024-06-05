txt = input()
smiles = []
for i, value in enumerate(txt):
	if (value == ":" or value == ";") and i != len(txt) - 1:
		if txt[i + 1] == ")":
			smiles.append(i)
		elif txt[i + 1] == "-":
			if txt[i + 2] == ")":
				smiles.append(i)
for i in smiles:
	print(i)
