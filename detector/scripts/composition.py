import re
import os.path
import hashlib
import sys
import pandas as pd
from collections import Counter
from scripts.graph import Graph
from scripts.filter import RefactoringFilter
import shutil

class Composition:

    def init(self, path, project, refactoring_levels, operations, file_name):
        if os.path.exists(path):
            print('Removing {}'.format(path))
            shutil.rmtree(path)
        filter = RefactoringFilter()
        return filter.init(path, project, refactoring_levels, operations,file_name)

    def calc_weight(self, refactorings):
        commits = list(set([(ref.get('commitHash'), ref.get('authorDateUnixTimestamp'), ref.get('authorDate')) for ref in refactorings]))
        commits.sort(key=lambda commit:commit[1], reverse=True)#sort commits by date
        weight = {}
        for index, commit in enumerate(commits):
            weight[commit[0]] = index+1
        return weight

    def plot(self, project, refactorings, path, category):
        nodes_after = [ref.get('target') for ref in refactorings]
        count_nodes_after = Counter(nodes_after)
        selected_nodes_after = [node for node in count_nodes_after if (count_nodes_after[node] > 1)]
        selected_refactorings = [ref for ref in refactorings if ref.get('target') in selected_nodes_after]
        graph = Graph()
        subgraphs = []
        for id, node in enumerate(selected_nodes_after):
            refactoring_from_target = [ref for ref in selected_refactorings if (ref.get('target') == node)]
            weight = self.calc_weight(refactoring_from_target)
            DG = graph.create_multigraph(project, refactoring_from_target, weight, id)
            subgraphs.append(DG)
        graph.plot(subgraphs, path, category)
        pass

    def pull_up_method(self, project):
        path = 'output/{}/results/composition_pull_up_method'.format(project)
        file_name_method = '{}/selected_refactorings_method.csv'.format(path)
        refactorings_method = self.init(path, project, ['MethodDeclaration'], ["PULL_UP"], file_name_method)
        for index, ref in enumerate(refactorings_method):
            ref['source'] = ref.get('entityBeforeFullName').replace(' ', '')
            ref['target'] = ref.get('entityAfterFullName').replace(' ', '')
        self.plot(project, refactorings_method, path, 'Pull Up Method')
        pass

    def extract_method(self, project):
        path = 'output/{}/results/composition_extract_method'.format(project)
        file_name_method = '{}/selected_refactorings_method.csv'.format(path)
        refactorings_method = self.init(path, project, ['MethodDeclaration'], ["EXTRACT", "EXTRACT_MOVE"], file_name_method)
        for index, ref in enumerate(refactorings_method):
            ref['source'] = ref.get('entityBeforeFullName').replace(' ', '')
            ref['target'] = ref.get('entityAfterFullName').replace(' ', '')
        self.plot(project, refactorings_method, path, 'Method Composition')
        pass


    def pull_up_attribute(self, project):
        path = 'output/{}/results/composition_pull_up_attribute'.format(project)
        file_name = '{}/selected_refactorings.csv'.format(path)
        refactorings = self.init(path, project, ['AttributeDeclaration'], ["PULL_UP"], file_name)
        for index, ref in enumerate(refactorings):
            ref['source'] = ref.get('entityBeforeFullName').replace(' ', '')
            ref['target'] = ref.get('entityAfterFullName').replace(' ', '')
        self.plot(project, refactorings, path, 'Pull Up Attribute')
    pass



