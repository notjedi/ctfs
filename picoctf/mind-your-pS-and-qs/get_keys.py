# had to refer https://www.youtube.com/watch?v=o4K5G7W8CbE
# https://www.di-mgt.com.au/rsa_alg.html#practicalkeygen
from Crypto.Util.number import long_to_bytes

c = 240986837130071017759137533082982207147971245672412893755780400885108149004760496
n = 831416828080417866340504968188990032810316193533653516022175784399720141076262857
e = 65537

# using http://factordb.com/index.php
p = 1593021310640923782355996681284584012117
q = 521911930824021492581321351826927897005221

l = (p-1) * (q-1)
d = pow(e, -1, l)

# does adding the n spped this up? smh
message = pow(c, d, n)
print((long_to_bytes(message)))
print(bytes.fromhex(hex(message)[2:]).decode('ascii'))
