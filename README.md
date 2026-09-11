# Tournament Report File for a chess tournament

## Prerequisites

- Create an account in [ChessManager](https://chessmanager.com/).
- Copy the code of this GitHub repository, select **Code** – Download ZIP.
- [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/), used for running the scripts below.

## Creating the input data

1. Download the latest ratings list in the `input/selolista.csv` file:

```bash
uv run -m trf --download-ratings
```

2. Create your customized [Tournament Report File](https://tornelo.com/knowledge-base/trfx-file-format/) named `input/tournament.trf` based on the `tournament.trf` template.

3. Create the `input/players.csv` file that contains the participants one per line:

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
uv run -m trf
```

Fix the player data in `input/players.csv` manually if needed. The player names are case-insensitive.

## Creating tournaments

1. Generate one or more Tournament Report Files in `output/tournament-*.trf`, and divide the players into them:

```bash
uv run -m trf --group-ends 10 24 38
```

The numbers after the `group-ends` argument are the **indexes of the last player** in each group.

2. Create tournaments:

- Log in to ChessManager.
- Select **New Tournament**.
- Select **Import From File**, and choose the generated TRF file from the `output` directory.
- Add the club for each player if needed.
