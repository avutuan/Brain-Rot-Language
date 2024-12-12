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
    print("-----------------------------------------------------")
    # Custom user input for the string to test
    x = False
    while not x:
        test = input("Enter a custom string to try and break our automaton! Enter 0 to stop: ")
        if test == "0":
            break
        print((tests.accept(nfa, test)))

if __name__ == "__main__":
    main()