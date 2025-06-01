import requests

def random_words_generator(count: int):
    if count > 10000:
        return print('Maximum 10000 words')
    else:
        url = f'https://random-word-api.herokuapp.com/word?number={count}'
        response = requests.get(url)
        if response.status_code == 200:
            words = response.json()
            return words
        else:
            raise Exception(f"Error fetching words: {response.status_code}")



print(random_words_generator(10000))

for word in random_words_generator(10000):
    print(word)