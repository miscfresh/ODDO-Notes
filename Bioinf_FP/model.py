#!/usr/bin/env python3

import sys
import modeller
import modeller.automodel

atomdiry = sys.argv[4]

env = modeller.environ() 
env.io.atom_files_directory = [atomdiry]

###

alignfname = sys.argv[1]
template = sys.argv[2]
targetseq = sys.argv[3]


a = modeller.automodel.automodel(env, alignfname, template, targetseq)

a.starting_model = 1
a.ending_model = 1
a.make()


