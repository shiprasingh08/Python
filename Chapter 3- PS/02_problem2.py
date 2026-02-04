letter = '''
Dear <|Name|>,
You are selected!
Date: <|Date|>

'''

print(letter.replace("<|Name|>", "Aditya")
      .replace("<|Date|>", "20th June 2024"))