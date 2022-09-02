import json
from scripts.composite import Composite as Composite

class Report:
      
    def get_composites(self, project, path):
        # file_name = 'output/{}/results/{}/subgraphs.json'.format(project,path)
        file_name = '../results/oracle/{}/results/{}/subgraphs.json'.format(project,path)
        subgraphs = []
        with open(file_name) as json_file:
            subgraphs = json.load(json_file)
        return subgraphs

    def count_composites(self, project, path):
        return len(self.get_composites(project, path))

    def print_composite(self, count, compositename):
        print('{}: {}'.format(compositename, count))

    def log(self, project):
        print('\n\n------------------\n\nReport: {}\n'.format(project))
        composites = Composite.get()
        for key in composites.keys():
            count = self.count_composites(project, key)
            self.print_composite(count, composites.get(key).get('name'))
        print('\n------------------')
        pass
