import sys
sys.stdout.reconfigure(encoding='utf-8')
from find_all_diffs import old_data, new_data

diff_keys = [k for k in new_data if k in old_data and (old_data[k]['intl'] != new_data[k]['intl'] or old_data[k]['vn'] != new_data[k]['vn'])]
print('All diff keys:', diff_keys)
for k in diff_keys:
    print(f'=== {k} ===')
    print('  OLD:', old_data[k]['intl'])
    print('  NEW:', new_data[k]['intl'])
    print()
