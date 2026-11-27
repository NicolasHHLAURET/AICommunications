import sys, hashlib
p = sys.argv[1]
nums = [int(x) for x in sys.argv[2].split(',')]
data = open(p, 'rb').read()
assert hashlib.sha256(data).hexdigest() == 'bc46652a3ffd0c188acea0e5cc47df02948dd95bafc3ed11b55af15dee69efd9'
L = data.split(b'\n')
fix = open(sys.argv[3], 'rb').read().split(b'\n')
assert len(fix) == len(nums) + 1 or len(fix) == len(nums)
for n, f in zip(nums, fix):
    L[n-1] = f
out = b'\n'.join(L)
open(p, 'wb').write(out)
print(hashlib.sha256(out).hexdigest())
