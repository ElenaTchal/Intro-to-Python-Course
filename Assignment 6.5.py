text = "X-DSPAM-Confidence:    0.8475";
piece = text.find(" ")
piece2 = text[piece:]
piece3 = piece2.strip()
print(float(piece3))
