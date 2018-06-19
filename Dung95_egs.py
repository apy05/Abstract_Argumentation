"""
Go through the examples of Dung 1995 Section 2 using the basic abstract argumentation engine
Paper: On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games by Phan Minh Dung, Artificial Intelligence, 1995

Coded by:
Anthony Peter Young
2018-06-19
Comments to peter.young@kcl.ac.uk
"""

execfile("basic_abs_arg.py")
print "Examples from Dung 1995"
print

# p326 Example 3
eg3AF = Absargfw(nx.DiGraph([("i1","a"),("a","i1"),("i2","a")]))
print "The AF from Example 3"
print eg3AF.arguments()
print eg3AF.attacks()
print

# p327 Example 8
print "The preferred extension of the AF from Example 3 is"
print eg3AF.all_pref()[0]
print

# p327 Example 9
eg9AF = Absargfw(nx.DiGraph([('a','b'),('b','a')]))
print "The AF from Example 9"
print eg9AF.arguments()
print eg9AF.attacks()
print "Its set of preferred extensions is:"
print eg9AF.all_pref()
print

# p329 Example 21
print "Iterating d from the empty set of the AF from Example 3 until stabilisation:"
print eg3AF.iterate_defence(set())
print

# p329 Example 22
print "The grounded extension of the AF from Example 9 is"
print eg9AF.grounded()
print

# p330 Theorem 25(1)
print "The set of complete extensions of the AF from Example 9 is:"
print eg9AF.all_comp()
print "Note that empty set is complete and not preferred"
print

# p331 Coherent AFs
print "The singleton self-attacking AF is:"
self_attack = Absargfw(nx.DiGraph([('a','a')]))
print self_attack.arguments()
print self_attack.attacks()
print "The set of preferred extensions is"
print self_attack.all_pref()
print "The set of stable extensions is"
print self_attack.all_stab()
print "i.e. there are no stable extensions!"
print "Notice the empty set is preferred but not stable"
print
