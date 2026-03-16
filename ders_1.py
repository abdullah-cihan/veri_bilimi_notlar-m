import numpy as np
np.random.seed(42)
test_sonuclari=np.random.randint(0,100,size=(4,5)).copy()
gecen_notlar=test_sonuclari[test_sonuclari>50]
gecen_notlar+=10
gecen_notlar.mean()
test_sonuclari.mean()

#burada kskdsdksdsd
