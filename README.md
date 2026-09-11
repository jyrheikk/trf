# Tournament Report File for a chess tournament

## Prerequisites

- Create an account in [ChessManager](https://chessmanager.com/).
- Copy the code of this GitHub repository, select **Code** – Download ZIP.
- [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/), used for running the scripts below.

## Creating a tournament

1. Download the latest `selolista.csv`:

```bash
uv run -m trf --download-ratings
```

2. Create your customized [Tournament Report File](https://tornelo.com/knowledge-base/trfx-file-format/) based on `tournament.trf`.

3. Create the `players.csv` file that contains the participants one per line:

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
uv run -m trf --players players.csv
```

Fix the player data in `players.csv` if needed. Player names are case-insensitive.

5. Generate one or more tournament files, and divide the players into them:

```bash
uv run -m trf --players players.csv --tournament my_tournament.trf --group_ends 10 24 38
```

The numbers after the `group_ends` argument are the **indexes of the last player** in each group.

6. Create tournaments:

- Log in to ChessManager.
- Select **New Tournament**.
- Select **Import From File**, and choose the generated TRF file.
- Add the club for each player if needed.
