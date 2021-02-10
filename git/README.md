
# Usage
```

    +----------------+   
    |    work dir    |------+ 
    +----------------+      | git add
    |     stage      | <----+
    +----------------+      | git commit
    |     HEAD       | <----+
    +----------------+

```

## git reset
- git reset HEAD~
    Cancel the last commit, point HEAD to the node before the commit, the content pointed to 
    by STAGE and HEAD will change, and the work directory remains unchanged. 

- git reset --hard HEAD~
    STAGE, HEAD and WORK are all changed.

## git checkout 
- git checkout 'branch'
    Switch branch

- git checkout HEAD~ foo.c
    Copy foo.c in the commit node HEAD~ (that is, the parent node of the current commit node) 
    to the working directory and add it to the staging area
```
    note: If the commit node is not specified in the command, the content will be copied from 
          the staging area
```
