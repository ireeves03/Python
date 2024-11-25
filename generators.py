def two_letter_combinations(characters):
    # Implement the generator function 
    for char1 in characters:
        for char2 in characters:
            yield char1 + char2

def main():
    # 5-letter list
    characters = ['l', 'm', 'n', 'o', 'p']
    
    # Call the generator function and print each combination
    for combination in two_letter_combinations(characters):
        print(combination)

main()
