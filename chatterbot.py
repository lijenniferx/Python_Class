#!/usr/bin/env

import string
import re
import numpy as np
import sys

def mood_generator(mood):
    if mood == 'good':
        score = np.random.random(1) + 0.1
    elif mood == 'bad':
        score = np.random.random(1) - 0.1
    else:
        score = np.random.random(1)
    return score


def make_bot(mood):
    mood_score = mood_generator(mood)
    
    done = False
    while not done:
        mom_says = raw_input("Say something: (Type 'quit' to exit the program)")
        ## remove quotes
        if mom_says == 'quit' or len(mom_says) == 0:
            done = True
        else:
            if mom_says[-1] == '?':
                if mood_score > 0.5:
                    print "It was alright."
                else:
                    print "Answer: Leave me alone."
                    
            elif mom_says[-1] == '!':
                if mood_score > 0.5:
                    print "Ok! Ok!"
                else:
                    print "Answer: Stop yelling!"
            elif mom_says[-1] == '.':
                if mood_score > 0.5:
                    print "Answer: Whatever."
                else:
                    print "Answer: Whatever"
            elif re.search('homework', string.lower(mom_says)):
                print "I'll do that later"
            else:
                pass
                
if __name__ == '__main__':
    mood = sys.argv[1]
    make_bot(mood)

