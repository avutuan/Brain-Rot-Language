from components.nfa import NFA

# accept function to determine if the NFA accepts the input string
def accept(A: NFA, w: str) -> str:
    acceptBoolean = A.run(w)
    if acceptBoolean:
        return "accepted"
    else:
        return "rejected"

# Create an NFA object and parse the input string to the NFA
nfa = NFA()
file = open("src/automata/brainRotNfa.txt", "r").read()
nfa.parse_input_to_nfa(file)

strings = [
    "the_sigma_cooked_the_yns",
    "the_opp_faded_the_rizzler",
    "the_low-taper-fade_mogged",
    "the_glizzy_cooked",
    "fanum-tax",
    "skibidi-toilet",
    "skibidi-toilet_fanum-tax_baby-oil",
    "apple",
    "the",
    "the_",
    "the_goat",
    "the_goat_",
    "the_goat’s_",
    "the_goat_cooked_",
    "the_goat_cooked_the",
    "",
    "the_sigma_cooked_the_yns_aura"
]

# Test cases
def run_tests():
    for i in strings:
        result = accept(nfa, i)
        # Find the longest string in the list
        max_length = max(len(s) for s in strings)
        # Pad the string with spaces to match the longest string

        formatted_string = f"{i:<{max_length + 2}}"
        print(f"{formatted_string}: {result}\n")
        
run_tests()