text = "Python is very interesting"
new_text = ""
for i in range(len(text)):
  if text[i] == " ":
    new_text += "-"
  else:
    new_text += text[i]
print(new_text)