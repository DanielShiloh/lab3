"""
Word Count
Daniel Shiloh
Counts the frequency of every word in a txt file, prints an alphabetical report
June 24, 2026
"""

from pathlib import Path
import string

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
    Present user with file options,
    on their choice print a list of words in the file and their counts
    """

    file_options = {
        1: Path("monte_cristo.txt"),
        2: Path("treasure_island.txt"),
        3: Path("Tarzan.txt"),
        4: Path("princess_mars.txt"),
    }

    while True:

        print("--- Word Analyzer ---\n")
        print("Please select a file to analyze:\n")

        for key, story in file_options.items():
            print(f"{key}. {story.stem.replace('_',' ').title()}")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        try:
            choice = int(choice)
            selected_path = file_options[choice]
            #find path for that story
        except ValueError:
            print("Invalid choice.  Please type a number, 1-5.")
            continue
        except FileNotFoundError:
            print("Invalid choice.  Please select from 1-5.")
            continue

        print(f"\nProcessing {file_options[choice]}...")


        #instance of WordAnalyzer

        #process_file()

        #if successful, print_report()

        again = input("Press Enter to return to the menu...")
        if again == "":
            break
