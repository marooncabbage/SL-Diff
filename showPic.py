from torchvision.utils import save_image, make_grid
import numpy as np
import torch
import matplotlib.pyplot as plt
import torch
from torchvision.utils import save_image
import torchvision
a = torch.randn(1, 3, 4, 4)
b = torch.randn(1, 3, 4, 4)
c = torch.randn(1, 3, 4, 4)
d = a[0]


e = torch.stack([a[0], b[0], c[0]], dim=0)

save_image(e, './hh.png')
# e=torch.cat([a[0],b[0],c[0]],dim=3)



def show(img):
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1,2,0)), interpolation='nearest')


def show_images(images,path):
    c=images.shape[0]
    l=images.shape[1]
    h=int(pow(l,0.5))+1
    pad = torch.zeros([c, h*h - l])
    images = torch.cat((images, pad), dim=1)
    images = torch.reshape(images, (c, 1, h, -1))
    save_image(images, path)


images = torch.FloatTensor(np.random.normal(0, 1, (32, 2810)))



print(images.shape)

show_images(images,'./hh.png')




#show(make_grid(images, nrow=5, padding=10, pad_value=0))
#plt.show()

