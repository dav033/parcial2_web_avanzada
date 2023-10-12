from Config.db import db, ma, app
from models.Package import Packages
from datetime import date
from utils import utils


class PackageService:
    def getPackage(self,user_id,type):
        package = Packages.query.filter_by(user_id=user_id,product=type,is_complete=0).first();
        return package
    def UpdatePackage(self, package:Packages,count):
        total_count=package.products_count+count
        if total_count > 12:
            package.products_count=12
            package.is_complete=1
            package.total_package_value = utils.getTotalPackagevalue(package.product,package.user_id)
            db.session.commit()
            excedente = total_count - 12
            if excedente > 0:
                new_package = self.createPackage(package.user_id,package.product,1)
                self.UpdatePackage(new_package,excedente-1)
            else:
                return True 
        else:
            package.products_count=total_count
            if total_count==12:
                package.is_complete=1
            db.session.commit()
        
    def createPackage(self, user_id,type,count=1):
        if count>12:
            newPackage = Packages(date.today(), type,user_id,0,0,0)
            db.session.add(newPackage)
            db.session.commit()
            self.UpdatePackage(newPackage,count)
        else:
            newPackage = Packages(date.today(), type,user_id,0,count,0)
            db.session.add(newPackage)
            db.session.commit()
        return newPackage