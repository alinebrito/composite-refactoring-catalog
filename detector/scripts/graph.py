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
        fillcolor = 'grey74'
        label = 'm'
        label = 'c' if category in ['Class Decomposition'] else label
        label = 'a' if category in ['Push Down Field', 'Pull Up Field'] else label
        return {'label': label, 'fillcolor': fillcolor }

    def get_target_config(self, category):
        fillcolor = 'gray92'
        label = 'm'
        label = 'a' if category in ['Push Down Field', 'Pull Up Field'] else label
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
            group = subgraph.graph.get('group')
            file_name = '{}/view/subgraph_{}_{}'.format(path, subgraph.graph.get('group'), index) 
            self.save_graph_to_html(svg, file_name)
            self.save_graph_to_svg(svg, file_name)
            self.create_readme(subgraph, file_name, index)
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
    
    def save_graph_to_html(self, svg, file_name):
        self.save_file(svg,'{}.html'.format(file_name))
        return

    def save_graph_to_svg(self, svg, file_name):
        self.save_file(svg,'{}.svg'.format(file_name))
        pass

    def save_file(self, file, file_name):
        print('Creating {}'.format(file_name))
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with io.open(file_name, 'w', encoding='utf8') as f:
            f.write(file.pipe().decode('utf-8'))
        pass

    def create_readme(self, graph, file_name, index):
        json = json_graph.node_link_data(graph)
        md_file = '{}.md'.format(file_name)
        svg_file = 'subgraph_{}_{}.svg'.format(graph.graph.get('group'), index)
        print('Creating {}'.format(md_file))
        with open(md_file, 'w') as f:
                f.write("<img src='{}' width='25%'>\n\n".format(svg_file))
                f.write("## Refactorings:\n")
                for edge in json.get('links'):
                    f.write("\n\nid: `{}`\\".format(edge.get('key')))
                    f.write("\nsource: `{}`\\".format(edge.get('source')))
                    f.write("\ntarget: `{}`\\".format(edge.get('target')))
                    f.write("\ntype: `{}`\\".format(edge.get('properties').get('refactoringType')))
                    f.write("\ncommit: [{}](https://github.com/{}/commit/{})".format(edge.get('properties').get('abbreviatedCommitHash'),json.get('graph').get('project'),edge.get('properties').get('commitHash')))
                    if edge.get('properties').get('descriptionOracle'):
                        f.write("\\\ndescription: `{}`".format(edge.get('properties').get('descriptionOracle')))
        pass
    

    