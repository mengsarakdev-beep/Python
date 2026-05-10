import sys
class RedirectStdoutToFile:
    def __enter__(self):
        # Save the original stdout
        self.original_stdout = sys.stdout

        # Open the file for writing and redirect stdout to it
        self.file = open("output.txt", "w")
        sys.stdout = self.file

        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        # Restore the original stdout
        sys.stdout = self.original_stdout

        # Close the file
        self.file.close()

        # Handle exceptions (if any)
        if exc_type:
            print(f"An error occurred: {exc_value}")
            return False  # Re-raise the exception
        return True

# Usage Example
print("This will print to the console.")

with RedirectStdoutToFile() as file:
    print("This will be written to the file output.txt.")

print("This will again print to the console.")