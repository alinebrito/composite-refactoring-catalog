import re
import os.path
import hashlib
import sys
import pandas as pd
import shutil


class RefactoringFilter:

    def constructor(self, path, refactoring_levels):
        return ("#new(" in path) and ('MethodDeclaration' in refactoring_levels)

    def test_package(self, path):
        path = path.split("#")[0]
        test_package = re.findall(r'(test.+?|test)\.', path, re.IGNORECASE)
        contains_test_package = bool(re.search(r'(test.+?|test)\.', path, re.IGNORECASE))
        return contains_test_package

    def sample_package(self, path):
        path = path.split("#")[0]
        sample_package = re.findall(r'(sample.+?|sample)\.', path, re.IGNORECASE)
        contains_sample_package = bool(re.search(r'(sample.+?|sample)\.', path, re.IGNORECASE))
        return contains_sample_package

    def example_package(self, path):
        path = path.split("#")[0]
        example_package = re.findall(r'(example.+?|example)\.', path, re.IGNORECASE)
        contains_example_package = bool(re.search(r'(example.+?|example)\.', path, re.IGNORECASE))
        return contains_example_package

    def selected_operations(self, ref, refactoring_levels, operations):
        before = ref.get('entityBeforeFullName')
        after = ref.get('entityAfterFullName')
        return (ref.get('refactoringType') in operations) and \
        (ref.get('refactoringLevel') in refactoring_levels) and \
        (not self.example_package(before)) and \
        (not self.example_package(after)) and \
        (not self.test_package(before)) and \
        (not self.test_package(after)) and \
        (not self.sample_package(before)) and \
        (not self.sample_package(after)) and \
        (not self.constructor(before, refactoring_levels)) and \
        (not self.constructor(after, refactoring_levels))

    def filter_operations(self, project, refactoring_levels, operations, out_path):
        # refactorings = pd.read_csv('output/{}/results/refactorings.csv'.format(project), sep=';', keep_default_na=False)
        refactorings = pd.read_csv('../results/oracle/{}/results/refactorings.csv'.format(project), sep=';', keep_default_na=False)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'a+') as file:
            head = 'id;entityBeforeFullName;entityBeforeSimpleName;entityBeforeLocation;entityBeforeParameters;entityBeforeLine;entityBeforeParents;entityAfterFullName;entityAfterSimpleName;entityAfterLocation;entityAfterParameters;entityAfterLine;entityAfterParents;refactoringLevel;refactoringType;commitHash;abbreviatedCommitHash;authorName;authorEmail;authorDate;authorDateUnixTimestamp;committerName;committerEmail;committerDate;committerDateUnixTimestamp;idOracle;descriptionOracle\n'
            file.write(head)
            id = 0
            for index, ref in refactorings.iterrows():
                if self.selected_operations(ref, refactoring_levels, operations):
                    line = '{};'.format(id)
                    id = id + 1
                    for key in ref.keys():
                        line = line + '{};'.format(ref.get(key))
                    file.write('{}\n'.format(line[:-1]))
        pass

    def key(self, refactoring):
        return ('{}-{}-{}'.format(refactoring.get('entityBeforeFullName'), refactoring.get('refactoringType'), refactoring.get('entityAfterFullName')))

    def is_same_target_and_source(self, refactoring):
        return refactoring.get('entityBeforeFullName') == refactoring.get('entityAfterFullName')

    def filter_duplicated_refactorings(self, refactorings):
        refactorings_keys = [self.key(ref) for index, ref in refactorings.iterrows()]
        duplicated_refactorings = set([key for key in refactorings_keys if refactorings_keys.count(key) > 1])
        return [ref for index, ref in refactorings.iterrows() if ((self.key(ref) not in duplicated_refactorings) and (not self.is_same_target_and_source(ref)))]

    def init(self, path, project, refactoring_levels, operations, file_name):
        filter = RefactoringFilter()
        filter.filter_operations(project, refactoring_levels, operations, file_name)
        refactorings = pd.read_csv(file_name, sep=';', keep_default_na=False)
        refactorings = filter.filter_duplicated_refactorings(refactorings)
        return refactorings
