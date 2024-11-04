def main():
    flower_list = []
    print("Enter flower names one by one. Type 'done' when you're finished.")
    
    while True:
        flower = input("Enter a flower name: ").strip()
        if flower.lower() == 'done':
            break
        if flower:
            flower_list.append(flower)

    flower_list.sort()

    print("\nSorted Flower List:")
    for i, flower in enumerate(flower_list, start=1):
        print(f"{i}. {flower}")

    while True:
        search = input("\nEnter a flower name to search for: ").strip()
        if not search:
            print("Please enter a valid flower name.")
            continue
        if search in flower_list:
            print(f"{search} found in the list.")
        else:
            print(f"{search} is not in the list.")

        try:
            index = int(input("Enter a number to access the corresponding flower: "))
            print(f"Flower at position {index}: {flower_list[index - 1]}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except IndexError:
            print("Index out of range. Please enter a valid index.")
        except:
            print("An error occurred:")

if __name__ == "__main__":
    main()
