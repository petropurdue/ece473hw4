import shell
import util
import wordsegUtil

#STANFORD HONOR CODE:
#The Honor Code is an undertaking of the students, individually and collectively:
#that they will not give or receive aid in examinations; that they will not give or receive unpermitted aid in class work, in the preparation of reports, or in any other work that is to be used by the instructor as the basis of grading;
#that they will do their share and take an active part in seeing to it that others as well as themselves uphold the spirit and letter of the Honor Code.
#The faculty on its part manifests its confidence in the honor of its students by refraining from proctoring examinations and from taking unusual and unreasonable precautions to prevent the forms of dishonesty mentioned above. The faculty will also avoid, as far as practicable, academic procedures that create temptations to violate the Honor Code.
#While the faculty alone has the right and obligation to set academic requirements, the students and faculty will work together to establish optimal conditions for honorable academic work.

#PURDUE HONOR CODE:
#As a boilermaker pursuing academic excellence, I promise to be honest and true in all that I do. Accountable together- we are Purdue


#I'm required by this assignment to agree to the Stanford Honor Code, but you can't deny Purdue's is just better

############################################################
# Problem 1: Solve the segmentation problem under a unigram model

class SegmentationProblem(util.SearchProblem):
    def __init__(self, query, unigramCost):
        self.query = query
        self.unigramCost = unigramCost

    def start(self):
        # Return the start state.
        # Return value has the same type as a state
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
        return(self.query)
        # END_YOUR_CODE

    def goalp(self, state):
        # Boolean predicate to decide whether |state| is an end state or not.
        # Return a True/False value.
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
        #print(len(state),len(self.query))
        if len(state) != 0:
            return False
        else:
            return True
        # END_YOUR_CODE

    def expand(self, state):
        # Return a list of (action, nextState, cost) tuples corresponding to edges
        # coming out of |state|.
        # |nextState| has the same type as |state|. |cost| is a float.
        # BEGIN_YOUR_CODE (our solution is 5 lines of code, but don't worry if you deviate from this)
        bigL = []

        for i in range(len(state),0,-1):
            substate = state[0:i]
            #results.append(('West', (x, y-1), 2))
            bigL.append((substate,state[(len(substate)):],self.unigramCost(substate)))
        return bigL

def segmentWords(query, unigramCost):
    if len(query) == 0:
        return ''

    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(SegmentationProblem(query, unigramCost))

    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    final=' '.join(ucs.actions)
    return final
    # END_YOUR_CODE

############################################################
# Problem 2: Solve the vowel insertion problem under a bigram cost

class VowelInsertionProblem(util.SearchProblem):
    def __init__(self, queryWords, bigramCost, possibleFills):
        self.queryWords = queryWords
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def start(self):
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
        return (self.queryWords[0],0)
        # END_YOUR_CODE

    def goalp(self, state):
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
        SL = state[1]
        if SL != len(self.queryWords)-1:
            return False
        else:
            return True
        # END_YOUR_CODE

    def expand(self, state):
        # BEGIN_YOUR_CODE (our solution is 6 lines of code, but don't worry if you deviate from this)
        res = []
        pos=state[1]+1
        #print("INDEX:",index)
        #print(state[1],state[1]+1)
        PF = self.possibleFills(self.queryWords[pos]).copy()

        PFL = len(PF)
        if PFL == 0:
            PF.add(self.queryWords[pos])
        for action in PF:
            cost=self.bigramCost(state[0],action)
            res.append((action, (action,pos), cost))
        return res
        # END_YOUR_CODE

def insertVowels(queryWords, bigramCost, possibleFills):
    # BEGIN_YOUR_CODE (our solution is 3 lines of code, but don't worry if you deviate from this)
    #print("!!!")
    QWL = len(queryWords)
    if QWL == 0:
        return ''
    else:
        queryWords.insert(0,wordsegUtil.SENTENCE_BEGIN)

    UniformCostRes=util.UniformCostSearch(verbose=1)
    UniformCostRes.solve(VowelInsertionProblem(queryWords,bigramCost,possibleFills))
    words = ' '.join(UniformCostRes.actions)
    return words

    # END_YOUR_CODE


if __name__ == '__main__':
    shell.main()
