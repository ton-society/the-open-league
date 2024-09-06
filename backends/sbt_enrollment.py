"""
Simple tool to sync cNFT SBT collection used for enrollment. 
1. Fetches latest cNFT merkle proof hash
2. Requests full lists of SBTs and checks the proof
3. Inserts list of participants into DB

DB structure:

create table tol.enrollment_{season_name} (
  id serial primary key,
  address varchar,
  sbt varchar,
  added_at timestamp
)
"""

class SBTEnrollmentSync(CalculationBackend):
    def __init__(self, connection):
        self.connection = connection

    def sync(self, config: SeasonConfig)
        # TODO