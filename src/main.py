# driver function for the program
from components.nfa import NFA

def main():
    nfa = NFA()
    file = open("src/automata/brainRotNfa.txt", "r").read()
    nfa.parse_input_to_nfa(file)
    print(nfa.run(input("Enter a string: ")))
    
if __name__ == "__main__":
    main()
    