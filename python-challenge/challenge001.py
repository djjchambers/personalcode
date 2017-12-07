lista = "abcdefghijklmnopqrstuvwxyz"
listb = "cdefghijklmnopqrstuvwxyzab"
emptystr = ''

stringtodecode = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

for char in stringtodecode:
	if char == ' ':
		emptystr += ' '
	else:
		listindex = int(lista.find(char))
		emptystr += (listb[listindex])

print(emptystr)