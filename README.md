# mailto
A simple python script used for sending email via SMTP

## usage
```
usage: mailto.py [-h] [-c CONFIG] [-t TO] [-s SUBJECT] [-b BODY]

A script used for sending email via SMTP.

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
  -t TO, --to TO
  -s SUBJECT, --subject SUBJECT
  -b BODY, --body BODY
```

## how to use it
```
# modify config.json
cp config.json.example config.json

# send mail to single receiver
./mailto.py -s "SUBJECT" -b "BODY" -t "receiver_one@mail.com"

# send mail to multiple receiver
./mailto.py -s "SUBJECT" -b "BODY" -t "receiver_one@mail.com"\
    -t "receiver_two@mail.com"

# pipe your data to mailto.py and use it as mail body
echo "test" | ./mailto.py -s "SUBJECT" -t "receiver_one@mail.com"
```
