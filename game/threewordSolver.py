import itertools
import os
from collections import defaultdict, Counter


class threewordSolver:
    def __init__(self, word_length=3):
        self.word_length = word_length
        self.words = self.load_words()
        self.possible_words = self.words[:]
        self.current_guess = self.possible_words[0]
        self.feedback = None

    def load_words(self):
        # Ensure the path is constructed correctly
        base_dir = os.path.dirname(__file__)  # Current script directory
        filename = os.path.join(base_dir, f"{self.word_length}_letter_words.txt")
        try:
            with open(filename, 'r') as f:
                words = [line.strip().lower() for line in f if len(line.strip()) == self.word_length]
                return words
        except FileNotFoundError:
            print(f"Word list file '{filename}' not found.")
            exit()
    
    def count_common_letters(self, word1, word2):
        c1 = Counter(word1)
        c2 = Counter(word2)
        common = c1 & c2
        return sum(common.values())

    def build_graph_incremental(self, feedback):
        graph = {}
        for word in self.possible_words:
            if self.count_common_letters(word, self.current_guess) == feedback:
                graph[word] = []
        for word in graph:
            for other_word in graph:
                if word != other_word:
                    weight = self.count_common_letters(word, other_word)
                    if weight > 0:
                        graph[word].append((other_word, weight))
        return graph

    def select_next_guess(self, graph):
        max_degree = -1
        best_guess = None
        for word, neighbors in graph.items():
            degree = len(neighbors)
            if degree > max_degree:
                max_degree = degree
                best_guess = word
        return best_guess

    def process_feedback(self, feedback):
        self.feedback = feedback
        graph = self.build_graph_incremental(feedback)
        self.possible_words = list(graph.keys())
        self.current_guess = self.select_next_guess(graph) if self.possible_words else None
        return self.possible_words, self.current_guess
