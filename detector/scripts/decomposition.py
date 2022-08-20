import re
import os.path
import hashlib
import sys
import pandas as pd
from collections import Counter
from scripts.graph import Graph
from scripts.filter import RefactoringFilter
import shutil

class Decomposition:

    def init(self, path, project, refactoring_levels, operations, file_name):
        if os.path.exists(path):
            print('Removing {}'.format(path))
            shutil.rmtree(path)
        filter = RefactoringFilter()
        return filter.init(path, project, refactoring_levels, operations, file_name)

    def calc_weight(self, refactorings):
        commits = list(set([(ref.get('commitHash'), ref.get('authorDateUnixTimestamp'), ref.get('authorDate')) for ref in refactorings]))
        commits.sort(key=lambda commit:commit[1], reverse=False)#sort commits by date
        weight = {}
        for index, commit in enumerate(commits):
            weight[commit[0]] = index+1
        return weight

    def plot(self, project, refactorings, path, category):
        nodes_before = [ref.get('source') for ref in refactorings]
        count_nodes_before = Counter(nodes_before)
        selected_nodes_before = [node for node in count_nodes_before if (count_nodes_before[node] > 1)]
        selected_refactorings = [ref for ref in refactorings if ref.get('source') in selected_nodes_before]
        graph = Graph()
        subgraphs = []
        for id, node in enumerate(selected_nodes_before):
            refactorings_from_source = [ref for ref in selected_refactorings if (ref.get('source') == node)]
            weight = self.calc_weight(refactorings_from_source)
            DG = graph.create_multigraph(project, refactorings_from_source, weight, id)
            subgraphs.append(DG)
        graph.plot(subgraphs, path, category)
        pass

    def extract_method(self, project):
        path = 'output/{}/results/decomposition_extract_method'.format(project)
        file_name = '{}/selected_refactorings.csv'.format(path)
        refactorings = self.init(path, project, ['MethodDeclaration'], ["EXTRACT", "EXTRACT_MOVE"], file_name)
        for index, ref in enumerate(refactorings):
            ref['source'] = ref.get('entityBeforeFullName').replace(' ', '')
            ref['target'] = ref.get('entityAfterFullName').replace(' ', '')
        self.plot(project, refactorings, path, 'Method Decomposition')
        pass

    def inline_method(self, project):
        path = 'output/{}/results/decomposition_inline_method'.format(project)
        file_name_method = '{}/selected_refactorings_method.csv'.format(path)
        refactorings_method = self.init(path, project, ['MethodDeclaration'], ["INLINE"], file_name_method)
        for index, ref in enumerate(refactorings_method):
            ref['source'] = ref.get('entityBeforeFullName').replace(' ', '')
            ref['target'] = ref.get('entityAfterFullName').replace(' ', '')
        self.plot(project, refactorings_method, path, 'Inline Method')

    def push_down_method(self, project):
        path = 'output/{}/results/decomposition_push_down_method'.format(project)
        file_name = '{}/selected_refactorings.csv'.format(path)
        refactorings = self.init(path, project, ['MethodDeclaration'], ["PUSH_DOWN"], file_name)
        for index, ref in enumerate(refactorings):
            ref['source'] = ref.get('entityBeforeFullName').replace(' ', '')
            ref['target'] = ref.get('entityAfterFullName').replace(' ', '')
        self.plot(project, refactorings, path, 'Push Down Method')
        pass

    def move_method(self, project):
        path = 'output/{}/results/decomposition_move_method'.format(project)
        file_name = '{}/selected_refactorings.csv'.format(path)
        refactorings = self.init(path, project, ['MethodDeclaration'], ["MOVE", "MOVE_RENAME", "INTERNAL_MOVE", "INTERNAL_MOVE_RENAME"], file_name)
        for index, ref in enumerate(refactorings):
            class_before = ref.get('entityBeforeFullName').split('#')[0].replace(' ', '')
            class_after = ref.get('entityAfterFullName').split('#')[0].replace(' ', '')
            ref['source'] = class_before
            ref['target'] = ref.get('entityAfterFullName')
        self.plot(project, refactorings, path, 'Class Decomposition')    
        pass

    def move_type(self, project):
        path = 'output/{}/results/decomposition_move_type'.format(project)
        file_name = '{}/selected_refactorings.csv'.format(path)
        refactorings = self.init(path, project, ['ClassDeclaration', 'InterfaceDeclaration'], ["MOVE", "MOVE_RENAME"], file_name)
        for index, ref in enumerate(refactorings):
            location_before = ref.get('entityBeforeLocation').split('/')
            package_before = '.'.join(location_before[0:(len(location_before)-1)])
            location_after = ref.get('entityAfterLocation').split('/')
            package_after = '.'.join(location_after[0:(len(location_after)-1)])
            class_after = ref.get('entityAfterFullName').split('#')[0]
            ref['source'] = package_before.replace(' ', '')
            ref['target'] = package_after.replace(' ', '')
            ref['refactoringType'] = '{} TYPE'.format(ref.get('refactoringType'))
        self.plot(project, refactorings, path, 'Package Decomposition') 
        pass

    def push_down_attribute(self, project):
        path = 'output/{}/results/decomposition_push_down_attribute'.format(project)
        file_name = '{}/selected_refactorings.csv'.format(path)
        refactorings = self.init(path, project, ['AttributeDeclaration'], ["PUSH_DOWN"], file_name)
        for index, ref in enumerate(refactorings):
            ref['source'] = ref.get('entityBeforeFullName').replace(' ', '')
            ref['target'] = ref.get('entityAfterFullName').replace(' ', '')
        self.plot(project, refactorings, path, 'Push Down Attribute')
    pass
