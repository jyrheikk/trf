# Create chess Tournament Report Files (TRF)

## Prerequisites

- Create an account in [ChessManager](https://chessmanager.com/).
- Copy the code of this GitHub repository, select **Code – Download ZIP**.
- [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/), used for running the scripts below.

> [!TIP]
> Install a browser add-on to show up-to-date results, say, [Easy Auto Refresh](https://chromewebstore.google.com/detail/easy-auto-refresh/aabcgdmkeabbnleenpncegpcngjpnjkc) for Chrome.

## Creating the input data

1. Create your customized **tournament info**:
- Create a file named `data/input/tournament.trf`.
- Reuse the `data/samples/tournament.trf` template if needed.

Set at least the following information:

ID | Value
-- | -----
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

See the [Tournament Report File format](https://github.com/echecsjs/trf/blob/main/SPEC.md) for more. Note that some data are not supported by ChessManager.

2. Download the **latest ratings** in the `data/input/selolista.csv` file:

```bash
./trfx -d
```

3. Create the **list of participants** (in the `data/input/players.csv` file):

```csv
surname,first,club
Heikkinen,Jyrki,LauttSSK
Koivusipilä,Hannes,LauttSSK
```

> [!NOTE]
> The names are case-insensitive.
> The following data in the participants file are ignored:
> - The first line (header) unless the `-n` (`--no-header`) option is given.
> - Extra fields after the `club` field.

For example, if participants are in Google Sheet,
- export them as CSV, and
- verify that the order of fields is correct.

Verify that all the participants are found from the ratings list:

```bash
./trfx
```

Warning is shown for each player who
- is not found from the ratings list, or
- has no chess license (if the `--license` option is given).

Fix the participant data manually if needed.

## Running tournaments

1. Generate Tournament Report Files, and divide the players into them:

```bash
./trfx -g 10 24 38
```

The numbers after the `-g` option are the **indexes of the last player** in each group.

The files are created in `data/output/tournament-*.trf`.

2. Create tournaments:

- Log in to ChessManager.
- Select **New Tournament**.
- Select **Import From File**, and choose the generated TRF file from the `data/output` directory.

Once the first round has started, add _Club_ for each player if needed.

3. Export results

After a tournament has finished, export its results for rating calculation:
- Select **Dashboard – Basic information – Export – TRF 2026**.

## Other

See the help for all options:

```bash
./trfx -h
```
