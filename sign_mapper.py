import os

SIGN_FOLDER = "signs"

def find_sign_video(word):

    word = word.lower()

    for file in os.listdir(SIGN_FOLDER):

        name = file.split(".")[0].lower()

        if name == word:
            return os.path.join(SIGN_FOLDER, file)

    return None