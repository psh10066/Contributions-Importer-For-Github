import git
from git_contributions_importer import *

repo = [
    git.Repo("../repo_name")
]
mock_repo = git.Repo("../import-contributions")

importer = Importer(repo, mock_repo)
importer.set_author(['psh10066@gmail.com', 'hjlee@kai-i.com']) # 내가 저장소에 작성했던 이메일

importer.set_start_from_last(True)

importer.import_repository()