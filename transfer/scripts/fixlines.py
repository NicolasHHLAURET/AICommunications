import sys, hashlib, base64
# usage: python3 fixlines.py FILE RANGES_CSV DATAFILE_B64
# RANGES_CSV items: 'S-E:N' = received lines S..E (1-indexed inclusive) are replaced
# by the next N lines of DATAFILE_B64 (base64 of the replacement lines, one per line,
# concatenated in CSV order). Ranges applied bottom-up so earlier numbers stay valid.
# N may differ from E-S+1 (0 = deletion, > = insertion). Prints resulting sha256.
p = sys.argv[1]
ranges = []
for r in sys.argv[2].split(','):
    se, n = r.split(':')
    s, e = (int(x) for x in se.split('-'))
    ranges.append((s, e, int(n)))
L = open(p, 'rb').read().split(b'\n')
fix = base64.b64decode(open(sys.argv[3], 'rb').read()).split(b'\n')
if fix and fix[-1] == b'':
    fix.pop()
i = len(fix)
for s, e, n in sorted(ranges, reverse=True):
    i -= n
    L[s-1:e] = fix[i:i+n]
assert i == 0, 'data/line count mismatch: %d left' % i
out = b'\n'.join(L)
open(p, 'wb').write(out)
print(hashlib.sha256(out).hexdigest())
