from collections import defaultdict
from sys import argv
import random
import re



def markovDictSimple(s, split=""):
	i_words = defaultdict(lambda : list())
	words = s.split()
	for index, word in enumerate(words):
		try:
			i_words[word].append(words[index+1])
		except:
			pass
	return i_words
	
def markovDictDepth(s, depth=1):
	i_words = defaultdict(lambda : list())
	words = s.split()
	i = 0
	depth_words = []
	while i < len(words):
		word_a = ''
		for j in range(depth):
			try:
				word_a = " ".join((word_a, words[i+j]))
			except:
				pass
		depth_words.append(word_a)
		i += depth
	for index, word in enumerate(depth_words):
		try:
			i_words[word].append(depth_words[index+1])
		except:
			pass
	return i_words
	
def markovString(str, size=25, depth=1, initial_list=None):
	word_d = markovDictDepth(str, depth)
	last_word = random.choices(list(word_d.keys()))[0]
	if initial_list is None:
		current_s = last_word
	else:
		current_s = random.choices(initial_list)[0]
		if current_s == '' or " ":
			current_s = last_word
	for i in range(size):
		if(word_d[last_word] == [] or word_d[last_word] is None):
			last_word = random.choices(list(word_d.keys()))[0]
		else:
			new_word = random.choices(word_d[last_word])[0]
			current_s = "".join((current_s, new_word))
			#print(word_d[last_word])
			last_word = new_word
	return current_s
	
if __name__ == "__main__":
	_, path, size, depth = argv		
	with open(path, 'r') as dict:
		current_s = markovString(dict.read().lower(), int(size), int(depth))
	
	print("\n",current_s)
