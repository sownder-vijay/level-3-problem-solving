text = "programming"
text2 = ""
count = 0
for i in range(len(text)):
  if text[i] in text[i+1:] and text[i] not in text2:
    text2 += text[i]
for j in range(len(text)):
  if text[j] not in text2:
    print(text[j], end="")
