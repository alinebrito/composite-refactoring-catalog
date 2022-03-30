import sys
import subprocess
import os
import json
import pandas as pd
import time
from scripts.gitservice import GitService
from scripts.refdiff import RefDiff
from scripts.decomposition import Decomposition
from scripts.composition import Composition
from scripts.report import Report

def run_refdiff(project):
    git = GitService()
    git.clone(project)
    git.first_parent(project)
    refdiff = RefDiff()
    refdiff.detect_refactorings(project, "java")
    pass

def detect_composite(project):
    detector_decomposition = Decomposition()
    detector_decomposition.extract_method(project)
    detector_decomposition.inline_method(project)
    detector_decomposition.push_down_method(project)
    detector_decomposition.move_method(project)
    detector_composition = Composition()
    detector_composition.pull_up_method(project)
    detector_composition.extract_method(project)
    pass

def report(project):
    report = Report()
    report.log(project)
    pass

def main():
    switch = {
        "refdiff": run_refdiff,
        "detector": detect_composite,
        "report": report
    }
    switch.get(sys.argv[1])(sys.argv[2])
    pass

if __name__ == "__main__":
    main()