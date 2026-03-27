import difflib
import os

SIGN_FOLDER = "signs"

def find_best_match(word, dataset_words):

    match = difflib.get_close_matches(
        word,
        dataset_words,
        n=1,
        cutoff=0.6
    )

    if match:

        video_name = match[0]

        return os.path.join(SIGN_FOLDER, video_name + ".mp4")

    return None