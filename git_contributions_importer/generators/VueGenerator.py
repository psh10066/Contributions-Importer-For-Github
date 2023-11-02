#!/usr/bin/python3

from . import Generator
import random

class VueGenerator(Generator):
    # one day this will generate awesome random code

    min_content_size = 2

    def __init__(self):
        pass

    def insert(self, content, num):
        if len(content) <= self.min_content_size:
            content.clear()
            content.append('<template>')
            content.append('</template>')
        for i in range(num):
            content.insert(-1, '  <div>' + self.random_phrase(random.random() * 10 + 1) + '</div>')

    def delete(self, content, num):
        for i in range(min(num, len(content) - self.min_content_size)):
            content.pop(-2)