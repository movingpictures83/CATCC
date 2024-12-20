import os

import PyPluMA

class CATCCPlugin:
   def input(self, inputfile):
       self.dataset = inputfile
   def run(self):
       pass
   def output(self, outputfile):
       os.system("python3 plugins/CATCC/main.py --selected_dataset "+self.dataset[self.dataset.rfind('/')+1:]+" --data_path "+PyPluMA.prefix())
