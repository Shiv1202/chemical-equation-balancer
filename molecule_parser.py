import re
import pandas as pd
"""
element_name is: capital letter followed by optionl lower-case
    eg:
        C => 'carbon'
        H => 'hydrogen'
        Fe => 'iron'
        Hg => 'mercury'

count is: empty string (so the count is 1), or a set of digits
    eg:
        CH3 => {
            'carbon': 1,
            'hydrogen': 3
        }
"""

molecule_pat = re.compile("([A-Z][a-z]?)(\d*)")

class MoleculeParser:
    def parse(self, molecule):
        all_element = dict()
        # print("\tPlease enter a valid chemical formula => {CH3COOH}")
        for (element_name, count) in molecule_pat.findall(molecule):
            if count == "":
                count = 1
            else:
                count = int(count)
            if element_name in all_element:
                all_element[element_name] += count
            else:
                all_element[element_name] = count
        return all_element
