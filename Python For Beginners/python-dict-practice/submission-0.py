from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    character_count = {}
    for character in word:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count





# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
