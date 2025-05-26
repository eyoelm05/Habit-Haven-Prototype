import random  # For random motivation selection

class Motivation:
    ## Initializes the Motivation class.
    def get_motivation(self):
        try:
            # Open motivational quotes file
            with open("motivational_quotes.txt", "r", encoding="utf-8") as file:
                # Set a delimiter: used to separate one quote from another inside the file
                delimiter = ','

                # Read files
                raw_quotes = file.read()
                quotes_list = []

                # Capitalize and add full stop to each quote
                for quote in raw_quotes.split(delimiter):
                    quotes_list.append(quote.strip().capitalize() + ".")
                # Print a random quote from the list
                print(random.choice(quotes_list))
                ## Return a random quote
        except FileNotFoundError:
            print("motivational_quotes.txt was not found!")

