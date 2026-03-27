from dataset_loader import load_dataset_words


def main():

    words = load_dataset_words()

    print("\n===== DATASET WORD LIST =====\n")

    for w in sorted(words):
        print(w)

    print("\nTotal dataset words:", len(words))


if __name__ == "__main__":
    main()