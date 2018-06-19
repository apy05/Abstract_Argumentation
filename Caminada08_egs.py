"""
Go through the examples of Caminada 2008 using the basic abstract argumentation engine
Paper: A Gentle Introduction to Argumentation Semantics by Martin Caminada, 2008
    
Coded by:
Anthony Peter Young
2018-06-19
Comments to peter.young@kcl.ac.uk
"""

execfile("basic_abs_arg.py")
print "Examples from Caminada 2008"
print

# p2 Figure 1
Cam_fig1 = Absargfw(nx.DiGraph([('c','b'),('b','a')]))
print "Figure 1"
print Cam_fig1.arguments()
print Cam_fig1.attacks()
print
print
print

# p4 Figure 2
Cam_fig2 = Absargfw(nx.DiGraph([('a','b'),('b','c'),('c','a')]))
print "Figure 2"
print Cam_fig2.arguments()
print Cam_fig2.attacks()
print
print
print

# p4 Figure 3
Cam_fig3 = Absargfw(nx.DiGraph([('a','b'),('b','a')]))
print "Figure 3"
print Cam_fig3.arguments()
print Cam_fig3.attacks()
print
print
print

# p5 Figure 4
Cam_fig4 = Absargfw(nx.DiGraph([('a','b'),('b','c'),('c','b'),('c','d')]))
print "Figure 4"
print Cam_fig4.arguments()
print Cam_fig4.attacks()
print
print "Exercise 2 (pp. 6-7). In Figure 4:"
print "Does {a} defend c?", 'c' in Cam_fig4.defence(set(['a']))
print "Does {c} defend c?", 'c' in Cam_fig4.defence(set(['c']))
print "Does {b} defend c?", 'c' in Cam_fig4.defence(set(['b']))
print
print "Exercise 4a (p7). Give all complete extensions of Figure 4"
print Cam_fig4.all_comp()
print
print "Exercise 5a (p8). Give the grounded extension of Figure 4"
print Cam_fig4.grounded()
print
print "Exercise 6a (p9). Is {a} admissible in Figure 4?", Cam_fig4.admissible(set(['a']))
print
print "Exercise 7a (p9). Give all preferred extensions of Figure 4"
print Cam_fig4.all_pref()
print
print "Exercise 8a (p10). Give all stable extensions of Figure 4"
print Cam_fig4.all_stab()
print
print "Exercise 9a (p11). Give all semi-stable extensions of Figure 4"
print Cam_fig4.all_semi_stab()
print
print
print

# p5 Figure 5
Cam_fig5 = Absargfw(nx.DiGraph([('a','b'),('b','c'),('c','d'),('d','c'),('d','e')]))
print "Figure 5"
print Cam_fig5.arguments()
print Cam_fig5.attacks()
print
print "Exercise 4b (p7). Give all complete extensions of Figure 5"
print Cam_fig5.all_comp()
print
print "Exercise 5b (p8). Give the grounded extension of Figure 5"
print Cam_fig5.grounded()
print
print "Exercise 6b (p9). Is {c} admissible in Figure 4?", Cam_fig5.admissible(set(['c']))
print
print "Exercise 7b (p9). Give all preferred extensions of Figure 5"
print Cam_fig5.all_pref()
print
print "Exercise 8b (p10). Give all stable extensions of Figure 5"
print Cam_fig5.all_stab()
print
print "Exercise 9b (p11). Give all semi-stable extensions of Figure 5"
print Cam_fig5.all_semi_stab()
print
print
print

# p5 Figure 6
Cam_fig6 = Absargfw(nx.DiGraph([('a','a'),('a','c'),('b','c'),('c','d')]))
print "Figure 6"
print Cam_fig6.arguments()
print Cam_fig6.attacks()
print
print "Exercise 4c (p7). Give all complete extensions of Figure 6"
print Cam_fig6.all_comp()
print
print "Exercise 5c (p8). Give the grounded extension of Figure 6"
print Cam_fig6.grounded()
print
print "Exercise 6c (p9). Is {a} admissible in Figure 6?", Cam_fig6.admissible(set(['a']))
print
print "Exercise 7c (p9). Give all preferred extensions of Figure 6"
print Cam_fig6.all_pref()
print
print "Exercise 8c (p10). Give all stable extensions of Figure 6"
print Cam_fig6.all_stab()
print
print "Exercise 9c (p11). Give all semi-stable extensions of Figure 6"
print Cam_fig6.all_semi_stab()
print
print
print

# Skip Exercise 1 (p5) as we are not dealing with labellings, but presumably it will be a list of dictionaries where the keys are nodes and the values are the possible labels

# p6 Figure 7
Cam_fig7 = Absargfw(nx.DiGraph([('a','b'),('b','a'),('b','c'),('c','d'),('d','e'),('e','c')]))
print "Figure 7"
print Cam_fig7.arguments()
print Cam_fig7.attacks()
print
print "Exercise 3 (p7). In Figure 7:"
print "F({a}) =", Cam_fig7.defence(set(['a']))
print "F({b}) =", Cam_fig7.defence(set(['b']))
print "F({b,d}) =", Cam_fig7.defence(set(['b','d']))
print
print "Exercise 4d (p7). Give all complete extensions of Figure 7"
print Cam_fig7.all_comp()
print
print "Exercise 5d (p8). Give the grounded extension of Figure 7"
print Cam_fig7.grounded()
print
print "Exercise 6d (p9). Is {a,c,d} admissible in Figure 7?", Cam_fig4.admissible(set(['a','c','d']))
print
print "Exercise 7d (p9). Give all preferred extensions of Figure 7"
print Cam_fig7.all_pref()
print
print "Exercise 8d (p10). Give all stable extensions of Figure 7"
print Cam_fig7.all_stab()
print
print "Exercise 9d (p11). Give all semi-stable extensions of Figure 7"
print Cam_fig7.all_semi_stab()
print
print
print

# p20 Figure 11
Cam_fig11 = Absargfw(nx.DiGraph([('a','b'),('b','a'),('a','c'),('b','c'),('c','d'),('d','e')]))
print "Figure 11"
print Cam_fig11.arguments()
print Cam_fig11.attacks()
print "The ideal extension is", Cam_fig11.ideal()
print
print
print

# p20 Figure 12
Cam_fig12 = Absargfw(nx.DiGraph([('a','a'),('a','b'),('b','a')]))
print "Figure 12"
print Cam_fig12.arguments()
print Cam_fig12.attacks()
print "The ideal extension is", Cam_fig12.ideal()
print
print
print

# Ignore CF2 semantics for now (Figure 13, p21)


