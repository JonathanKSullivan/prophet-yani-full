#!/bin/bash

# Secrets for your Flask application
export FLASK_APP_SECRET_KEY='9mNzVK6gyqR2Vl3BRud4LW1wS5TGHoJp'

# AWS Credentials
export AWS_ACCESS_KEY_ID='AKIAW6KYM2GOBFIY3LWF'
export AWS_SECRET_ACCESS_KEY='ZY68fr+/d9VhmNj0YhHy5VbaFrB5FdUE+PEWKsyQ'
export AWS_DEFAULT_REGION='us-east-2'

# Database Credentials (if applicable)
export DATABASE_URL='sqlite:///prophet_yani_dev.db'
export DATABASE_WRITER_URL='postgresql://postgres:postgres@database-2.c96cgiewsw34.us-east-2.rds.amazonaws.com/postgres'
export DATABASE_READER_URL='postgresql://postgres:postgres@database-2.c96cgiewsw34.us-east-2.rds.amazonaws.com/postgres'

# Flask and Security Settings:
export SECURITY_PASSWORD_SALT='gEqjCI2sfn+7bynRmslvlwNR/GiNGuH29H6WgIIzuuQ='
export SECRET_KEY='Ybg3vUcN6SlxUWHzNWCSmWAxihbzZc04IEvB35mz9B127JWd8VkbJsvpaXF/ucKj'

# Gmail Credentials
export MAIL_USERNAME='SullivanSoftwareSolutions@gmail.com'
export MAIL_PASSWORD='omib pebi rwua mrsk'
export MAIL_DEFAULT_SENDER='jonathan.k.sullivan@gmail.com'

# Stripe Credentials
export STRIPE_PROD_PUBLIC_KEY='pk_live_51ORmDrBO4RqVDnuZ6f52FrLQyRDtSmx0LWhyySxjGB2WgywLjmaZ2ll8TOfyuM1ed8ZjZPlOi35qLJ5pVE8HbTxh000JWBuD8S'
export STRIPE_PROD_SECRET_KEY='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'
export STRIPE_TEST_PUBLIC_KEY='pk_test_51ORmDrBO4RqVDnuZuqrlnOyhWBEJELt57CAxDpJDfcW7eVRFm1T4QwF9Sbhd0x1Vpb9iA1QOof1nU4PZvQZChS500036lqa94e'
export STRIPE_TEST_SECRET_KEY='sk_test_51ORmDrBO4RqVDnuZ25SgvZLlo1HTt7RbNwlUbHnaeU2DdiiDugQRratl1G6FTtsfN7K69pfJn9GCvsNPYYMkNONX00m35NJUPM'
