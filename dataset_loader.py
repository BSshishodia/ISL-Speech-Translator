import os

SIGN_FOLDER = "signs"

def load_dataset_words():

    words = []

    for file in os.listdir(SIGN_FOLDER):

        if file.endswith(".mp4"):

            name = file.replace(".mp4", "")

            words.append(name.lower())

    return words
    
if not os.path.exists(SIGN_FOLDER):
    return []
