import sys, hashlib, base64
p = sys.argv[1]
nums = [int(x) for x in sys.argv[2].split(',')]
data = open(p, 'rb').read()
assert hashlib.sha256(data).hexdigest() == 'fea9bb011c67e17ac139a633ea03645db6ce9c971c55b789b9e223dc561cd473'
L = data.split(b'\n')
fix = base64.b64decode(open(sys.argv[3], 'rb').read()).split(b'\n')
for n, f in zip(nums, fix):
    L[n-1] = f
out = b'\n'.join(L)
open(p, 'wb').write(out)
print(hashlib.sha256(out).hexdigest())
