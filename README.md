# Weirdo
Weirdo is a Python-based Slack-bot designed to store and regurgitate quotes. Quotes are stored in JSON format and managed by TinyDB. Weirdo was designed to run in CloudFoundry and store its database in an Amazon S3 bucket. 

- [Getting started](#getting-started)
- [Configuration](#configuration)
- [Supported commands](#supported-commands)
- [Development](#development)
- [Deployment](#deployment)

# Getting started
The instructions below assume you are setting up a Python virtual environment using virtualenv.

First, instantiate your virtual environment using Python 3.7 or higher.
```
virtualenv venv
```
Install dependencies.
```
venv/bin/pip -r requirements.txt
```
Make sure the folder where you wish to store your database exists. In this example, the database will be named `db.json` and stored in the `db` folder. 
```
mkdir db
```
(Re-)populate the sing database, if desired.
```
DB_PATH=db/db.json venv/bin/python scripts/resetsong.py
```

As a Slack-bot, Weirdo requires a Slack app to talk to. The app in question is identified by means of a Slack API token, which can be generated in the Slack app settings. 

Run weirdo.
```
SLACK_API_TOKEN=<your Slack token> venv/bin/python src/__main__.py
```
If all goes well, this should output `Connection established`.

To verify your install, you can run the unit tests.
```
venv/bin/pytest
```


# Configuration
Weirdo is configured by means of environmental variables. The assignment of these should either precede the `python` command or be set globally by `export`ing. I.e. `<variable_name>=<desired_value> venv/bin/python`.

## SLACK_API_TOKEN
Weirdo needs to know which Slack instance it should be talking to. A Slack API token can be generated by creating a Slack App, attaching it to your Slack project, and generating an API token in the app settings. 

## DB_PATH
The path to the JSON database. The `db` folder is ignored by default in `.gitignore`, so `db/db.json` makes an obvious choice.

## WEIRDO_ENV
If set to 'S3', Weirdo will synchronize with the Amazon S3 bucket designated by the `S3_BUCKET`, `AWS_ACCESS_KEY_ID`, and `AWS_SECRET_ACCESS_KEY` variables described below. 

## S3_BUCKET
The name of the S3 bucket that stores the databse. Only required if `WEIRDO_ENV` is set to 'S3'.

## AWS_ACCESS_KEY_ID
Credentials for the designated S3 bucket. Only required if `WEIRDO_ENV` is set to 'S3'.

## AWS_SECRET_ACCESS_KEY
Credentials for the designated S3 bucket. Only required if `WEIRDO_ENV` is set to 'S3'.


# Supported commands
When chatting with weirdo, messages the begin with the following strings will be interpreted as commands to execute. The rest of the message will be passed as a parameter. E.g. opening a Slack channel to Weirdo and sending the message `sq cookies are awesome` will search the database for quotes containing the text "cookies are awesome". 

## sq
Will search the database for three random quotes that contain the text described by the rest of the message. Searches will ignore case.

### Example
```
sq Bob
```
Output
```
00001 Bob said this thing.
00005 I love to bob my head.
00003 Sally mentioned Bob in a quote.
```


## aq
Appends the rest of the message to the quote database as a new quote and echoes the new quote as confirmation. 

### Example
```
Bob said another thing!
```
Output
```
Quote 00006 added.
```


## lq
If followed by a valid quote id, the quote with that id and the nine subsequent quotes will be returned. If no id is provided, will return the last ten quotes added to the database. 

### Example 
```
lq 00020
```
Output
```
00020 Someone said ten things.
00019 Someone said nine things.
00018 Someone said eight things.
00017 Someone said seven things.
00016 Someone said six things.
00015 Someone said five things.
00014 Someone said four things.
00013 Someone said three things.
00012 Someone said two things.
00011 Someone said one thing.
```


## sing
Outputs lyrics from the song _Creep_ by Radiohead sequentially. Ignores all parameters. 

### Example
```
sing
```
Output
```
When you were here before
```


# Development
Weirdo's Slack interface can be circumvented by calling `handlemessage.py` directly from the command line. This calls `handle_message()` with the parameters provided in the call. The function takes three arguments:
|||
| --------- | ---------------------------------------------------------------------------- |
| `user_id` | The Slack id of the user sending the message. |
| `command` | The desired command as found under [Supported commands](#Supported-commands) |
| `input` | Parameter for command call. |

### Example
```
DB_PATH=db/db.json venv/bin/python src/handlemessage.py 1 sq bob
```
Output
```
00001 Bob said this thing.
00005 I love to bob my head.
00003 Sally mentioned Bob in a quote.
```


# Deployment
Weirdo can be deployed to a suitable CloudFoundry container using the [`cf` command line interface](https://docs.run.pivotal.io/devguide/deploy-apps/deploy-app.html). [Log in](https://docs.cloudfoundry.org/cf-cli/getting-started.html), select a container, make sure to configure the container's environmental variables, and push. All necessary meta-data *should* be in `manifest.yml`. 
