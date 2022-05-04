import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.match (patron,texto))
print(texto[22:26])
print (re.search(patron,texto).group())
print (re.findall(patron,texto))