def modify_artist_list(artists):
    try:
        index = int(input("Enter the index of the artist to replace (1-10): ")) - 1
        new_artist = input("Enter the new artist's name: ")
        artists[index] = new_artist
        print(f"Artist at position {index + 1} replaced with {new_artist}.")
    except (ValueError, IndexError):
        print("An input error occurred. Please ensure the index is a number between 1 and 10.")

def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    
    print("Top Performing Artists List:")
    for i, artist in enumerate(top_artists, start=1):
        print(f"{i}. {artist}")
        
    modify_artist_list(top_artists)

    print("\nUpdated Artist List:")
    for i, artist in enumerate(top_artists, start=1):
        print(f"{i}. {artist}")

if __name__ == "__main__":
    main()
