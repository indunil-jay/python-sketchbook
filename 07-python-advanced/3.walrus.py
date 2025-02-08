
def get_info(text: str):

    return {
        'text': text,
        "letters": (length := len(text.replace(" ", ""))),
        "words": (words := text.split()),
        "total_words": (word_length := len(words)),
        "avg_per_word": round(length/word_length, 2)
    }


print(get_info("hello world"))
