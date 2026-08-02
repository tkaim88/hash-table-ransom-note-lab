def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    # Count the frequency of each character in the magazine
    char_count = {}

    for char in magazine:
        char_count[char] = char_count.get(char, 0) + 1

    # Check if each character in the ransom note is available
    for char in ransomNote:
        if char not in char_count or char_count[char] == 0:
            return False

        char_count[char] -= 1

    return True