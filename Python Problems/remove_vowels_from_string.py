text = "programming"
new_text = ""
for i in range(len(text)):
  if text[i] not in ['a', 'e', 'i', 'o', 'u']:
    new_text += text[i]
print(new_text)