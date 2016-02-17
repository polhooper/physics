import subprocess, sys, os

print('Generating the term-document matrix...')
cmd = 'python term_doc_mat.py . 100'
subprocess.call(cmd, shell=True) 

print('Running the LDA analysis...')
cmd = 'python topic_lda.py . 10 250 30'
subprocess.call(cmd, shell=True) 

print('Formatting data to Gephi-ingestible format...')
cmd = 'Rscript gexf_format.R'
subprocess.call(cmd, shell=True) 
