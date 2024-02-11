# learn_imap_yahoo

Simple python program to open a Yahoo email account and list the folders and the number of message in each folder.

## Step 1: Generate a Yahoo application password

Go to [Yahoo|https://www.yahoo.com] and follow the steps there to generate an application password.

## Step 2: Add environment variables

You will need to set two environment variables to log into your Yahoo account.

```bash
export YAHOO_USER=`echo -n "yourname@yahoo.com" | base64`
export YAHOO_PW=`echo -n "shzmkjosjohwnkqa" | base64`
```

You can test they are set up properly by running these commands.

```bash
echo $YAHOO_USER | base64 --decode
echo $YAHOO_PW | base64 --decode
```

## Step 3: How to run

Copy this file to your $HOME/Applications folder.
python learn_imap_yahoo.py

## Testing and Assumptions

This program was tested on a Macbook Air using iTerm2 (a better alternative to the terminal).
You should be using Python3 and it should be in your PATH when you run this program.

## Supporting Documentation

* [Yahoo IMAP Server Settings|https://help.yahoo.com/kb/SLN4075.html]
