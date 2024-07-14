from collections import defaultdict
import re

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # Helper function to parse the formula and count atoms
        def parse_formula(s: str, i: int) -> tuple[defaultdict, int]:
            n = len(s)
            count = defaultdict(int)
            
            while i < n:
                if s[i] == '(':
                    # Recursively parse the sub-formula within the parentheses
                    sub_count, i = parse_formula(s, i + 1)
                    i += 1  # Skip the closing ')'
                    
                    # Get the multiplier after the parentheses, if any
                    start = i
                    while i < n and s[i].isdigit():
                        i += 1
                    multiplier = int(s[start:i] or 1)
                    
                    # Multiply the counts in the sub-formula
                    for atom, cnt in sub_count.items():
                        count[atom] += cnt * multiplier
                
                elif s[i] == ')':
                    return count, i
                
                else:
                    # Parse the atom name
                    start = i
                    i += 1
                    while i < n and s[i].islower():
                        i += 1
                    atom = s[start:i]
                    
                    # Parse the number after the atom name, if any
                    start = i
                    while i < n and s[i].isdigit():
                        i += 1
                    count[atom] += int(s[start:i] or 1)
            
            return count, i
        
        # Get the final atom counts by parsing the whole formula
        atom_count, _ = parse_formula(formula, 0)
        
        # Format the result as specified
        result = ""
        for atom in sorted(atom_count):
            result += atom
            if atom_count[atom] > 1:
                result += str(atom_count[atom])
        
        return result

# Test cases
solution = Solution()
print(solution.countOfAtoms("H2O"))  # Output: "H2O"
print(solution.countOfAtoms("Mg(OH)2"))  # Output: "H2MgO2"
print(solution.countOfAtoms("K4(ON(SO3)2)2"))  # Output: "K4N2O14S4"
