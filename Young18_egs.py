"""
Examples from
Notes on Abstract Argumentation Theory
Young, 2018
https://arxiv.org/abs/1806.07709

Coded by:
Anthony Peter Young
2018-06-21
Comments to peter.young@kcl.ac.uk
"""

execfile("basic_abs_arg.py")

print
nixon = Absargfw(nx.DiGraph([('a','b'),('b','a')]))
test_AF(nixon, "p4, Example 2.2 - Nixon diamond")

print
simple_reinstatement = Absargfw(nx.DiGraph([('c','b'),('b','a')]))
test_AF(simple_reinstatement, "p4-5, Example 2.3 - Simple Reinstatement")

print
double_reinstatement = Absargfw(nx.DiGraph([('b','a'),('c','b'),('e','b')]))
test_AF(double_reinstatement, "p5, Example 2.4 - Double Reinstatement")

print
eg2p5 = Absargfw(nx.DiGraph([('a','b'),('b','a'),('c','b')]))
test_AF(eg2p5, "p5, Example 2.5")

print
eg2p6 = Absargfw(nx.DiGraph([('e','c'),('c','b'),('b','a')]))
test_AF(eg2p6, "p5, Example 2.6")

print
fri = Absargfw(nx.DiGraph([('a','b'),('b','a'),('a','c'),('b','c'),('c','e')]))
test_AF(fri, "pp5-6, Example 2.7 - Floating Reinstatement")

print
print "p6, Example 2.10 - from Nixon Diamond"
print "b in {a}^+?", 'b' in nixon.set_plus(set(['a']))
print "a in {b}^+?", nixon.set_attacks(set(['b']), 'a')

print
print "p6, Example 2.11 - from Example 2.5"
print "c in {a,b}^-?", 'c' in eg2p5.set_minus(set(['a','b']))

print
print "p6, Example 2.12 - from Double Reinstatement"
print "{c,e} attacks {a,b}?", double_reinstatement.subset_attacks(set(['c','e']),set(['a','b']))

print
print "p7, Example 2.15 - from Example 2.6"
print "The set of unattacked arguments is", eg2p6.set_of_unattacked()

print
print "p7, Example 2.16 - from Floating Reinstatement"
print "The set of unattacked arguments is", fri.set_of_unattacked()

print
eg2p18 = Absargfw(nx.DiGraph([('a','a'),('a','b')]))
test_AF(eg2p18, "p7, Example 2.18")

print
eg2p33 = Absargfw(nx.DiGraph([('b','a'),('b','e'),('e','c'),('c','b')]))
test_AF(eg2p33, "p10, Example 2.36")

print
print "p12, Example 2.45 - from Example 2.6"
print "Does e indirectly attack a?", eg2p6.indirectly_attacks('e','a')

print
print "Example 2.48 - from Example 2.2"
print "Does b indirectly defend b (itself)?", nixon.indirectly_defends('b','b')

print
eg2p52 = Absargfw(nx.DiGraph([('a','b'),('b','c'),('a','c')]))
test_AF(eg2p52, "pp12-13, Example 2.52")
print "Is a controversial w.r.t. c?", eg2p52.controversial_arguments('a','c')

print
print "p16, Example 3.3 - neutrality function for simple reinstatement"
for subset in powerlist(simple_reinstatement.arguments()):
    print subset, simple_reinstatement.neutrality(subset)

print
print "p23, Example 6.2 - simple reinstatement"
print "Does {c} reinstate a?", 'a' in simple_reinstatement.defence(set(['c']))

print
print "p23, Example 6.3 - double reinstatement"
print "Does {c,e} reinstate a?", 'a' in double_reinstatement.defence(set(['c','e']))

print
print "p23, Example 6.7 - simple reinstatement"
for subset in powerlist(simple_reinstatement.arguments()):
    print subset, simple_reinstatement.defence(subset)

print
eg6p8 = Absargfw(nx.DiGraph([('a','a'),('a','b'),('b','a')]))
test_AF(eg6p8, "p23, Example 6.8")

print
print "p23, Example 6.8 - values of defence function"
for subset in powerlist(eg6p8.arguments()):
    print subset, eg6p8.defence(subset)

print
eg9p4 = Absargfw(nx.DiGraph([('a','b'),('c','b'),('c','f'),('f','c'),('f','e'),('e','e')]))
test_AF(eg9p4, "p33, Example 9.4")

print
thm15p8 = Absargfw(nx.DiGraph([('e','a'),('a','b'),('b','c'),('c','a')]))
test_AF(thm15p8, "Converse to Theorem 15.8, pp54-55")

