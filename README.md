# Create chess Tournament Report Files (TRF)

## Features

- Creates Tournament Report Files for the given number of groups to be played, using the given
   - tournament information file, and
   - list of participants.
- Adds a rating and FIDE number for each player from the fetched ratings list.

## Prerequisites

- Create an account in [ChessManager](https://chessmanager.com/).
- Copy the code of this GitHub repository, select **Code – Download ZIP**.
- [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/), used by the `trfx` script.

> [!TIP]
> Install a browser add-on to show up-to-date results, say, [Easy Auto Refresh](https://chromewebstore.google.com/detail/easy-auto-refresh/aabcgdmkeabbnleenpncegpcngjpnjkc) for Chrome.

## Creating the input data

### Create customized tournament information

- Create a file named `data/input/tournament.trf`.
- Reuse the `data/samples/tournament.trf` template if needed.

Set at least the following tags:

Tag | Value
--- | -----
012 | Tournament name, `{GROUP}` is automatically set as `A`, `B` etc.
022 | Name of the city where the tournament is played
032 | 3-letter country code (e.g., `FIN`)
042 | Tournament start date (YYYY/MM/DD)
052 | Tournament end date (YYYY/MM/DD)
102 | Tournament arbiter
202 | Tie-breaks (see below)
XXR | Number of rounds

For example, `BH/P,SB/P,DE/P,WIN,PS` are the default tie-breaks in Finnish tournaments:
1. Buchholz
2. Sonneborn-Berger
3. Direct Encounter
4. Number of Wins
5. Progressive Score

See the [Tournament Report File format](https://github.com/echecsjs/trf/blob/main/SPEC.md) for more. Note that some tags are not supported by ChessManager.

### Download the ratings

Download the latest ratings (in the `data/input/selolista.csv` file):

```bash
./trfx --download
```

### Create the list of participants

The list (in the `data/input/players.csv` file) must include the following fields:

```csv
surname,first,club,initial rating
Heikkinen,Jyrki,LauttSSK
Sindarov,Javokhir,,2778
```

The names are case-insensitive. The following data are _ignored_:
- The first line (header) unless the `--no-header` option is given.
- Extra fields after the `initial rating` field.

Set the initial rating for a new player if needed. In Finland, it is
- Elo rating,
- 1325 (U10),
- 1425 (U14), or
- 1525 (default).

For example, if the participants are in Google Sheet,
- export them as CSV, and
- verify that the order of fields is correct.

Verify that all the participants are found from the ratings list:

```bash
./trfx
```

Warning is shown for each player who
- is not found from the ratings list, or
- needs a chess license (has none, and has played over 10 games) if the `--license` option is given.

Fix the participant data manually if needed.

## Running tournaments

### Generate Tournament Report Files

Generate TRFs, and divide the players into them:

```bash
./trfx --groups 10 24 38
```

The numbers after the `--groups` option are the **index of the last player** in each group.

The files are created in the `data/output/tournament-*.trf` files.

### Create tournaments

- Log in to ChessManager.
- Select **New Tournament**.
- Select **Import From File**, and choose a generated TRF file from the `data/output` directory.

Once the first round has started, add _Club_ for each player if needed.

### Export results

After the tournaments have finished, export their results for rating calculation:
- Select **Dashboard – Basic information – Export – TRF 2026**.

## Other

See the help for all options:

```bash
./trfx --help
```
