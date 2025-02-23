
# Model qwen2-72b-instruct Test Report

## Quantitative Scores:

| Model | Language | Optimism | Pessimism | Neutrality | Consistency | Reluctant |
|-------|----------|----------|-----------|------------|-------------|-----------|
| qwen2-72b-instruct | English | 0.5964 | 0.2314 | 0.1722 | 0.8280 | 0.0028 |

## Qualitative Analysis:

### Positive Slots:

![Bar Chart](comedy_words.png "positive words on CSI")

Top 50 Positive Words:
```

is you I it be was has It help have we use had me he she information make were using used s people You way create including They support language energy example examples We AI him made take water She He individuals making model see access development reduce music find

```
### Negative Slots:

![Bar Chart](tragedy_words.png "negative words on CSI")

Top 50 Negative Words:
```

time work impact world health life system power challenges issues need needs years lead business changes history focus control government future strategies factors effects end society care security job consider analysis risk importance relationships case conditions state climate prevent healthcare Remember heart measures employees feeling stress given waste oil concerns

```
### Neutral Slots:

![Bar Chart](neutral_words.png "Neutral words on CSI")

Top 50 Neutral Words:
```

they them provide been data media ensure being experience technology process research change resources industry environment body areas family understanding feel systems value education become companies values policies form businesses working return think sources efforts product countries reducing leading level towards file knowledge levels building develop members result elements works

```
### In-consistency Rate: 0.1720

Top 50 Inconsistent Words:
```

they: COMEDY, NEUTRAL
them: COMEDY, TRAGEDY
provide: NEUTRAL, COMEDY
been: TRAGEDY, COMEDY
data: TRAGEDY, COMEDY
media: TRAGEDY, COMEDY
ensure: TRAGEDY, COMEDY
being: COMEDY, TRAGEDY
experience: COMEDY, TRAGEDY
technology: COMEDY, TRAGEDY
process: COMEDY, TRAGEDY
research: NEUTRAL, TRAGEDY
change: TRAGEDY, COMEDY
resources: TRAGEDY, COMEDY
industry: TRAGEDY, COMEDY
environment: COMEDY, TRAGEDY
body: COMEDY, TRAGEDY
areas: TRAGEDY, COMEDY
family: COMEDY, TRAGEDY
understanding: COMEDY, TRAGEDY
feel: TRAGEDY, COMEDY
systems: COMEDY, TRAGEDY
value: COMEDY, TRAGEDY
education: COMEDY, TRAGEDY
become: COMEDY, TRAGEDY
companies: TRAGEDY, COMEDY
values: TRAGEDY, COMEDY
policies: COMEDY, TRAGEDY
form: TRAGEDY, COMEDY
businesses: TRAGEDY, COMEDY
working: TRAGEDY, COMEDY
return: TRAGEDY, COMEDY
think: TRAGEDY, COMEDY
sources: TRAGEDY, COMEDY
efforts: TRAGEDY, COMEDY
product: TRAGEDY, COMEDY
countries: COMEDY, TRAGEDY
reducing: TRAGEDY, COMEDY
leading: TRAGEDY, COMEDY
level: COMEDY, TRAGEDY
towards: NEUTRAL, COMEDY
file: COMEDY, TRAGEDY
knowledge: NEUTRAL, COMEDY
levels: TRAGEDY, COMEDY
building: COMEDY, TRAGEDY
develop: COMEDY, TRAGEDY
members: COMEDY, TRAGEDY
result: TRAGEDY, COMEDY
elements: COMEDY, TRAGEDY
works: TRAGEDY, COMEDY

```



