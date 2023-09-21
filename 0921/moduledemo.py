#Module Search Ordering
# 1.동일 디렉토리에서 써치
# 2.sys.path에서
# 3.파이썬 설치위치
# 4.

import sys

for path in sys.path:
    print(path)