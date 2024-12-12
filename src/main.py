# Driver function for the program
from components.nfa import NFA
import tests

# Main function
def main():
    # Create an NFA object and parse the input string to the NFA
    nfa = NFA()
    file = open("src/automata/brainRotNfa.txt", "r").read()
    nfa.parse_input_to_nfa(file)
    
    # Automated testing 
    tests.run_tests()
    
    # Custom user input for the string to test
    print(nfa.run(input("Enter a personal string: ")))
    
if __name__ == "__main__":
    main()