import sys
import subprocess
import os
import json
import pandas as pd
import networkx as nx
import io
from graphviz import Digraph
from networkx.readwrite import json_graph
import json

class Graph:

    def create_digraph(self, refactorings, weight, id):
        group_name = 'atomic' if len(weight) == 1 else 'overtime'
        DG = nx.DiGraph(group=group_name,id=id)
        for ref in refactorings:
            properties = {}
            for key in ref.keys():
                properties[key] = ref.get(key)
            properties['weight'] = weight.get(ref.get('commitHash'))
            DG.add_edge(ref.get('entityBeforeFullName'), ref.get('entityAfterFullName'))
            DG[ref.get('entityBeforeFullName')][ref.get('entityAfterFullName')]['properties'] = properties
        return DG

    def create_multigraph(self, project, refactorings, weight, id):
        group_name = 'atomic' if len(weight) == 1 else 'overtime'
        DG = nx.MultiDiGraph(group=group_name,id=id,project=project)
        for index, ref in enumerate(refactorings):
            properties = {}
            for key in ref.keys():
                properties[key] = ref.get(key)
            properties['weight'] = weight.get(ref.get('commitHash'))
            DG.add_edge(ref.get('source'), ref.get('target'), index)
            DG[ref.get('source')][ref.get('target')][index]['properties'] = properties
        return DG

    def get_source_config(self, category):
        label = 'm'
        fillcolor = 'grey74'
        if category in ['Class Decomposition']:
            label = 'c'
        return {'label': label, 'fillcolor': fillcolor }

    def get_target_config(self, category):
        label = 'm'
        fillcolor = 'gray92'
        return {'label': label, 'fillcolor': fillcolor }


    def plot(self, subgraphs, path, category):
        for index, subgraph in enumerate(subgraphs):
            #print('{}: {}'.format(node, DG.out_edges(node)))
            svg = Digraph(format='svg')
            for edge in subgraph.edges(data=True):
                properties = edge[2].get('properties')
                #source
                sourceconfig = self.get_source_config(category)
                svg.attr('node', shape='circle', style='filled', color='dimgrey', fillcolor=sourceconfig.get('fillcolor'), width='0.4', height='0.15',  stroke='black', fixedsize='true')
                svg.node(edge[0], label=sourceconfig.get('label'), len='1.0')
                #target
                targetconfig = self.get_target_config(category)
                svg.attr('node', shape='circle', style='filled, dashed', color='dimgrey', fillcolor=targetconfig.get('fillcolor'), width='0.4', height='0.15',  stroke='black', fixedsize='true')
                svg.node(edge[1], label=targetconfig.get('label'), len='1.0')
                #edge
                linkedge = 'https://github.com/{}/commit/{}'.format(subgraph.graph.get('project'), properties.get('commitHash'))
                svg.edge(edge[0], edge[1], color='dimgrey', href=linkedge, label='{}'.format(properties.get('refactoringType')), fontsize='10', len='0.1', minlen=str(properties.get('weight')), style="dashed")
            label_text = '\n\n{}\n\nSubgraph #{}\n\n\{}'.format(subgraph.graph.get('project'), index, category)
            svg.attr(bgcolor='', label=label_text, fontcolor='black', rankdir='LR', ratio='auto', pad="0.5,0.5")
            self.save_graph_to_html(svg, subgraph.graph.get('group'), index, path)
        self.save_graph_to_json(subgraphs, path)    
        return

    def save_graph_to_json(self, subgraphs, path):
        file_name = '{}/subgraphs.json'.format(path) 
        file_json = [json_graph.node_link_data(subgraph) for subgraph in subgraphs]
        print('Creating {}'.format(file_name))
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        file = open(file_name, 'w+')
        json.dump(file_json, file)
        file.close()
        pass  

    def save_graph_to_html(self, svg, group, id, path):
        file_name = '{}/view/subgraph_{}_{}.html'.format(path, group, id) 
        print('Creating {}'.format(file_name))
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with io.open(file_name, 'w', encoding='utf8') as f:
            f.write(svg.pipe().decode('utf-8'))
        return
    

    