# Commands
1. Check commit: git log -1 (or -2, -3...)
2. Commit: git gui -> press commit button
3. Create new user branch: git checkout -b usr/tdi4hc/TICKET
4. Push on remote branch: 
        git push origin usr/tdi4hc/TICKET
        git push -f origin usr/tdi4hc/TICKET
6. git reset --hard
7. git clean -fdx -> clean all 
    -> clean uncommit: git clean -fd
8. Create patch file from commits:
    One commit: git format-patch -1 <commit>
    Many commit (từ A đến B, bao gồm B): git format-patch <commit_A>^..<commit_B>
    ->> Apply patch file: git am *.patch
9. Create file patch for file:
        git diff app/prog/reset_detection/reset_detection_messages.h > a.patch
10. Add repo from WSL: \\wsl$\Ubuntu-20.04\home\username\my-repo
11. Git merge: merge commits from feature/login into main:
        git checkout main
        git merge feature/login
12. Remote
List all remote repos:
        git remote
Add new remote repo:
        git remote add <NAME> <URL/PathToGit>
        git remote add backup "C:/Users/tdi4hc/code/MeDaC_AI_Cofigurator_MAC_backup_02/.git"
Delete remote repo:
        git remote remove <NAME>
Show infor of remote:
        git remote show origin
13. Tag
        git tag <name> <commit_hash>
        git tag -d <name>
14. Stash
Create stash:
        git stash -m "mess"
Apply and keep:
        git stash apply stash@{0}
Apply and remove:
        git stash pop stash@{0}
Clear only 1 stash:
        git stash drop stash@{0}
Clear all stashes: 
        git stash clear
15. submodule
    git submodule add <repo-url> path/to/subrepo
    git submodule add <repo-url> etas/abo
    ->> do NOT create new folder

