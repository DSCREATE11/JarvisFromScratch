# get_vocab.py
import urllib.request

url = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa-no-swears.txt"
output_path = "/home/divyam/Jarvis/local_model2/vocabulary.txt"

print("Downloading 10,000-word vocabulary text file...")
urllib.request.urlretrieve(url, output_path)
print("Saved vocabulary.txt successfully!")
