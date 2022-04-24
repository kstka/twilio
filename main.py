from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import config


app = Flask(__name__)
client = Client(config.account_sid, config.auth_token)


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """ Send a dynamic reply to an incoming text message """
    body = request.values.get('Body', None)
    resp = MessagingResponse()
    for to_number in config.to_numbers:
        try:
            message = client.messages \
                    .create(
                         body=body,
                         from_=config.twilio_number,
                         to=to_number
                     )
        except TwilioRestException as e:
            print(f"Error sending to {to_number}: {e}")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)

