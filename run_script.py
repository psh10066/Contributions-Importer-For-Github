import git
from git_contributions_importer import *

repo = [
    git.Repo("../brand-site"),
    git.Repo("../config-files"),
    git.Repo("../dental-hygiene"),
    git.Repo("../dent-i"),
    git.Repo("../denti-i_2021_api"),
    git.Repo("../denti-i_2021_front"),
    git.Repo("../dentii-signup"),
    git.Repo("../denti-roka"),
    git.Repo("../denti-roka-admin"),
    git.Repo("../denti-roka-module"),
    git.Repo("../dentis-admin"),
    git.Repo("../dentis-api"),
    git.Repo("../dentix-admin"),
    git.Repo("../dentix-api"),
    git.Repo("../dt2022-api"),
    git.Repo("../dt2022-batch"),
    git.Repo("../dt2022-edu"),
    git.Repo("../dt2022-front"),
    git.Repo("../dt2022-mobile-web"),
    git.Repo("../dt2022-webview"),
    git.Repo("../dth-api"),
    git.Repo("../dth-front"),
    git.Repo("../dthi-admin"),
    git.Repo("../dthi-api"),
    git.Repo("../dtvtn-admin"),
    git.Repo("../dtvtn-api"),
    git.Repo("../excel"),
    git.Repo("../famdoc-2020"),
    git.Repo("../mdm-admin-front"),
    git.Repo("../mdm-front"),
    git.Repo("../menti-doc"),
    git.Repo("../m-gyeonggi-2021"),
    git.Repo("../ondentii-admin"),
    git.Repo("../ondentii-api"),
    git.Repo("../ondentii-web"),
]
mock_repo = git.Repo("../import-contributions")

importer = Importer(repo, mock_repo)
importer.set_author(['psh10066@gmail.com', 'hjlee@kai-i.com']) # 내가 저장소에 작성했던 이메일

importer.set_start_from_last(True)

importer.import_repository()