"""
Book: Elements of Argumentation by Philippe Besnard and Anthony Hunter, 2008, MIT Press
Using the basic abstract argumentation engine to check through the examples of chapter 2

Coded by:
Anthony Peter Young
2018-06-19
Comments to peter.young@kcl.ac.uk
"""

execfile("basic_abs_arg.py")
print "Examples from Elements of Argumentation (Besnard, Hunter, 2008), Chapter 2"
print

# Figure 2.1, p22
BHC2_fig2p1 = Absargfw(nx.DiGraph([('d','d'),('c','d'),('c','b'),('b','c'),('b','a'),('c','a')]))
print "Figure 2.1, p22"
print BHC2_fig2p1.arguments()
print BHC2_fig2p1.attacks()
print

# Example 2.1.1, p22
BHC2_eg2p1p1 = Absargfw(nx.DiGraph([('b','a')]))
print "Example 2.1.1, p22"
print BHC2_eg2p1p1.arguments()
print BHC2_eg2p1p1.attacks()
print

# Example 2.1.2, p23
BHC2_eg2p1p2 = Absargfw(nx.DiGraph([('b','a'),('c','a'),('c','b')]))
print "Example 2.1.2, p23"
print BHC2_eg2p1p2.arguments()
print BHC2_eg2p1p2.attacks()
print

# Example 2.1.3, p23
BHC2_eg2p1p3 = Absargfw(nx.DiGraph([('b','a'),('a','b')]))
print "Example 2.1.3, p23"
print BHC2_eg2p1p3.arguments()
print BHC2_eg2p1p3.attacks()
print

# Example 2.2.1, p25
BHC2_eg2p2p1 = Absargfw(nx.DiGraph([('a','b'),('c','b'),('c','d'),('d','c'),('d','e'),('e','e')]))
print "Example 2.2.1, p25"
print BHC2_eg2p2p1.arguments()
print BHC2_eg2p2p1.attacks()
print "The set of admissible sets is"
print BHC2_eg2p2p1.all_adm()
print

# Example 2.2.2, p25
print "Example 2.2.2, p25"
print "Same AF as in Example 2.2.1, p25"
print "The set of complete extensions is"
print BHC2_eg2p2p1.all_comp()
print

# Example 2.2.3, p26 (also Example 2.3.2, p28)
print "Example 2.2.3, p26 (also Example 2.3.2, p28)"
print "Same AF as in Example 2.2.1, p25"
print "The set of preferred extensions is"
print BHC2_eg2p2p1.all_pref()
print

# Paragraph just after Example 2.2.3
print "Now add arguments f, g, h, i and attacks (f,g), (g,h), (h,i), (i,f) to the AF in Example 2.2.1, p25"
BHC2_eg2p2p3 = Absargfw(nx.DiGraph([('a','b'),('c','b'),('c','d'),('d','c'),('d','e'),('e','e'),('f','g'),('g','h'),('h','i'),('i','f')]))
print "The set of preferred extensions is (takes a longer time)"
print BHC2_eg2p2p3.all_pref()
print

# Example 2.2.4, pp26-7
print "Example 2.2.4, pp26-7"
print "Same AF as in Example 2.2.1, p25"
print "The set of stable extensions is"
print BHC2_eg2p2p1.all_stab()
print

# Example 2.2.5, p27
print "Example 2.2.5, p27"
BHC2_eg2p2p5 = Absargfw(nx.DiGraph([('a','b'),('d','d'),('d','c')]))
print BHC2_eg2p2p5.arguments()
print BHC2_eg2p2p5.attacks()
print "The set of stable extensions is"
print BHC2_eg2p2p5.all_stab()
print

# Example 2.3.1, p27
print "Example 2.3.1, p27"
BHC2_eg2p3p1 = Absargfw(nx.DiGraph([('b','a'),('c','b'),('d','c'),('b','d')]))
print BHC2_eg2p3p1.arguments()
print BHC2_eg2p3p1.attacks()
print

# Figure 2.2, p28
print "Figure 2.2, p28"
print
print "The left AF is"
BHC2_fig2p2a = Absargfw(nx.DiGraph([('a','b'),('b','a')]))
print BHC2_fig2p2a.arguments()
print BHC2_fig2p2a.attacks()
print "The cycles are"
print BHC2_fig2p2a.cycles()
print
print "The right AF is"
BHC2_fig2p2b = Absargfw(nx.DiGraph([('a','c'),('c','b'),('b','a')]))
print BHC2_fig2p2b.arguments()
print BHC2_fig2p2b.attacks()
print "The cycles are"
print BHC2_fig2p2b.cycles()
print

# Example 2.3.3, p29
print "Example 2.3.3, p29"
print "Same AF as in Example 2.2.5, p27"
print "The set of preferred extensions is"
print BHC2_eg2p2p5.all_pref()
print

# Example 2.3.4, p29
print "Example 2.3.4, p29"
BHC2_eg2p3p4 = Absargfw(nx.DiGraph([('a','b'),('b','a'),('a','c'),('c','a'),('c','b'),('b','c')]))
print BHC2_eg2p3p4.arguments()
print BHC2_eg2p3p4.attacks()
print "The set of preferred extensions is"
print BHC2_eg2p3p4.all_pref()
print "The set of stable extensions is"
print BHC2_eg2p3p4.all_stab()
print

# Figure 2.3, p29
print "Figure 2.3, p29"
print
BHC2_fig2p3a = Absargfw(nx.DiGraph([('a','c'),('c','b'),('b','a')]))
print "The left AF is"
print BHC2_fig2p3a.arguments()
print BHC2_fig2p3a.attacks()
print "Its set of preferred extensions is"
print BHC2_fig2p3a.all_pref()
print
BHC2_fig2p3b = Absargfw(nx.DiGraph([('a','a'),('a','b')]))
print "The right AF is"
print BHC2_fig2p3b.arguments()
print BHC2_fig2p3b.attacks()
print "Its set of preferred extensions is"
print BHC2_fig2p3b.all_pref()
print

# Example 2.3.5, p30
print "Example 2.3.5, p30"
BHC2_eg2p3p5 = Absargfw(nx.DiGraph([('d','c'),('c','b'),('b','a')]))
print BHC2_eg2p3p5.arguments()
print BHC2_eg2p3p5.attacks()
print "The set of stable extensions is"
print BHC2_eg2p3p5.all_stab()
print "The set of preferred extensions is"
print BHC2_eg2p3p5.all_pref()
print "The set of complete extensions is"
print BHC2_eg2p3p5.all_comp()
print "The grounded extension is"
print BHC2_eg2p3p5.grounded()
print

# Example 2.3.6, p30
print "Example 2.3.6, p30"
BHC2_eg2p3p6 = Absargfw(nx.DiGraph([('a','b'),('c','b'),('c','d'),('d','c'),('d','e')]))
print BHC2_eg2p3p6.arguments()
print BHC2_eg2p3p6.attacks()
print "The set of preferred extensions is"
print BHC2_eg2p3p6.all_pref()
print "The set of stable extensions is"
print BHC2_eg2p3p6.all_stab()
print

# Example 2.4.1, p31
print "Example 2.4.1, p31"
print "Same AF as in Example 2.3.5, p30"
print "Iterate its defence function starting from the empty set, until termination"
print BHC2_eg2p3p5.iterate_defence(set())
print

# Example 2.4.2, p31
print "Example 2.4.2, p31"
print "Same AF as in Example 2.2.1, p25"
print "The grounded extension is"
print BHC2_eg2p2p1.grounded()
print
