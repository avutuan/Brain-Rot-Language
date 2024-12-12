from components.nfa import NFA

# accept function to determine if the NFA accepts the input string
def accept(A: NFA, w: str) -> str:
    acceptBoolean = A.run(w)
    if acceptBoolean:
        return "accept"
    else:
        return "reject"

# Create an NFA object and parse the input string to the NFA
nfa = NFA()
file = open("src/automata/brainRotNfa.txt", "r").read()
nfa.parse_input_to_nfa(file)

# Test cases
print(accept(nfa, "the_sigma_cooked_the_yns"))