#..thanks to http://www.christianpeccei.com/textmining/ and 
#  https://pypi.python.org/pypi/textmining/1.0

import csv
import sys 
import os 
import textmining

work_dir = sys.argv[1]  
cutoff = int(sys.argv[2])

#..extract a list of files from the work directory
abs_dir = os.path.join(work_dir, 'cit-HepTh-abstracts')
date_dirs = os.listdir(abs_dir)

#..initialize term-document matrix
tdm = textmining.TermDocumentMatrix()

def build_tdm():
    ids = []
    for date in date_dirs: 
        print('Parsing data for %s...' % date)
        date_path = os.path.join(abs_dir, date)
        file_names = os.listdir(date_path)
        for abstract in file_names:
            ids.append(abstract[:-4])
            abs_path = os.path.join(date_path, abstract)
            with open(abs_path, 'r') as f: 
                text = f.read().splitlines()
                text = ' '.join(text)
                tdm.add_doc(text)
    
    print('Writing results to csv...')
    tdm.write_csv('%s/tdm.csv' % work_dir, cutoff = cutoff)
    with open('%s/ids.csv' % work_dir, 'wb') as f: 
        writer = csv.writer(f)
        for i in ids: 
            writer.writerow([i])

if __name__ == '__main__':
    build_tdm()
