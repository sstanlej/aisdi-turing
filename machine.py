import sys

def load_transitions(filename):
    transitions = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 5:
                current_state, current_symbol, new_symbol, direction, new_state = parts
                transitions[(current_state, current_symbol)] = (new_symbol, direction, new_state)
    return transitions

def is_halt_state(state):
    return state.startswith("halt")

def print_tape(tape, head, state):
    print(''.join(tape).rstrip('_'), state)
    print(' ' * head + '^')

def run_turing_machine(tape_input, transition_file):
    transitions = load_transitions(transition_file)
    tape = list(tape_input) + ['_']
    head = 0
    state = 'init'

    while True:
        print_tape(tape, head, state)

        if is_halt_state(state):
            break

        if head >= len(tape):
            tape.append('_')
        elif head < 0:
            tape.insert(0, '_')
            head = 0

        current_symbol = tape[head]
        key = (state, current_symbol)

        if key not in transitions:
            break

        new_symbol, direction, new_state = transitions[key]
        tape[head] = new_symbol

        if direction == 'L':
            head -= 1
        elif direction == 'R':
            head += 1

        state = new_state

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python machine.py <tape> <transitions_file>")
        sys.exit(1)

    tape_input = sys.argv[1]
    transition_file = sys.argv[2]
    run_turing_machine(tape_input, transition_file)
