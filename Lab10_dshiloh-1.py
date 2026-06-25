"""
Word Count
Daniel Shiloh
Counts the frequency of every word in a txt file, prints an alphabetical report
June 24, 2026
"""

from pathlib import Path

class WordAnalyzer:
    """
    """

    def __init__(self, filepath):
        """
        """
        #store filepath as private pathlibrary
    
    def process_file(self):
        """
        """
    
    def print_report(self):
        """
        """

def main():
    """
    """
    intro = "--- Word Analyzer ---\n"
    intro += "Please select a file to analyze:\n"
    intro += "1. Monte Cristo\n"
    intro += "2. Treasure Island\n"
    intro += "3. Tarzan\n"
    intro += "4. Princess Mars\n"
    intro += "5. Exit\n"

    while True:

        print(intro)
        choice = input("Enter your choice (1-5): ")

        try:
            choice = int(choice)
            #find path for that story
        except ValueError:
            #print needs to be a number 1-5
            continue
        except FileNotFoundError:
            #print invalid input
            continue

        choice_path = 0
        choice_title = ""
        #if 1, monte_cristo.txt...

        print(f"\nProcessing {choice_title}...")

        #instance of WordAnalyzer

        #process_file()

        #if successful, print_report()

        print("Press Enter to return to the menu...")