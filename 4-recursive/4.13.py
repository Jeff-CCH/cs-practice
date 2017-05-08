"""

In Section 4.2 we prove by induction that the number of lines printed by a call to draw interval(c) is 2^c - 1. Another interesting question is how many dashes are printed during that process. Prove by induction that the number of dashes printed by draw interval(c) is 2^(c+1) - c -2
"""

Prove: interval(c) = 2^(c+1) - c -2
Justification:
    We know that the number of dash for interval(c) = 2*interval(c-1) + c - 1. By induction, we can say that interval(c-1) = 2^(c) - (c-1) - 2 = 2^c - c - 1
    That is, interval(c) = 2*(2^c - c - 1) + c - 1
                         = 2^(c+1) - 2c - 2 + c - 1
                         = 2^(c+1) - c - 3??
