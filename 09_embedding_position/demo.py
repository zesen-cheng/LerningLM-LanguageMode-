"""第 09 课：Embedding 与位置。运行：python demo.py"""

def lesson_09():
    embeddings = {"猫": [1.0, 0.0], "追": [0.0, 1.0], "狗": [0.5, 0.5]}
    positions = [[0.0, 0.1], [0.1, 0.0], [0.2, 0.0]]
    encode = lambda words: [[a + b for a, b in zip(embeddings[word], positions[i])] for i, word in enumerate(words)]
    cat_chases_dog = encode(["猫", "追", "狗"])
    dog_chases_cat = encode(["狗", "追", "猫"])
    print("猫追狗首位置:", cat_chases_dog[0], "狗追猫首位置:", dog_chases_cat[0])
    assert cat_chases_dog != dog_chases_cat

if __name__ == '__main__':
    lesson_09()
