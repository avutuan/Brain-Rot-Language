# Automaton of general NFA
from components.state import State

class NFA:
    def __init__(self):
        self.states: list = []
        self.alphabet: list = []
        self.initial_state: State = None
        self.final_states: list = []
        
    def __str__(self):
        return f"Initial state: {self.initial_state}, \nFinal states: {self.final_states}, \nStates: {self.states}, \nTransitions: {[(state, state.transitions) for state in self.states]}"
    
    def _transition_table(self):
        for state in self.states:
            state.transitions = self.transitions[state.name]
    
    def add_state(self, state: State):
        self.states.append(state)
    
    def set_initial_state(self, state: State):
        self.initial_state = state
    
    def add_final_state(self, state: State):
        self.final_states.append(state)
    
    def run(self, input_string: str):
        current_state = self.initial_state
        symbol_list = []
        string_builder = ""
        
        for char in input_string:
            string_builder += char
            if string_builder in self.alphabet:
                symbol_list.append(string_builder)
                string_builder = ""
        
        for symbol in symbol_list:
            current_state = current_state.next_state(symbol)
            if current_state is None and current_state not in self.final_states:
                return False
        return current_state in self.final_states
    
    def parse_input_to_nfa(self, input_string: str):
        # Parsing input string to list of lists
        input = input_string.split("\n")
        for i in range(len(input)):
            input[i] = input[i].split(" ")
            
        # Initialize sensible variables for the input
        input_states = input[0]
        input_alphabet = input[1]
        input_initial_state = input[2][0]
        input_final_states = input[3]
            
        # Adding states to the NFA
        for state in input_states:
            self.add_state(State(state))
        
        # Adding alphabet to the NFA
        for char in input_alphabet:
            self.alphabet.append(char)
            
        # Adding transitions to the NFA
        for i in range(4, len(input)):
            state = input[i][0]
            symbol = input[i][1]
            next_state = input[i][2]
            for s in self.states:
                if s.name == state:
                    state = s
                if s.name == next_state:
                    next_state = s
            if state in self.states and next_state in self.states and symbol in self.alphabet:
                state.add_transition(symbol, next_state)
            else:
                return "Error: Transition not valid"
        
        # Setting initial state of the NFA
        if input_initial_state in input_states:
            for state in self.states:
                if state.name == input_initial_state:
                    self.set_initial_state(state)
        else:
            return "Error: Initial state not in list of states"
        
        # Adding final states to the NFA
        for final_state in input_final_states:
            if final_state in input_states:
                for state in self.states:
                    if state.name == final_state:
                        self.add_final_state(state)
            else:
                return "Error: Final state not in list of states"
        
        return self
