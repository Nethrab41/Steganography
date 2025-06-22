import numpy as np
from PIL import Image
from IPython.display import display

d={chr(i):i for i in range(255)}#char to ascii
c={i:chr(i) for i in range(255)}#ascii to char

#message and encryption key
text="Hello"
key="key"

#random pixel value image dummy 10x10 image
x=np.random.randint(0,255,(10,10,3),dtype=np.uint8)

#Having an Image
image_path="/content/god.jpg"
pic=Image.open(image_path)
display(pic)
x=np.array(pic)

#encryption
x_enc=x.copy()
n=0 #row
m=0 #column
z=0 #channel
l=len(text)
kl=0 #index for key
for i in range(l):
  char_val=d[text[i]]^d[key[kl]]
  for bit_pos in range(8):
    bit=(char_val >> (7-bit_pos))&1 #important
    orig_val=x_enc[n,m,z]
    x_enc[n,m,z]=(orig_val & 254) | bit #important 1101101 1 0
    print(f"Writing bit {bit} of '{text[i]}' at ({n},{m},{z}) original={orig_val} new={x_enc[n,m,z]}")
    z=(z+1)%3
    if z==0:
      m=m+1
      if m==x_enc.shape[1]:
        m=0
        n=n+1
  kl=(kl+1)%len(key)
  encrypt_pic=Image.fromarray(x_enc)
  display(encrypt_pic)

#decryption
n,m,z=0,0,0
kl=0
decrypt=""
for i in range(l):
  val=0
  for bit_pos in range(8):
    bit=x_enc[n,m,z]&1
    val=(val << 1) | bit
    print(f"Reading bit {bit} from ({n},{m},{z})")
    z=(z+1)%3
    if z==0:
      m=m+1
      if m==x_enc.shape[1]:
        m=0
        n=n+1
  orig_char=c[val^d[key[kl]]]
  decrypt+=orig_char
  kl=(kl+1)%len(key)
print("decrypt text",decrypt)
