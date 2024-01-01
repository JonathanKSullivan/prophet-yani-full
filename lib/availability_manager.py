from model import db, AvailabilityRule, ExclusionDate, GlobalExclusionDate

class AvailabilityManager:
    @staticmethod
    def add_availability_rule(day_of_week, start_time, end_time, priority=0, is_recurring=True):
        new_rule = AvailabilityRule(
            day_of_week=day_of_week,
            start_time=start_time,
            end_time=end_time,
            priority=priority,
            is_recurring=is_recurring
        )
        db.session.add(new_rule)
        try:
            db.session.commit()
            return new_rule
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def add_exclusion_date(availability_rule_id, date):
        exclusion = ExclusionDate(
            availability_rule_id=availability_rule_id,
            date=date
        )
        db.session.add(exclusion)
        try:
            db.session.commit()
            return exclusion
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def add_global_exclusion_date(date):
        global_exclusion = GlobalExclusionDate(date=date)
        db.session.add(global_exclusion)
        try:
            db.session.commit()
            return global_exclusion
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_availability_rule_by_id(rule_id):
        return AvailabilityRule.query.get(rule_id)

    @staticmethod
    def update_availability_rule(rule_id, **kwargs):
        rule = AvailabilityRule.query.get(rule_id)
        if not rule:
            return None
        for key, value in kwargs.items():
            if hasattr(rule, key):
                setattr(rule, key, value)
        db.session.commit()
        return rule

    @staticmethod
    def delete_availability_rule(rule_id):
        rule = AvailabilityRule.query.get(rule_id)
        if rule:
            db.session.delete(rule)
            db.session.commit()
            return True
        return False

    @staticmethod
    def list_all_availability_rules():
        return AvailabilityRule.query.all()

    @staticmethod
    def list_all_global_exclusions():
        return GlobalExclusionDate.query.all()
    
    # You may add more methods as necessary for other functionalities
