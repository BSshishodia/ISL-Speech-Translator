# ==============================
# Smart ISL Interpreter
# Final Version (Audio → ISL Video)
# ==============================

from speech_to_text import speech_to_text
from hindi_nlp import process_text
from isl_converter import convert_to_isl
from context_memory import ContextMemory
from dataset_loader import load_dataset_words
from translator import hindi_to_english
from sign_finder import find_best_match
from video_merger import merge_videos
import os


def main():

    print("\n===== SMART ISL INTERPRETER =====\n")

    # -----------------------------
    # 1️⃣ Audio Input
    # -----------------------------
    audio_path = r"sample_audio/test.wav"

    if not os.path.exists(audio_path):
        print("❌ Audio file not found!")
        return

    # -----------------------------
    # 2️⃣ Speech → Text
    # -----------------------------
    print("🎤 Converting Speech to Text...\n")

    text = speech_to_text(audio_path)

    print("📝 Recognized Text:")
    print(text)

    # -----------------------------
    # 3️⃣ Hindi NLP Processing
    # -----------------------------
    print("\n🧠 Processing Text...\n")

    tokens = process_text(text)

    print("Tokens:", tokens)

    # -----------------------------
    # 4️⃣ Context Memory
    # -----------------------------
    memory = ContextMemory()

    tokens = memory.resolve_reference(tokens)
    memory.update_memory(tokens)

    # -----------------------------
    # 5️⃣ Convert to ISL Grammar
    # -----------------------------
    print("\n🔄 Converting to ISL Structure...\n")

    isl_output = convert_to_isl(tokens)

    print("🤟 ISL Structured Sentence:")
    print(" ".join(isl_output))

    # -----------------------------
    # 6️⃣ Load Dataset Words
    # -----------------------------
    dataset_words = load_dataset_words()

    # -----------------------------
    # 7️⃣ Hindi → English Translation
    # -----------------------------
    print("\n🔁 Translating Hindi → English\n")

    translated_words = []

    for word in isl_output:

        english_word = hindi_to_english(word)

        translated_words.append(english_word)

    print("English words:", translated_words)

    # -----------------------------
    # 8️⃣ Find Sign Videos
    # -----------------------------
    print("\n🔍 Searching sign videos...\n")

    video_list = []

    for word in translated_words:

        video = find_best_match(word, dataset_words)

        if video:

            print("Matched:", word)

            video_list.append(video)

        else:

            print("⚠ No sign found for:", word)

    # -----------------------------
    # 9️⃣ Merge Sign Videos
    # -----------------------------
    if len(video_list) == 0:

        print("\n❌ No videos found to merge")

    else:

        print("\n🎬 Creating final ISL translation video...\n")

        merge_videos(video_list)

        print("\n✅ Translation video created successfully!")

    print("\n===== PROCESS COMPLETE =====\n")


# Run Program
if __name__ == "__main__":
    main()
