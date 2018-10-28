#!/usr/bin/env python3

import argparse, json, smtplib, sys

email_text = """\
From: {}
To: {}
Subject: {}

{}
"""

def load_json(filename):
    with open(filename, 'r') as f:
        obj = json.load(f)
    return obj

def check_smtp(smtp):
    keys = ['server', 'port', 'username', 'password', 'tls']
    for k in keys:
        if k not in smtp:
            print('[ERR] missing {} in smtp configuration file'.format(k))
            return None
    return smtp

def send_mail(smtp, to, subject, body):
    text = email_text.format(smtp['username'], ", ".join(to), subject, body)
    try:
        if smtp['tls']:
            server = smtplib.SMTP(smtp['server'], smtp['port'])
            server.ehlo()
            server.starttls()
        else:
            server = smtplib.SMTP_SSL(smtp['server'], smtp['port'])
            server_ssl.ehlo()
        server.login(smtp['username'], smtp['password'])
        server.sendmail(smtp['username'], to, text)
        server.close()
        print('Email sent.')
    except Exception as e:
        print('[ERR] {}'.format(e))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description=
            'A script used for sending email via SMTP.'
            )
    parser.add_argument('-c', '--config', default='config.json')
    parser.add_argument('-t', '--to', action='append')
    parser.add_argument('-s', '--subject')
    parser.add_argument('-b', '--body')

    args = parser.parse_args()

    if not args.config:
        parser.print_help()
    else:
        if not ( args.to and args.subject):
            parser.print_help()
            exit(-1)
        else:
            to = args.to
            subject = args.subject

        if not args.body:
            body = sys.stdin.readlines()
            body = ''.join(body)
        else:
            body = args.body

        config = load_json(args.config)
        if 'smtp' not in config:
            print('[ERR] missing smtp section in {}'.format(args.config))
            exit(-1)

        smtp = check_smtp(config['smtp'])

        if smtp:
            send_mail(smtp, to, subject, body)
        else:
            exit(-1)

