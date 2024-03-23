import rand as rand
import time
import string
vowels = string.ascii_lowercase[0:5]
consonants = string.ascii_lowercase[5:]
def choose_letter():
  r = rand.random()
  if r < 0.5:
    return rand.choice(vowels)
  else:
    return rand.choice(consonants)
def make_word():
  length = rand.randint(3, 10)
  word = ""
  vowel_count = 0
  for i in range(length):
    letter = choose_letter()
    word += letter
    if letter in vowels:
      vowel_count += 1
  if vowel_count == 0:
    word = word[:-1] + rand.choice(vowels)
  return word

def make_definition(word):
  definition = ""
  length = len(word)
  vowel_count = sum(letter in vowels for letter in word)
  consonant_count = length - vowel_count
  first_letter = word[0]
  last_letter = word[-1]
  if vowel_count > consonant_count:
    if first_letter in vowels:
      definition += "an "
    else:
      definition += "a "
    if last_letter == "a":
      definition += "type of cheese"
    elif last_letter == "e":
      definition += "musical instrument"
    elif last_letter == "i":
      definition += "rare disease"
    elif last_letter == "o":
      definition += "mythical creature"
    elif last_letter == "u":
      definition += "slang term for money"
    else:
      definition = "a random noun"
  else:
    definition += "to "
    if last_letter == "a":
      definition += "dance"
    elif last_letter == "e":
      definition += "sing"
    elif last_letter == "i":
      definition += "study"
    elif last_letter == "o":
      definition += "jump"
    elif last_letter == "u":
      definition += "run"
    else:
      definition = "a random verb"
  return definition

while True:
  word = make_word()
  print(word)
  definition = make_definition(word)
  print(definition)
  time.sleep(5)
