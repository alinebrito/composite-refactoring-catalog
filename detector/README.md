# Scripts to detect Composite Refactorings

## Dependencies

* Git 2.17.1+

* Java 8

* Python 3+

* Python libraries: `pip3 install --no-cache-dir -r requirements.txt`

* [Graphviz](https://graphviz.org/download/) 2.40.1 

## Usage

> python3 main.py refdiff owner/project

> python3 main.py detect owner/project

> python3 main.py report owner/project

## Output

### Composite Refactoring:

* JSON: `output/{owner}/{project}/results/{composite name}/subgraphs.json`

* HTML: `output/{owner}/{project}/results/{composite name}/view`

* Single refactoring operations: ` output/{owner}/{project}/results/{composite name}/selected_refactorings.csv`

### Project:

* Commits: `output/{owner}/{project}/results/commits.csv`

* Detected refactorings: `output/{owner}/{project}/results/refactorings.csv`

### Report:

Class Decomposition: {occurrence}

Method Decomposition: {occurrence}

Method Composition: {occurrence}

Pull Up Method: {occurrence}

Push Down Method: {occurrence}

Inline Method: {occurrence}




