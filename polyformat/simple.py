class SimplePolynomFormatter:

    superscript_numbers = [u"\u2070", u"\u00B9", u"\u00B2", u"\u00B3",
                           u"\u2074", u"\u2075", u"\u2076", u"\u2077",
                           u"\u2078", u"\u2079"]

    def __init__(self, polynom, varname="x"):
        self.varname = varname
        self.polynom = polynom

    def num_to_superscript(self, num):
        if num in (0, 1):
            return ""

        result = []
        for digit in str(num):
            result.append(self.superscript_numbers[int(digit)])

        return "".join(result)

    def format_coefficient(self, coefficient):

        if coefficient.is_integer():
            if int(coefficient) == 1:
                return "+"
            else:
                return "+%s" % int(coefficient)

        return "+%f" % coefficient

    def __unicode__(self):
        elements = []
        current_degree = self.polynom.degree()

        for coefficient in self.polynom:
            if not coefficient == 0:
                elements.append(
                    "%s%s%s" % (
                        self.format_coefficient(coefficient),
                        self.varname if current_degree > 0 else "",
                        self.num_to_superscript(current_degree)
                    )
                )

            current_degree -= 1

        result = unicode("".join(elements))
        if (result[0] == "+"):
            return result[1:]

        return result
