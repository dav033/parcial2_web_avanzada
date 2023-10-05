from Config.db import db, ma, app
from models.Package import Production
from datetime import datetime

class ProductionService:
    def create_production(self, user_id):
        
        current_date_time = datetime.now()
        
        current_date = current_date_time.strftime('%Y-%m-%d')
        current_time = current_date_time.strftime('%H:%M:%S')

        new_production = Production(current_date, current_time, None, user_id)
        db.session.add(new_production)
        db.session.commit()
        return new_production