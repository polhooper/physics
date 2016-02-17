import subprocess, sys, os

print('Generating the term-document matrix...')
cmd = 'python term_doc_mat.py . 100'
subprocess.call(cmd, shell=True) 

print('Running the LDA analysis...')
#..30 - 50 branches of physics as the prior: https://en.wikipedia.org/wiki/Outline_of_physics
cmd = 'python topic_lda.py . 50 500 60'
subprocess.call(cmd, shell=True) 

print('Formatting data to Gephi-ingestible format...')
cmd = 'Rscript gexf_format.R'
subprocess.call(cmd, shell=True) 
