# airflow-examples
Examples of using airflow

## Components
### Webserver
### Scheduler
- monitors and stays in sync with a folder for all DAG objects it may contain, and periodically (every minute or so) collects DAG parsing results and inspects active tasks to see whether they can be triggered.

- [ ] What launches executors?

## Models
- DAG: the work, order in which work should take place.
- DAG Run: instance of DAG for particular logical date and time.
- Operator: class as template for doing work.
- Task: defines work by implementing operator.
- Task Instance: instance of task that has been assigned to DAG and has a state
associated with specific DAG run.
- execution_date: logical date time for a DAG Run and its task instances.

## Steps to Create and Run Dag

### How to get a dag recognized by Airflow?
- define your dag python file in `dags_folder` config of `airflow.cfg`
- run `airflow list_dags` to see if your dag was added 
- `airflow list_tasks dag_id [--tree]` # list tasks of dag, add --tree to se hierarchy

Airflow parses all DAGs in the background at a specific period. Default period set by `processor_poll_interval` config (default 1sec).

When searching for DAGs, Airflow only considers python files that contain the strings “airflow” and “DAG” by default. To consider all python files instead, disable the `DAG_DISCOVERY_SAFE_MODE` configuration flag.

### My dag does not show up on Web UI?
- [ ] check your dag filename, it does not include string "dag"?
- [ ] Restart the scheduler. Scheduler periodically parses dag folders.