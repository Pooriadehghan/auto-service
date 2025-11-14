from model.da.da import DataAccess
from controller.pdr_controller import *
from model.entity.pdr import Pdr
DataAccess(Pdr)
pdr1=Pdr("dsfsdfseee","wdsd",200)
# print(pdr1)
# add("dsfsdfqq","rrtret",758)
# edit(1,"dssaqw","ioiew",5)
# remove_by_id(6)
print(find_all())


