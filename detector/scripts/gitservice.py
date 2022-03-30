import subprocess
import os
import pandas as pd

class GitService:
    
    def clone(self, project):
        print('Cloning {}...'.format(project))
        subprocess.call('git clone https://github.com/{}.git --bare output/{}/code'.format(project,project), shell = True)
    pass

    def first_parent(self, project):
        print('Finding commits from default branch...')
        # proc = subprocess.Popen(['git', '-C', 'output/{}/code'.format(project), 'log', '--first-parent', '--pretty=%H;%h;%an;%ae;%ad;%at;%cn;%ce;%cd;%ct'], stdout=subprocess.PIPE).communicate()
        proc = subprocess.Popen(['git', '-C', 'output/{}/code'.format(project), 'log', '--first-parent', '--pretty=%H;%h;-;-;%ad;%at;-;-;%cd;%ct'], stdout=subprocess.PIPE).communicate()
        file_name = 'output/{}/results/commits.csv'.format(project)
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with open(file_name, 'w') as file:
            file.write('commitHash;abbreviatedCommitHash;authorName;authorEmail;authorDate;authorDateUnixTimestamp;committerName;committerEmail;committerDate;committerDateUnixTimestamp\n')
            [file.write(data.decode('utf-8')) for data in proc if data]
    pass

    def count_files(self, project):
        print('Counting changed files at commit...')
        commits = pd.read_csv('output/{}/results/commits.csv'.format(project), sep=";", keep_default_na=False)
        file_name = 'output/commits_changed_files.csv'.format(project)
        with open(file_name, 'a+') as file:
            file.flush()
            os.fsync(file.fileno())
            # file.write('project;commitHash;files\n')
            for index, commit in commits.iterrows():
                proc1 = subprocess.Popen(['git', '-C', 'output/{}/code'.format(project), 'show', '--oneline', '--numstat', '{}'.format(commit.get('commitHash'))], stdout=subprocess.PIPE)
                proc2 = subprocess.Popen(['wc', '-l'], stdin=proc1.stdout, stdout=subprocess.PIPE).communicate()
                for data in proc2:
                    if data:
                        countfiles = int(data.decode('utf-8')) - 1
                        print('Commit {} ... '.format(commit.get('commitHash')))
                        line = '{};{};{}\n'.format(project, commit.get('commitHash'), countfiles)
                        file.flush()
                        os.fsync(file.fileno())
                        file.write(line)
        pass
 


