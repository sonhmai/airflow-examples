"""
Hooks should be used when interacting with external system.
Hooks provide interface to interact with an external system.

All hooks inherit from BaseHook which contains logic for how hooks
interact with Connections. Connections are Airflow's built-in cred-store
for source/destination systems.
"""
from airflow.contrib.hooks.aws_hook import AwsHook
try:
    from airflow.hooks.postgres_hook import PostgresHook
except ImportError:
    from airflow.providers.postgres.hooks.postgres import PostgresHook


def load_data_to_redshift(*args, **kwargs):
    aws_hook = AwsHook('aws_credentials')
    credentials = aws_hook.get_credentials()
    redshift_hook = PostgresHook('redshift')
    sql_stmt = sql.COPY_STATIONS_SQL.format(
        credentials.access_key,
        credentials.secret_key
    )
    redshift_hook.run(sql_stmt)



