# As described in the paper, maps are generated by a self-driving automaton.
# Note: I was not able to figure out how to program this so that the SDA example in the paper
# reproduces the output claimed.

class SDA:
    def __init__(self, labels, transitions):
        self.emit = labels
        self.next_state = transitions
        self.reset()

    # reset should be called every time a new map is generated.
    def reset(self):
        # Initialize parameters for producing bits
        self.bitstring = self.emit[0]
        self.num_bits = 0 # Number of bits produced so far. Grand total
        self.cur_bit = 0 # Number of bits produced so far on the current string

    # Feed the current output string back into the SDA to generate a longer output string.
    def expand_string(self):
        cur_node = 0
        new_string = self.emit[cur_node]
        for i in range(len(self.bitstring)):
            cur_node = self.next_state[cur_node][int(self.bitstring[i])]
            new_string = new_string + self.emit[cur_node]
        self.bitstring = new_string

    # Return a single bit (0 or 1), expanding the output string if necessary.
    def get_bit(self):
        if self.cur_bit >= len(self.bitstring):
            self.cur_bit = 0 # Not clear whether we want this line
            self.expand_string()
        bit = self.bitstring[self.cur_bit]
        self.cur_bit += 1
        self.num_bits += 1
        return int(bit)

    # Get multiple bits. This is the main interface for map generation.
    def get_bits(self,n):
        return [self.get_bit() for i in range(n)]
