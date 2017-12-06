# BrewerBot
This is a wrapper around [os/slacker](http://github.com/os/slacker). You need to give it a webhook for your slack channel, as well as the name of the channel you want messages to be sent in. Here's how to do that:

## Set the webhook (api_token):
When initializing a new `BrewerBot`, it will first look for an environment variable called `brewer_token`. Set that beforehand by running:
```
$ export brewer_token="xoxo-your-token-here-xoxo"
```
If you want to set the token more permanantly, you can write it to `~/slack.token`. Be sure it's just the key, and there's no whitespace or comments or anything. Just the key.

The `brewer_token` environment variable will take precedence over the `~/slack.token` file. Unset it if you need to.

## Set the channel
By default the channel is set to `'@luke'`. This is a PM to me, so my people don't get annoyed when I test things out. Like the token, you can set this with an environment variable.
```
$ export brewer_channel="#your_channel"
```
Remember that if it's a channel, use `"#channel"`, and if it's a private message, use `"@person"`.
