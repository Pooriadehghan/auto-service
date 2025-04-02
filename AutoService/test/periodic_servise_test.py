from model.entity.periodic_service import PeriodicService
from model.da.da import DataAccess
periodic_service=PeriodicService("moggt",66,878)
periodic_service.id=2
pservice_da=DataAccess(PeriodicService)
pservice_da.edit(periodic_service)
