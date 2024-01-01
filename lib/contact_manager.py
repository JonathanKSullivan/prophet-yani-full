from model import db, ContactMessage

class ContactMessageManager:
    @staticmethod
    def add_message(name, email, message):
        new_message = ContactMessage(
            name=name,
            email=email,
            message=message
        )
        db.session.add(new_message)
        try:
            db.session.commit()
            return new_message
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_message_by_id(message_id):
        return ContactMessage.query.get(message_id)

    @staticmethod
    def update_message(message_id, **kwargs):
        message = ContactMessage.query.get(message_id)
        if not message:
            return None
        for key, value in kwargs.items():
            if hasattr(message, key):
                setattr(message, key, value)
        db.session.commit()
        return message

    @staticmethod
    def delete_message(message_id):
        message = ContactMessage.query.get(message_id)
        if message:
            db.session.delete(message)
            db.session.commit()
            return True
        return False

    @staticmethod
    def list_all_messages():
        return ContactMessage.query.all()
