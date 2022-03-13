# Post to Facebook

Thanks to:
- http://nodotcom.org/python-facebook-tutorial.html
- https://softwaredev3loper.wordpress.com/2016/10/09/posting-to-facebook-using-python/
- https://stackoverflow.com/questions/48579740/how-to-write-a-post-on-facebook-using-python

-------------------------------------------------------------------

## Setup facebook python api

https://github.com/mobolic/facebook-sdk
https://facebook-sdk.readthedocs.io/

```bash
# create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# install sdk
pip install facebook-sdk
```

-------------------------------------------------------------------

## Collect all the necessary tokens, etc

Create a new app: https://developers.facebook.com/apps/

Store the:
- PageID: XXXXXXXXXXXXXXXXXX
- App ID: XXXXXXXXXXXXXXX
- App secret: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Get Graph API tokens: https://developers.facebook.com/tools/explorer/
Select correct app from drop down and store the user token.

```bash
# User token is very long. Example:
"EAADuzOK3RP0BAA8Q9GUsO233U9wX9n2ZApdJ52m66LEGuZBBRgLXbMP0kMMNNnSuGVoL4WcS7edGdapItJurrErZAoHvzDr3YZAjTT5V8uWUdjhG4ZAttIeZA7P3KjgyM98ZCNZBGRwrC6ISj4lDKo8TomaZC7L7xXoukLNGmtX3ecSwFOLrtc4UZBESyzA8gYpcasYw7SUyBM8dCN4vhJuqumFfgCZBOk736j4ZD"
```

Convert token to long-lived token. Also remove the curly brackets

-------------------------------------------------------------------


```plain
https://graph.facebook.com/oauth/access_token?
	client_id={APP_ID}&
	client_secret={APP_SECRET}&
	grant_type=fb_exchange_token&
	fb_exchange_token={EXISTING_ACCESS_TOKEN}

token type: bearer

https://graph.facebook.com/oauth/access_token?client_id=XXXXXXXXXXXXXX&client_secret=XXXXXXXXXXXXXXXXXXXXXXXXX&grant_type=fb_exchange_token&fb_exchange_token=
```
