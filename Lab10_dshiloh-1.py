"""
Word Count
Daniel Shiloh
Counts the frequency of every word in a txt file, prints an alphabetical report
June 24, 2026
"""

from pathlib import Path
import string

#unicode quotes
extra_punctuation = "“”‘’"

class WordAnalyzer:
    """
    """

    def __init__(self, filepath):
        """
        Args: filepath: str, path of txt file
        Create dictionary for word frequencies
        """
        self.filepath = Path(filepath)
        self.frequencies = {}
    
    def process_file(self):
        """
        Check that the file path exists,
        remove punctuation,
        read line by line and update frequencies
        """
        try:
            if not self.filepath.exists():
                raise FileNotFoundError
        
            translator = str.maketrans('', '', string.punctuation + extra_punctuation)

            with self.filepath.open('r', encoding='utf-8') as file:
                for line in file:
                    plain_line = line.translate(translator).lower()
                    words = plain_line.split()
                    for word in words:
                        self.frequencies[word] = self.frequencies.get(word, 0) + 1
            return True
        
        except FileNotFoundError:
            print(f"{self.filepath} could not be found.")
            return False

    
    def print_report(self):
        """
        Sort words, print with frequencies
        Use length of longest word for column alignment
        """
        sorted_words = sorted(self.frequencies.keys())

        if not sorted_words:
            print("No words found.")
            return
        
        max_len = max(len(word) for word in sorted_words)

        for word in sorted_words:
            print(f"{word:<{max_len}} :: {self.frequencies[word]}")

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

        print("\n--- Word Analyzer ---\n")
        print("Please select a file to analyze:\n")

        for key, story in file_options.items():
            print(f"{key}. {story.stem.replace('_',' ').title()}")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == 5:
            print("Goodbye!")
            break
    
        try:
            choice = int(choice)
            selected_path = file_options[choice]
        except ValueError:
            print("Invalid choice.  Please type a number.")
            continue
        except FileNotFoundError:
            print("Invalid choice.  Please select from 1-5.")
            continue

        print(f"\nProcessing {file_options[choice]}...")

        analyzer = WordAnalyzer(str(selected_path))

        if analyzer.process_file():
            analyzer.print_report()
            
        again = ""
        again = input("Press Enter to return to the menu...")
        if again != "":
            break

if __name__ == "__main__":
    main()