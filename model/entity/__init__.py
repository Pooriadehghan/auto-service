from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship

from model.entity.base import Base
from model.entity.carwash import CarWash
from model.entity.acceptance import Acceptance
from model.entity.periodic_service import PeriodicService
from model.entity.repairs import Repair
from model.entity.admin import Admin
from model.entity.user import User
from model.tools import *
