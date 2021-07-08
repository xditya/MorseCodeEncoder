# By @xditya

# Translator based off GeeksForGeeks, modded and made simple for suiting my needs.
# https://www.geeksforgeeks.org/morse-code-translator-python/

from telethon import Button

"""
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
"""

MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}

# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    return "".join(
        MORSE_CODE_DICT[letter] + " " if letter != " " else " " for letter in message
    )


# Function to decrypt the string
# from morse to english
def decrypt(message):
    # extra space added at the end to access the
    # last morse code
    message += " "
    decipher = ""
    citext = ""
    for letter in message:
        # checks for space
        if letter != " ":
            # counter to keep track of space
            i = 0
            # storing morse code of a single character
            citext += letter
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:
                # adding space to separate words
                decipher += " "
            else:
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[
                    list(MORSE_CODE_DICT.values()).index(citext)
                ]
                citext = ""
    return decipher


async def encode_deocde(event, type_):
    msg = event.text.split(" ", 1)
    try:
        text = msg[1]
    except IndexError:
        return await event.reply("Please use /{type_} <some text>")
    msgg = encrypt(text.upper()) if type_ == "encode" else decrypt(text)
    await event.reply(f"`{msgg}`")


async def send_start(event, type):
    user = await event.client.get_entity(event.sender_id)
    msg = f"Hi {user.first_name}, I'm a Morse Code Encoder bot. \nCheck the help for more info."
    buttons = [
        [Button.inline("Help 🆘", data="help_me")],
        [Button.url("Channel 💭", url="https://t.me/BotzHub")],
    ]
    if type == "message":
        await event.reply(msg, buttons=buttons)
    elif type == "edt":
        await event.edit(msg, buttons=buttons)
