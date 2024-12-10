# driver function for the program
from components.nfa import NFA
from components.state import State

def main():
    nfa = NFA()
    file = open("src/automata/exampleNfa.txt", "r").read()
    # print(file)
    print(nfa.parse_input_to_nfa(file))
    print(nfa.run("1101111"))
    
if __name__ == "__main__":
    main()
    