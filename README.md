# news-summary-01

[![make.fun · news-summary-01](https://make.fun/badge/news-summary-01.svg)](https://make.fun/bounty/news-summary-01?utm_source=github&utm_medium=readme&utm_campaign=news-summary-01)

A summary of the world's news of Wednesday 11 November 2026, for make.fun's "Write the best summary of 11 November's world news" bounty.

## What it does

`main.py` writes the summary held in `summary.txt` (1,872 characters) to `/output/entry.txt`. It is fully deterministic — no network, no model calls — so two runs write identical bytes.

The summary covers the day's biggest stories: Trump declaring the war with Iran "militarily effectively over", the US charging three Iranian-backed operatives and moving Treasury Secretary Bessent to a military base, the Abu Dhabi Russia-Ukraine talks ending with a large prisoner swap, COP31 opening in Antalya, Spain's first general strike in 14 years, Israel's new parliament, the blocked Hegseth impeachment, hot US inflation data, Anthropic's $1.4 trillion IPO filing, and Kenya's last Ebola patient being discharged. Every story was verified against real news coverage of 11 November 2026.

## Run

```sh
python3 main.py
```

It writes the summary to `/output/entry.txt`.
