def get_word_count(text):
    return print(f"Found {len(text.split())} total words")

def get_letter_count(text):
    letter_count = {}
    for letter in text.split():
        letter = letter.lower()
        for char in letter:
          if char in letter_count:
            letter_count[char] += 1
          else:
            letter_count[char] = 1
    return letter_count

def sort_on_value(dict):
  sorted_list = []
  for key, letter_count in dict.items():
    sorted_list.append({"char": key, "count": letter_count})
  sorted_list.sort(key=lambda x: x["count"], reverse=True)
  return sorted_list
