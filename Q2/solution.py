import math

def solve(input_file, output_file):
    with open(input_file, 'r') as infile:
        # Read number of test cases
        T = int(infile.readline().strip())
        
        results = []
        
        for t in range(1, T + 1):
            # Read N and P for each test case
            N, P = map(int, infile.readline().strip().split())
            
            # Convert P to a decimal probability (P%)
            prob_P = P / 100.0
            
            # Success probability with N-1 lines: (P/100)^(N-1)
            prob_N_minus_1 = prob_P**(N-1)
            
            # Find the required P' such that (P'/100)^N = (P/100)^(N-1)
            required_P = (prob_N_minus_1**(1 / N)) * 100
            
            # The increase in P is:
            increase_in_P = required_P - P
            
            # Store the result formatted to 15 decimal places
            results.append(f"Case #{t}: {increase_in_P:.15f}")
    
    # Write results to the output file
    with open(output_file, 'w') as outfile:
        outfile.write("\n".join(results) + "\n")

# Example usage
input_file = 'line_by_line_input.txt'
output_file = 'output.txt'
solve(input_file, output_file)
