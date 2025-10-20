def count_string_properties(text):
    total_chars = len(text)
    
    chars_no_space = len(text.replace(" ", ""))
    

    words = len(text.split())
    
    # Count vowels
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    
    return total_chars, chars_no_space, words, vowel_count

# Input string
text = "Hello World Python Programming"

# Get counts
total, no_space, words, vowels = count_string_properties(text)

# Display results
print(f"String: '{text}'")
print(f"Total characters: {total}")
print(f"Characters (no spaces): {no_space}")
print(f"Number of words: {words}")
print(f"Number of vowels: {vowels}")

# Count specific character
char_to_count = 'o'
specific_count = text.lower().count(char_to_count.lower())
print(f"Occurrences of '{char_to_count}': {specific_count}")
