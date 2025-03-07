from model.da.da import DataAccess
from model.entity.acceptance import Acceptance

# Unit Test
acceptance = Acceptance("benz", "c200", 2002, "black", "12b123iran11", "ABNM132456887", "mr.dehghan", "09372352663"
                        , 111225, "pdr","2024-02-03")

acceptance_da = DataAccess(Acceptance)
acceptance_da.save(acceptance)

print(acceptance)
