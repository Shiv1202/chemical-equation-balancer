from random import randint
from math import gcd
from functools import reduce
import molecule_parser as per

p = per.MoleculeParser()



class Equation:

    """
    A chemical equation.
    ===== Attributes =====
    @type left: list[dict]
    @type right: list[dict]
    """

    def __init__(self, equation):

        """
        Intializes an Equation object.

        @type self: Equation
        @type equation: str
        @rtype: None
        """
        self.left = list()
        self.right = list()
        self.is_balanced = True

        split = equation.split("=>")
        left = split[0]
        right = split[1]

        left_components = left.split("+")
        right_components = right.split("+")

        left_components = [i.strip() for i in left_components]
        right_components = [i.strip() for i in right_components]

        total_left = dict()
        total_right = dict()

        for component in left_components:

            left_counts = p.parse(component)
            
            for element, value in left_counts.items():
                if element in total_left:
                    total_left[element] += value
                else:
                    total_left[element] = value
            self.left.append(left_counts)

        for component in right_components:
            
            right_counts = p.parse(component)

            for element, value in right_counts.items():
                if element in total_right:
                    total_right[element] += value
                else:
                    total_right[element] = value
            self.right.append(right_counts)


        for key in total_left:
            if total_left[key] != total_right[key]:
                self.balanced = False
            else:
                continue


    def equation_balancer(self):
        """
        This is going to balance the Equations.

        @type self: Equation
        @rtype: str
        """

        if self.balanced:
            string = str()
            for dictionary in self.left:
                compound = str()
                for key in dictionary:
                    compound += key
                    compound += str(dictionary[key])
                string += compound
                string += " + "
            string = string[:len(string) - 3] + " => "

            for dictionary in self.right:
                compound = str()
                for key in dictionary:
                    compound += key
                    compound += str(dictionary[key])
                string += compound
                string += " + "
            string = string[:len(string) - 2]
            return string
        else:
            while not self.balanced:
                temp_left = list()
                temp_right = list()
                total_left = dict()
                total_right = dict()

                for item in self.left:
                    new_dict = dict()
                    for key in item:
                        new_dict[key] = item[key]
                    temp_left.append(new_dict)

                for item in self.right:
                    new_dict = dict()
                    for key in item:
                        new_dict[key] = item[key]
                    temp_right.append(new_dict)

                left_coff = [randint(1, 10) for _ in range(len(temp_left))]
                right_coff = [randint(1, 10) for _ in range(len(temp_right))]

                for index in range(0, len(left_coff)):
                    for key in temp_left[index]:
                        temp_left[index][key] *= left_coff[index]
                        if key not in total_left:
                            total_left[key] = temp_left[index][key]
                        else:
                            total_left[key] += temp_left[index][key]

                for index in range(0, len(right_coff)):
                    for key in temp_right[index]:
                        temp_right[index][key] *= right_coff[index]
                        if key not in total_right:
                            total_right[key] = temp_right[index][key]
                        else:
                            total_right[key] += temp_right[index][key]

                self.balanced = True
                for key in total_left:
                    if total_left[key] != total_right[key]:
                        self.balanced = False
                    else:
                        continue

            big_tuple = tuple(left_coff + right_coff)
            left_coff = list(map(lambda x: int(x / reduce(gcd, big_tuple)), left_coff))
            right_coff = list(map(lambda x: int(x / reduce(gcd, big_tuple)), right_coff))

            string = str()
            for index in range(0, len(self.left)):
                if left_coff[index] != 1:
                    compound = str(left_coff[index])
                else:
                    compound = str()
                for key in self.left[index]:
                    compound += key
                    if self.left[index][key] != 1:
                        compound += str(self.left[index][key])
                    else:
                        continue
                string += compound
                string += " + "
            string = string[:len(string) - 3] + " => "
            compound = ""
            for index in range(0, len(self.right)):
                if right_coff[index] != 1:
                    compound += str(right_coff[index])
                else:
                    compound = str()
                for key in self.right[index]:
                    compound += key
                    if self.right[index][key] != 1:
                        compound += str(self.right[index][key])
                    else:
                        continue
                string += compound
                string += " + "
            string = string[:len(string) - 2]
            return string


# obj = Equation()
# print(f"\t {obj.left}")
# print(f"\t {obj.right}")