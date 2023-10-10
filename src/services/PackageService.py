from Config.db import db, ma, app
from models.Package import Packages
from datetime import date

class PackageService:
    def getPackage(self,user_id,type):
        package = Packages.query.filter_by(user_id=user_id,product=type,is_complete=0).first();
        return package
    def UpdatePackage(self, package):
        package.products_count += 1
        if package.products_count==12:
            package.is_complete=1
            package.date = date.today()
        db.session.commit()
        return package;
    def createPackage(self, user_id,type):
        newPackage = Packages(date.today(), type,user_id,0,1,0)
        db.session.add(newPackage)
        db.session.commit()
        return newPackage