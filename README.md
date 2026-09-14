# Create Tournament Report File(s) for a chess tournament

You need two files:
- List of registrants.
- List of the latest ratings.

To speed up creating several groups in a tournament, you may want to create the third file:
- Tournament info.

## Prerequisites

- Create an account in [ChessManager](https://chessmanager.com/).
- Copy the code of this GitHub repository, select **Code** – Download ZIP.
- [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/), used for running the scripts below.

## Creating the input data

1. Download the latest ratings list in the `data/input/selolista.csv` file:

```bash
./trfx -d
```

2. Create your customized [Tournament Report File](https://tornelo.com/knowledge-base/trfx-file-format/) named `data/input/tournament.trf` based on the `tournament.trf` template.

3. Create the `data/input/players.csv` file that contains the participants one per line:

```csv
last-name,first-name,club
Carlsen,Magnus,2823
Heikkinen,Jyrki,2062
```

The following data in the file are ignored:
- The first line, which should be a header.
- Extra fields after the `club` field.

For example, if registrations are in Google Sheet,
- export them as CSV, and
- verify that the order of fields is correct.

4. Verify that all the registrants are found from the ratings list:

```bash
./trfx
```

Fix the player data in `data/input/players.csv` manually if needed. The player names are case-insensitive.

## Running tournaments

1. Generate one or more Tournament Report Files in `data/output/tournament-*.trf`, and divide the players into them:

```bash
./trfx -g 10 24 38
```

The numbers after the `g` argument are the **indexes of the last player** in each group.

2. Create tournaments:

- Log in to ChessManager.
- Select **New Tournament**.
- Select **Import From File**, and choose the generated TRF file from the `data/output` directory.

Having started the first round, add _Club_ for each player if needed.

3. Export results

After a tournament has finished, export its results for rating calculation:
- Select _Dashboard – Basic information – Export – TRF 2026_.

## Other

For all options, see

```bash
trfx --help
```
