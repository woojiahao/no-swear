# no-swear

Telegram Bot used for Project Intern to moderate swear words

## Getting Starting

To get started, clone the repository and install all requirements:

```sh
git clone https://github.com/woojiahao/no-swear.git
cd no-swear
pip install -r requirements.txt
```

Then, copy `.env.example` and rename it to `.env`. Set the bot token in `.env`.

```sh
cp .env.example .env
vim .env
```

Update the blacklist as you see fit, found in `__main__.py`.

Run the bot:

```sh
python __main__.py
```
