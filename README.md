# twilio sms forward

Simple SMS forwarder for Twilio.

Update config.py accourding to your needs:

twilio_number is your Twilio active phone number with SMS support. This is also a number where you will receive incoming SMS

to_numbers is an array of numbers to which a forward will be made

# systemd configuration

/etc/systemd/system/twilio.service
```
[Unit]
Description=Twilio SMS
After=network.target

[Service]
User=kstka
Group=kstka
WorkingDirectory=/home/kstka/twilio/
ExecStart=python3 main.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```
sudo systemctl daemon-reload
sudo systemctl start twilio
sudo systemctl enable twilio
sudo systemctl status twilio
sudo journalctl -u twilio -f
```

# nginx configuration

```
server {
    ...
    location /twilio/ {
        include proxy_params;
        proxy_pass http://127.0.0.1:5000/;
    }
    ...
}
```

# github link

