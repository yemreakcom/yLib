python ../YGitBookIntegration/integrate.py .
echo "---
description: Sitede neler olup bittiğinin raporudur.
---
" > CHANGELOG.md

gitchangelog.exe >> CHANGELOG.md
gbash github .
