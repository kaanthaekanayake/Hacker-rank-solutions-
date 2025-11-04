def mutate_string(string,position,character):
    """This function mutates a string by changing the character at the specified position to the given character.

    Args:
        string (str): The original string to be mutated.
        position (int): The index position of the character to be changed.
        character (str): The new character to insert at the specified position.

    Returns:
        str: The mutated string with the character at the specified position changed.
    """
    # Convert the string to a list to allow mutation
    character_list = list(string)
    
    # Change the character at the specified position
    character_list[position] = character
    
    # Join the list back into a string and return
    return ''.join(character_list)

if __name__ == '__main__':
    getmutatestring = input().strip()
    position, character = input().split()
    changedstring = mutate_string(getmutatestring, int(position), character)
    print(changedstring)