import summarizer
import sys

print('Пожалуйста, введите только один аргумент.' if len(sys.argv[1:]) != 1 else summarizer.Summarizer().summarize(sys.argv[1]))