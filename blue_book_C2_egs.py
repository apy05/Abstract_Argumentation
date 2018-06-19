"""
Book: Argumentation in Artificial Intelligence, Rahwan and Simari (eds.), Springer 2009
Chapter: Semantics of Abstract Argumentation Systems by Baroni and Giacomin

Coded by:
Anthony Peter Young
2018-06-19
Comments to peter.young@kcl.ac.uk
"""

execfile("basic_abs_arg.py")
print "Examples from Semantics of Abstract Argumentation Systems by Baroni and Giacomin, 2009"
print

# Figure 2.1, p25
BG_fig2p1 = Absargfw(nx.DiGraph([('b','a')]))
print "Figure 2.1, p25"
print BG_fig2p1.arguments()
print BG_fig2p1.attacks()
print "(p35) Its complete extension is", BG_fig2p1.all_comp()
print "(p37) Its stable extension is", BG_fig2p1.all_stab()
print "(p38) Its preferred extension is", BG_fig2p1.all_pref()
print

# Figure 2.2, p27
BG_fig2p2 = Absargfw(nx.DiGraph([('b','a'),('a','b')]))
print "Figure 2.2, p27"
print BG_fig2p2.arguments()
print BG_fig2p2.attacks()
print "(p28) Its naive extesions are", BG_fig2p2.all_naive()
print "(p28) The set of unattacked arguments is", BG_fig2p2.set_of_unattacked()
print "(p35) Its complete extensions are", BG_fig2p2.all_comp()
print "(p37) Its stable extensions are", BG_fig2p2.all_stab()
print "(p38) Its preferred extensions are", BG_fig2p2.all_pref()
print

# Figure 2.3, p27
BG_fig2p3 = Absargfw(nx.DiGraph({'a':set(), 'b':set(['a']), 'c':set()}))
print "Figure 2.3, p27"
print BG_fig2p3.arguments()
print BG_fig2p3.attacks()
print "(p35) Its complete extension is", BG_fig2p3.all_comp()
print "(p37) Its stable extension is", BG_fig2p3.all_stab()
print "(p38) Its preferred extension is", BG_fig2p3.all_pref()
print

# Figure 2.4, p30
BG_fig2p4 = Absargfw(nx.DiGraph([('b','c'),('b','a'),('a','b')]))
print "Figure 2.4, p30"
print BG_fig2p4.arguments()
print BG_fig2p4.attacks()
print "(p30) Its admissible sets are", BG_fig2p4.all_adm()
print "(p35) Its complete extensions are", BG_fig2p4.all_comp()
print "(p37) Its stable extensions are", BG_fig2p4.all_stab()
print "(p38) Its preferred extensions are", BG_fig2p4.all_pref()
print

# Figure 2.5, p35
BG_fig2p5 = Absargfw(nx.DiGraph([('d','c'),('c','d'),('b','c'),('b','a'),('a','b')]))
print "Figure 2.5, p35"
print BG_fig2p5.arguments()
print BG_fig2p5.attacks()
print "(p35) The set of unattacked arguments is", BG_fig2p5.set_of_unattacked()
print "(p35) The set of admissible sets is", BG_fig2p5.all_adm()
print "(p35) The set of complete extensions is", BG_fig2p5.all_comp()
print "(p37) Its stable extensions are", BG_fig2p5.all_stab()
print "(p38) Its preferred extensions are", BG_fig2p5.all_pref()
print

# Figure 2.6, p36
BG_fig2p6 = Absargfw(nx.DiGraph([('a','b'),('b','c'),('c','d'),('d','e'),('e','f'),('f','e')]))
print "Figure 2.6, p36"
print BG_fig2p6.arguments()
print BG_fig2p6.attacks()
print "(p36) The iteration of the defence function is", BG_fig2p6.iterate_defence(set())
print "(p36) The grounded extension is", BG_fig2p6.grounded()
print "(p37) Its stable extensions are", BG_fig2p6.all_stab()
print "(p38) Its preferred extensions are", BG_fig2p6.all_pref()
print

# Figure 2.7, p37
BG_fig2p7 = Absargfw(nx.DiGraph([('a','b'),('b','c'),('c','a')]))
print "Figure 2.7, p37"
print BG_fig2p7.arguments()
print BG_fig2p7.attacks()
print "(p37) Its stable extensions are", BG_fig2p7.all_stab()
print "(p38) Its preferred extension is", BG_fig2p7.all_pref()
print "(p39) Its semi-stable extension is", BG_fig2p7.all_semi_stab()
print "(p39) Its stage extensions are", BG_fig2p7.all_stage()
print

# Figure 2.8, p38
BG_fig2p8 = Absargfw(nx.DiGraph([('c','c'),('b','c'),('b','a'),('a','b')]))
print "Figure 2.8, p38"
print BG_fig2p8.arguments()
print BG_fig2p8.attacks()
print "(p37) Its stable extension is", BG_fig2p8.all_stab()
print "(p38) Its preferred extensions are", BG_fig2p8.all_pref()
print

# Figure 2.9, p39
BG_fig2p9 = Absargfw(nx.DiGraph({'a':set(['b']),'b':set(['a','c']),'c':set(['c']),'d':set(['d'])}))
print "Figure 2.9, p39"
print BG_fig2p9.arguments()
print BG_fig2p9.attacks()
print "(p39) Its stable extensions are", BG_fig2p9.all_stab()
print "(p39) Its preferred extensions are", BG_fig2p9.all_pref()
print "(p39) Its semi-stable extension is", BG_fig2p9.all_semi_stab()
print "(p39) Its stage extension is", BG_fig2p9.all_stage()
print

# Figure 2.10, p40
BG_fig2p10 = Absargfw(nx.DiGraph([('a','b'),('b','a'),('a','c'),('b','c'),('c','d'),('d','c')]))
print "Figure 2.10, p40"
print BG_fig2p10.arguments()
print BG_fig2p10.attacks()
print "(p39) Its preferred extensions are", BG_fig2p10.all_pref()
print "(p39) Its grounded extension is", BG_fig2p10.grounded()
print "(p39) Its ideal extension is", BG_fig2p10.ideal()

# Omit CF2 semantics (Section 5.7) and prudent semantics (Section 5.8)
