"""
Basic Abstract Argumentation Engine
Anthony Peter Young
2018-06-19
Comments to peter.young@kcl.ac.uk

This is a basic (non-scalable) implementation of an abstract argumentation engine
The definitions and properties are those of Dung 1995 Section 2
It is implemented for me to check examples that I read in the literature
Also it is a test of my understanding of the concepts
The engine is not scalable and hence nowhere near as good as scalable argumentation engines, e.g. http://argumentationcompetition.org/2017/
Can do argumentation frameworks of up to size (around) 12 well (at least on my Macbook Air...)

FUTURE WORK:
Visualisation of AFs, colour in extensions: green for in, red for out, grey for und
"""

# Python modules
import time
import random
from tqdm import tqdm # progress bars

"""
Helper functions
"""

# returns the list of all subsets of a given set - this is the slowest step!
def powerlist(myset):
    """
        Given a set input myset, generate the list of subsets of this set
        Recall that in Python you cannot (yet) have sets of sets
        EXP time!
        N.B. Cannot have sets of sets in Python, so compromise with list of sets
        """
    # the power set of the empty set has one element, the empty set itself
    result = [[]]
    for element in myset:
        # for every additional element in myset
        # the power set consists of the subsets that do not contain this element
        # plus the subsets that do contain this element
        # this is achieved with list comprehension to add x to everything in the previous power set
        result.extend([sublist + [element] for sublist in result])
    answer = []
    for sublist in result:
        # not sure whether to use frozenset or set
        answer.append(frozenset(sublist))
    return answer

# [S1, S2, ..., Sn] --> max [S1, S2, ..., Sn]
def find_max_sets(mylist):
    """
    Input: a list of sets
    Output: the list of subset-maximal sets of that list
    But there is a more efficient implementation:
    https://stackoverflow.com/questions/14106121/efficient-algorithm-for-finding-all-maximal-subsets
    """
    non_max_sets = []
    for myset in mylist:
        for other_set in mylist:
            if myset.issubset(other_set) and myset != other_set:
                non_max_sets.append(myset)
    answer = [item for item in mylist if item not in non_max_sets]
    return answer

# [S1, S2, ..., Sn] --> min [S1, S2, ..., Sn]
def find_min_sets(mylist):
    """
    Input: a list of sets
    Output: the list of minimal sets of that list (dual of the previous)
    """
    non_min_sets = []
    for myset in mylist:
        for other_set in mylist:
            if other_set.issubset(myset) and myset != other_set:
                non_min_sets.append(myset)
    answer = [item for item in mylist if item not in non_min_sets]
    return answer

"""
Abstract argumentation frameworks
"""

# Abstract argumentation frameworks are based on directed graphs
import networkx as nx

# Write an inherited class implementing abstract argumentation frameworks
class Absargfw:

    # Derived class from networkx directed graphs, nodes cannot be sets
    def __init__(self, nxdigraph):
        self.data = nxdigraph

    # List all arguments (nodes)
    def arguments(self):
        return list(self.data.nodes())

    # List all attacks (edges)
    def attacks(self):
        return list(self.data.edges())

    # Number of arguments (finite!)
    def number_of_arguments(self):
        return self.data.number_of_nodes()

    # Number of attacks
    def number_of_attacks(self):
        return self.data.number_of_edges()

    # Forward set, i.e. S --> S^+
    def set_plus(self, subset):
        if not subset.issubset(self.arguments()):
            return "invalid subset of arguments"
        answer = frozenset()
        for argument in subset:
            forward_set = set(self.data.successors(argument))
            answer = answer.union(forward_set)
        return answer

    # Set attacks, i.e. does S --> a ?
    def set_attacks(self, subset, argument):
        if not subset.issubset(self.arguments()):
            return "invalid subset of arguments"
        elif not argument in self.arguments():
            return "invalid argument"
        return argument in self.set_plus(subset)

    # Backward set, i.e. S --> S^-
    def set_minus(self, subset):
        if not subset.issubset(self.arguments()):
            return "invalid subset of arguments"
        answer = frozenset()
        for argument in subset:
            backward_set = set(self.data.predecessors(argument))
            answer = answer.union(backward_set)
        return answer

    # Sets attacking each other
    def subset_attacks(self, set1, set2):
        if not set1.issubset(self.arguments()) or not set2.issubset(self.arguments()):
            return "invalid subset of arguments"
        set1_plus = self.set_plus(set1)
        answer = set1_plus.intersection(set2)
        if len(answer) > 0:
            return True
        else:
            return False

    # Unattacked arguments, i.e. is a unattacked?
    def unattacked(self, argument):
        if not argument in self.arguments():
            return "invalid argument"
        return len(self.set_minus(set([argument]))) == 0
    
    # Set of unattacked arguments
    def set_of_unattacked(self):
        answer = set()
        for argument in self.arguments():
            if self.unattacked(argument):
                answer.add(argument)
        return answer

    # Self attacking arguments, i.e. does a --> a?
    def self_attacking(self, argument):
        if not argument in self.arguments():
            return "invalid argument"
        return argument in self.set_plus(set([argument]))
    
    # Return all self-attacking arguments
    def set_of_self_attacking(self):
        answer = set()
        for argument in self.arguments():
            if self.self_attacking(argument):
                answer.add(argument)
        return answer

    # Is the AF empty?
    def empty(self):
        return self.number_of_arguments() == 0

    # Is the AF trivial?
    def trivial(self):
        return self.number_of_attacks() == 0

    # Induced subframework
    def subframework(self, subset):
        """
        https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.Graph.subgraph.html
        """
        if not subset.issubset(self.arguments()):
            return "invalid subset of arguments"
        answer = Absargfw(self.data.subgraph(subset))
        return answer

    # Lists all simple cycles
    def cycles(self):
        """
        https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.cycles.simple_cycles.html#networkx.algorithms.cycles.simple_cycles
        """
        return list(nx.simple_cycles(self.data))

    # Cyclic?
    def cyclic(self):
        return len(self.cycles()) > 0

    # List attack paths from arg1 to arg2, paths are a list of nodes
    def attack_paths(self, arg1, arg2):
        if arg1 not in self.arguments() or arg2 not in self.arguments():
            return "invalid arguments"
        paths = nx.all_simple_paths(self.data, source = arg1, target = arg2)
        answer = list(paths)
        return answer

    # Indirectly attacks, i.e. exists odd-length attack path
    # As paths are a list of nodes, path lengths are the length - 1 (counting edges)
    def indirectly_attacks(self, arg1, arg2):
        paths = self.attack_paths(arg1, arg2)
        for path in paths:
            if (len(path) - 1) % 2 == 1:
                return True
        return False

    # Indirectly defends, i.e. exists even-length attack path
    def indirectly_defends(self, arg1, arg2):
        if arg1 == arg2:
            return True
        paths = self.attack_paths(arg1, arg2)
        for path in paths:
            if (len(path) - 1) % 2 == 0:
                return True
        return False

    # Is arg1 controversial w.r.t. arg2?
    def controversial_arguments(self, arg1, arg2):
        if self.indirectly_attacks(arg1, arg2) and self.indirectly_defends(arg1, arg2):
            return True
        return False

    # Is arg1 a controversial argument?
    def controversial_argument(self, arg1):
        for arg2 in self.arguments():
            if self.controversial_arguments(arg1, arg2):
                return True
        return False

    # Is the AF controversial?
    def controversial(self):
        for arg in self.arguments():
            if self.controversial_argument(arg):
                return True
        return False

    # Is the AF limited controversial?
    def limited_controversial(self):
        # use the result: finite AFs with no odd cycles are limited controversial
        all_cycles = self.cycles()
        # search through all cycles
        for cycle in all_cycles:
            # If there is an odd cycle
            if len(cycle) % 2 == 1:
                # Then the AF is not limited controversial
                return False
        # If you cannot find an odd cycle then it is limited controversial
        return True

    # Neutrality function, S --> n(S)
    def neutrality(self, subset):
        if not subset.issubset(self.arguments()):
            return "invalid subset of arguments"
        # Calculate S^+
        attackers = self.set_plus(subset)
        # Calculate A - S^+ = n(S)
        answerlist = [arg for arg in self.arguments() if arg not in attackers]
        answer = frozenset(answerlist)
        return answer

    # Test whether S is conflict free
    def conflict_free(self, subset):
        if not subset.issubset(self.arguments()):
            return "invalid subset of arguments"
        return subset.issubset(self.neutrality(subset))
    
    # List all conflict free sets, uses powerset
    def all_cf(self):
        all_subsets = powerlist(self.arguments())
        answer = []
        for subset in all_subsets:
            if self.conflict_free(subset):
                answer.append(subset)
        return answer

    # List all naive extensions
    def all_naive(self):
        return find_max_sets(self.all_cf())

    # Test whether S is a naive extension
    def naive(self, subset):
        if not subset.issubset(self.arguments()):
            return "invalid subset of arguments"
        return subset in self.all_naive()

    # Defence function, S --> d(S)
    def defence(self, subset):
        if not subset.issubset(self.arguments()):
            return "invalid subset of arguments"
        attackers = self.set_plus(subset)
        answer = set()
        for argument in self.arguments():
            backwards = self.set_minus(set([argument]))
            if backwards.issubset(attackers):
                answer.add(argument)
        return answer

    # Fixed points of d, uses powerset
    def list_fp_of_d(self):
        answer = []
        for subset in powerlist(self.arguments()):
            if self.defence(subset) == subset:
                answer.append(subset)
        return answer

    # Least fixed point of d, know it is unique, uses powerset
    def lfpd(self):
        return find_min_sets(self.list_fp_of_d())[0]

    # Test whether S is self defending
    def self_defending(self, subset):
        if not subset.issubset(self.arguments()):
            return "invalid subset of arguments"
        return subset.issubset(self.defence(subset))
    
    # List all self defending sets, uses powerset
    def all_sd(self):
        all_subsets = powerlist(self.arguments())
        answer = []
        for subset in all_subsets:
            if self.self_defending(subset):
                answer.append(subset)
        return answer
    
    # List all admissible sets, uses powerset
    def all_adm(self):
        answer = [argset for argset in self.all_cf() if argset in self.all_sd()]
        return answer

    # Test whether S is admissible
    def admissible(self, subset):
        if not subset.issubset(self.arguments()):
            return "invalid subset of arguments"
        return subset in self.all_adm()

    # List all complete extensions, uses powerset
    def all_comp(self):
        answer = [argset for argset in self.all_adm() if argset in self.list_fp_of_d()]
        return answer

    # List all preferred extensions
    def all_pref(self):
        adm = self.all_adm()
        return find_max_sets(adm)
    
    # Test whether S is preferred
    def preferred(self, subset):
        if not subset.issubset(self.arguments()):
            return "invalid subset of arguments"
        return subset in self.all_pref()

    # Stable extension, i.e. is S stable?
    def stable(self, subset):
        if not subset.issubset(self.arguments()):
            return "invalid subset of arguments"
        return subset == self.neutrality(subset)
    
    # List all stable extensions
    def all_stab(self):
        all_subsets = powerlist(self.arguments())
        answer = []
        for subset in all_subsets:
            if self.stable(subset):
                answer.append(subset)
        return answer
    
    # Does a stable extension exist? Note in the finite AF case, all other extension types exist
    def stable_exists(self):
        return len(self.all_stab()) > 0

    # Return the grounded extension, as least complete extension
    def grounded(self):
        return find_min_sets(self.all_comp())[0]

    # Iterate defence function S, d(S), d^2(S), ... until stabilisation
    def iterate_defence(self, subset):
        if not subset.issubset(self.arguments()):
            return "invalid subset of arguments"
        answer = [subset]
        for iteration in range(self.number_of_arguments()):
            # Must have the last set already iterated
            current_set = answer[-1]
            current_set = self.defence(current_set)
            if current_set not in answer:
                answer.append(current_set)
        return answer

    # Is the AF coherent? Know that STAB is a subset of PREF already
    def coherent(self):
        PREF = set(self.all_pref())
        STAB = set(self.all_stab())
        return PREF.issubset(STAB)

    # Is the AF relatively grounded?
    def relatively_grounded(self):
        PREF = set(self.all_pref())
        skep_PREF = frozenset.intersection(*PREF)
        return skep_PREF == self.grounded()

    """
    Now begins a selection of the other non-Dung semantics
    """

    # Range, i.e. S --> S U S^+ = OK
    def set_range(self, subset):
        if not subset.issubset(self.arguments()):
            return "invalid subset of arguments"
        return subset.union(self.set_plus(subset))

    # List all semi-stable extensions
    def all_semi_stab(self):
        set_range_list = []
        for complete_extension in self.all_comp():
            data = (complete_extension, self.set_range(complete_extension))
            set_range_list.append(data)
        range_list = []
        for item in set_range_list:
            range_list.append(item[1])
        max_range = find_max_sets(range_list)
        answer = []
        for item in max_range:
            for pair in set_range_list:
                if pair[1] == item:
                    if pair[0] not in answer:
                        answer.append(pair[0])
        return answer

    # Test whether S is semi-stable
    def semi_stable(self, subset):
        if not subset.issubset(self.arguments()):
            return "invalid subset of arguments"
        return subset in self.all_semi_stab()

    # List all stage extensions
    def all_stage(self):
        set_range_list = []
        for cf_set in self.all_cf():
            data = (cf_set, self.set_range(cf_set))
            set_range_list.append(data)
        range_list = []
        for item in set_range_list:
            range_list.append(item[1])
        max_range = find_max_sets(range_list)
        answer = []
        for item in max_range:
            for pair in set_range_list:
                if pair[1] == item:
                    if pair[0] not in answer:
                        answer.append(pair[0])
        return answer

    # Test whether S is a stage extension
    def stage(self, subset):
        if not subset.issubset(self.arguments()):
            return "invalid subset of arguments"
        return subset in self.all_stage()

    # Return the ideal extension (always unique)
    def ideal(self):
        """
        The largest admissible set contained in all preferred extensions
        """
        ADM = self.all_adm()
        PREF = self.all_pref()
        inter = frozenset.intersection(*PREF)
        bddADM = [S for S in ADM if S.issubset(inter)]
        answer = find_max_sets(bddADM)
        return answer[0]

    # Return the eager extension (unique for finite and finitary)
    def eager(self):
        """
        The largest admissible set contained in all semi-stable extensions
        """
        ADM = self.all_adm()
        SSTAB = self.all_semi_stab()
        inter = frozenset.intersection(*SSTAB)
        bddADM = [S for S in ADM if S.issubset(inter)]
        answer = find_max_sets(bddADM)
        return answer[0]

    """
    Graded acceptability of arguments Modgil Grossi IJCAI 2015 (not tested)
    """

    # Graded neutrality function, (S,m) --> n_m(S)
    def graded_neutrality(self, subset, number):
        if not subset.issubset(self.arguments()):
            return "invalid subset of arguments"
        # set up output
        answer = set()
        # iterate over all arguments
        for argument in self.arguments():
            # Calculate a^-
            attackers = self.set_minus(set([argument]))
            # Calculate |S cap a^-|
            threshold = len(subset.intersection(attackers))
            if threshold < number:
                answer.add(argument)
        return answer

    # Graded defence function S --> d^m_n(S)
    def graded_defence(self, subset, num1, num2):
        if not subset.issubset(self.arguments()):
            return "invalid subset of arguments"
        intermediate = self.graded_neutrality(subset, num2)
        answer = self.graded_neutrality(intermediate, num1)
        return answer



def test_AF(myAF, example_name):
    """
    Function that tests most of the class methods above
    Input: Absargfw class, name of example (string)
    Output: prints a list of properties using the above methods
    """
    print example_name
    
    start = time.time()
    answer = myAF.empty()
    end = time.time()
    print str(end - start)+"s:", "\t", "Is this AF empty?", "\t", answer

    start = time.time()
    answer = myAF.trivial()
    end = time.time()
    print str(end - start)+"s:", "\t", "Is this AF trivial?", "\t", answer

    start = time.time()
    answer = myAF.number_of_arguments()
    end = time.time()
    print str(end - start)+"s:", "\t", "Number of arguments:", "\t", answer
    
    start = time.time()
    answer = myAF.number_of_attacks()
    end = time.time()
    print str(end - start)+"s:", "\t", "Number of attacks:", "\t", answer
    
    start = time.time()
    answer = myAF.arguments()
    end = time.time()
    print str(end - start)+"s:", "\t", "The arguments are:", "\t", answer

    start = time.time()
    answer = myAF.attacks()
    end = time.time()
    print str(end - start)+"s:", "\t", "The attacks are:", "\t", answer
    
    start = time.time()
    answer = myAF.set_of_unattacked()
    end = time.time()
    print str(end - start)+"s:", "\t", "Unattacked arguments:", "\t", answer
    
    start = time.time()
    answer = myAF.set_of_self_attacking()
    end = time.time()
    print str(end - start)+"s:", "\t", "Self-attacking args:", "\t", answer
    
    start = time.time()
    answer = myAF.cyclic()
    end = time.time()
    print str(end - start)+"s:", "\t", "Is this AF cyclic?", "\t", answer
    if myAF.cyclic():
        start = time.time()
        answer = myAF.cycles()
        end = time.time()
        print str(end - start)+"s:", "\t", "The set of cycles is:", "\t", answer
    
    start = time.time()
    answer = myAF.controversial()
    end = time.time()
    print str(end - start)+"s:", "\t", "Controversial AF?", "\t", answer
    
    start = time.time()
    answer = myAF.limited_controversial()
    end = time.time()
    print str(end - start)+"s:", "\t", "Limited controversial?", "\t", answer
    
    start = time.time()
    answer = myAF.all_cf()
    end = time.time()
    print str(end - start)+"s:", "\t", "Conflict-free sets:", "\t", answer

    start = time.time()
    answer = myAF.all_naive()
    end = time.time()
    print str(end - start)+"s:", "\t", "Naive extensions:", "\t", answer

    start = time.time()
    answer = myAF.all_sd()
    end = time.time()
    print str(end - start)+"s:", "\t", "Self-defending sets:", "\t", answer

    start = time.time()
    answer = myAF.all_adm()
    end = time.time()
    print str(end - start)+"s:", "\t", "Admissible sets:", "\t", answer

    start = time.time()
    answer = myAF.all_comp()
    end = time.time()
    print str(end - start)+"s:", "\t", "Complete extensions:", "\t", answer

    start = time.time()
    answer = myAF.all_pref()
    end = time.time()
    print str(end - start)+"s:", "\t", "Preferred extensions:", "\t", answer

    start = time.time()
    answer = myAF.stable_exists()
    end = time.time()
    print str(end - start)+"s:", "\t", "Stable extensions?", "\t", answer
    if answer:
        start = time.time()
        answer = myAF.all_stab()
        print str(end - start)+"s:", "\t", "Stable extensions are:", "\t", answer

    start = time.time()
    answer = myAF.grounded()
    end = time.time()
    print str(end - start)+"s:", "\t", "Grounded extension:", "\t", answer

    start = time.time()
    answer = myAF.coherent()
    end = time.time()
    print str(end - start)+"s:", "\t", "Is this AF coherent?", "\t", answer

    start = time.time()
    answer = myAF.relatively_grounded()
    end = time.time()
    print str(end - start)+"s:", "\t", "Relatively grounded?", "\t", answer

    start = time.time()
    answer = myAF.all_semi_stab()
    end = time.time()
    print str(end - start)+"s:", "\t", "Semi-stable exts:", "\t", answer

    start = time.time()
    answer = myAF.all_stage()
    end = time.time()
    print str(end - start)+"s:", "\t", "Stage extensions:", "\t", answer

    start = time.time()
    answer = myAF.ideal()
    end = time.time()
    print str(end - start)+"s:", "\t", "The ideal extesion:", "\t", answer

    start = time.time()
    answer = myAF.eager()
    end = time.time()
    print str(end - start)+"s:", "\t", "The eager extension:", "\t", answer



def APY_abs_arg_note():
    """
    Runs all the examples in Notes on Abstract Argumentation Theory by A. P. Young
    """
    print
    nixon = Absargfw(nx.DiGraph([('a','b'),('b','a')]))
    test_AF(nixon, "Example 2.2 - Nixon diamond")

    print
    simple_reinstatement = Absargfw(nx.DiGraph([('c','b'),('b','a')]))
    test_AF(simple_reinstatement, "Example 2.3 - Simple Reinstatement")

    print
    double_reinstatement = Absargfw(nx.DiGraph([('b','a'),('c','b'),('e','b')]))
    test_AF(double_reinstatement, "Example 2.4 - Double Reinstatement")

    print
    eg2p5 = Absargfw(nx.DiGraph([('a','b'),('b','a'),('c','b')]))
    test_AF(eg2p5, "Example 2.5")

    print
    eg2p6 = Absargfw(nx.DiGraph([('e','c'),('c','b'),('b','a')]))
    test_AF(eg2p6, "Example 2.6")

    print
    fri = Absargfw(nx.DiGraph([('a','b'),('b','a'),('a','c'),('b','c'),('c','e')]))
    test_AF(fri, "Example 2.7 - Floating Reinstatement")

    print
    print "Example 2.10 - Nixon Diamond"
    print "b in {a}^+?", 'b' in nixon.set_plus(set(['a']))
    print "a in {b}^+?", nixon.set_attacks(set(['b']), 'a')

    print
    print "Example 2.11 - Example 2.5"
    print "c in {a,b}^-?", 'c' in eg2p5.set_minus(set(['a','b']))

    print
    print "Example 2.12 - Double Reinstatement"
    print "{c,e} attacks {a,b}?", double_reinstatement.subset_attacks(set(['c','e']),set(['a','b']))

    print
    eg2p18 = Absargfw(nx.DiGraph([('a','a'),('a','b')]))
    test_AF(eg2p18, "Example 2.18")

    print
    eg2p33 = Absargfw(nx.DiGraph([('b','a'),('b','e'),('e','c'),('c','b')]))
    test_AF(eg2p33, "Example 2.33")

    print
    print "Example 2.42 - Example 2.6"
    print "Does e indirectly attack a?", eg2p6.indirectly_attacks('e','a')

    print
    print "Example 2.45 - Example 2.2"
    print "Does b indirectly defend b (itself)?", nixon.indirectly_defends('b','b')

    print
    eg2p49 = Absargfw(nx.DiGraph([('a','b'),('b','c'),('a','c')]))
    test_AF(eg2p49, "Example 2.49")
    print "Is a controversial w.r.t. c?", eg2p49.controversial_arguments('a','c')

    print
    print "Example 3.3 - neutrality function for simple reinstatement"
    for subset in powerlist(simple_reinstatement.arguments()):
        print subset, simple_reinstatement.neutrality(subset)

    print
    print "Example 5.2 - simple reinstatement"
    print "Does {c} reinstate a?", 'a' in simple_reinstatement.defence(set(['c']))

    print
    print "Example 5.3 - double reinstatement"
    print "Does {c,e} reinstate a?", 'a' in double_reinstatement.defence(set(['c','e']))

    print
    print "Example 5.7 - simple reinstatement"
    for subset in powerlist(simple_reinstatement.arguments()):
        print subset, simple_reinstatement.defence(subset)

    print
    eg5p8 = Absargfw(nx.DiGraph([('a','a'),('a','b'),('b','a')]))
    test_AF(eg5p8, "Example 5.8")

    print
    print "Example 5.8 - values of defence function"
    for subset in powerlist(eg5p8.arguments()):
        print subset, eg5p8.defence(subset)

    print
    eg8p4 = Absargfw(nx.DiGraph([('a','b'),('c','b'),('c','f'),('f','c'),('f','e'),('e','e')]))
    test_AF(eg8p4, "Example 8.4")

    print
    thm14p8 = Absargfw(nx.DiGraph([('a','b'),('b','c'),('c','a'),('f','c'),('e','f'),('a','c')]))
    test_AF(thm14p8, "Converse to Theorem 14.8")


# Directed ER graph (returns object of type nx.DiGraph)
def erdigraph(nodes, prob):
    """
    Slight modification to NetworkX graph generator syntax
    Use this as ``null model'' for argument graphs
    """
    answer = nx.erdos_renyi_graph(nodes, prob, directed = True)
    return answer

# ER argumentation framework (returns object of type Absargfw)
def eraf(nodes, prob):
    """
    Outputs an ER-graph as an AF class
    """
    return Absargfw(erdigraph(nodes, prob))

# How scalable is this code, implemented naively?
def scalability_measure_powerlist(upper):
    """
    Input: integer >= 0 as largest size (upper)
    Output: list of pairs (size, time taken to calculate powerlist)
    MacBook Air running this code locally: set of size 20 takes 10s to calculate power set
    """
    answer = []
    # e.g. if upper = 10 then we have 0, 1, 2, ..., 9, 10
    for size in tqdm(range(upper + 1)):
        start = time.time()
        calculate = powerlist(set(range(size)))
        end = time.time()
        y_value = end - start
        datapoint = (size, y_value)
        answer.append(datapoint)
    return answer

# How scalable is this code, implemented naively?
def scalability_measure_adm(upper, sample_size, prob):
    """
    Input: upper >= 0 as integer, sample_size > 0, prob in [0,1]
    Output: list of pairs (size, average time over sample_size to list all adm sets)
    """
    answer = []
    for size in tqdm(range(upper + 1)):
        sample_time = []
        for round in range(sample_size):
            myAF = eraf(size, prob)
            start = time.time()
            calculate = myAF.all_adm()
            end = time.time()
            sample_point = end - start
            sample_time.append(sample_point)
        y_value = sum(sample_time) / sample_size
        datapoint = (size, y_value)
        answer.append(datapoint)
    return answer
