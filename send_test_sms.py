from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import config


if __name__ == "__main__":
    client = Client(config.account_sid, config.auth_token)
    try:
        message = client.messages \
                .create(
                     body='This is a test message, dude!',
                     from_=config.twilio_number,
                     to=config.to_numbers[0]
                 )
    except TwilioRestException as e:
        print(f"Error sending to {config.from_number}: {e}")

