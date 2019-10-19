# python ../YGitBookIntegration/integrate.py . -d && \
echo "---
description: Sitede neler olup bittiğinin raporudur.
---
" > CHANGELOG.md && \
python update_sums.py && \
ygitchangelog.exe -d >> CHANGELOG.md && \
bash github .
