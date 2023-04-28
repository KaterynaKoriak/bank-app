from core.apps.clients.db_client import execute_db_query


class PopulationDbSteps:
    @staticmethod
    def get_country(country):
        query = f"select * from country where name='{country}'"
        return execute_db_query(query)


population_db_steps = PopulationDbSteps()