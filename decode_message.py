#!/usr/bin/env python3
"""
Decode the intern's message by analyzing keyboard patterns.
The message appears to be typed with shifted hand positions on a QWERTY keyboard.
"""

def decode_keyboard_shift(message):
    """
    Decode a message where each letter is shifted one key to the right on a QWERTY keyboard.
    """
    # QWERTY keyboard layout mapping (each key maps to the key on its left)
    keyboard_map = {
        # Top row
        'W': 'Q', 'E': 'W', 'R': 'E', 'T': 'R', 'Y': 'T', 'U': 'Y', 'I': 'U', 'O': 'I', 'P': 'O',
        # Middle row
        'S': 'A', 'D': 'S', 'F': 'D', 'G': 'F', 'H': 'G', 'J': 'H', 'K': 'J', 'L': 'K',
        # Bottom row
        'X': 'Z', 'C': 'X', 'V': 'C', 'B': 'V', 'N': 'B', 'M': 'N',
        # Lowercase
        'w': 'q', 'e': 'w', 'r': 'e', 't': 'r', 'y': 't', 'u': 'y', 'i': 'u', 'o': 'i', 'p': 'o',
        's': 'a', 'd': 's', 'f': 'd', 'g': 'f', 'h': 'g', 'j': 'h', 'k': 'j', 'l': 'k',
        'x': 'z', 'c': 'x', 'v': 'c', 'b': 'v', 'n': 'b', 'm': 'n',
    }
    
    decoded = ""
    for char in message:
        decoded += keyboard_map.get(char, char)
    
    return decoded

def main():
    encrypted_message = "WERTYUESDTOHJY"
    
    print("=" * 50)
    print("CLASSIFIED MESSAGE RECOVERY")
    print("=" * 50)
    print(f"\nEncrypted message: {encrypted_message}")
    print("\nAnalyzing keyboard shift pattern...")
    
    # Decode by shifting each letter one key to the left
    decoded_message = decode_keyboard_shift(encrypted_message)
    
    print(f"\n✓ DECODED MESSAGE: {decoded_message}")
    print("\nExplanation: The intern's hands were shifted one key to the")
    print("right on the QWERTY keyboard. Each letter typed was one")
    print("position to the right of the intended letter.")
    print("=" * 50)

if __name__ == "__main__":
    main()
