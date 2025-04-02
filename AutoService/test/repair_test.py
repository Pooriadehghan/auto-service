from model.entity.repairs import Repair
from model.da.da import DataAccess
repair_da=DataAccess(Repair)
repair1=Repair("mojo","dil-255",9000.5,8,1208)

print(repair1)
#repair_da.remove_by_id(1)
#print(repair_da.find_by(repair1.price > 2500))
#print(repair_da.find_all())
repair_da.remove_by_id(3)
