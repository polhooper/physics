#..thanks to https://pypi.python.org/pypi/lda and 

import numpy as np 
import pandas as pd 
import lda
import sys 

work_dir = sys.argv[1]
n_topics = int(sys.argv[2])
n_iter = int(sys.argv[3])

def run_lda(): 
    term_doc = pd.read_csv('%s/tdm.csv' % work_dir)
    vocab = term_doc.columns.values
    term_doc = np.array(term_doc)

    model = lda.LDA(n_topics=n_topics, n_iter=n_iter, random_state=1)
    print('Training the LDA model. This could take a minute...')
    model.fit(term_doc)

    topic_assignments = pd.DataFrame(model.doc_topic_)
    topic_assignments.to_csv('topic_weights.csv', index = False)

if __name__ == '__main__':
    run_lda()

# topic_word = model.topic_word_  # model.components_ also works
# n_top_words = 35
# for i, topic_dist in enumerate(topic_word):
#     topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
#     print('Topic {}: {}'.format(i, ' '.join(topic_words)))
