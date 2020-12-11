
# Examples
- [x] What launches the executor in general? The sequential executor 
  specifically?  
  The scheduler is responsible for executor launching by
    - LocalExecutor - it forks a new process.
      
    - KubernetesExecutor - it talks to KubeAPI to launch a pod running the task.
      The pod will then run 
      
      `airflow run dagid taskid`

# Kubernetes Executor
- K8s Exec run as process in Scheduler. When DAG submits a task, k-exec
  requests a pod from K8s-API, worker pod runs task, reports result, terminates.
- The plan is to launch Scheduler, Webserver locally and k8s execs on minicube.
- Difference
  - KubernetesPodOperator used to create pod, can be used by any executor.
  - Kubernetes Executor used to exec task specified by an Operator.
  
TODO
- [ ] Add postgres docker as a database backend for airflow because k8s
  executor can't access local sqlite db to write results and sqlite does not 
  support concurrency.
    - [x] install postgres `sudo apt install postgresql postgresql-contrib`
    - [x] create airflow user, db, init
  ```
  sudo -u postgres createuser --interactive --prompt
  sudo -u postgres createdb airflow
  export AIRFLOW_HOME=<path-contains-config>
  airflow initdb
  ```
  
- [ ] Modify airflow.cfg
  - [x] Change executor to KubernetesExecutor
  - [x] Change sqlalchemy conn to metadata db from sqlite to postgres
  - [ ] Specify in kubernetes section dag configs. (In kubernetes mode the 
    following must be set in the `kubernetes` config section: `dags_volume_claim` 
    or `dags_volume_host` or `dags_in_image` or
    `git_repo and git_branch and git_dags_folder_mount_point`).
- [ ] How to change how airflow load kubenetes config? default path of k8s 
  executor is to load_incluster_config(), which 
  will raise an exception if called from a process not running in k8s env.
- [ ] Set up and use a simple Kubernetes Executor

# Deployment
- [x] Debug stop-local bash script and Makefile. 
  -> Don't use makefile, it introduces unnecessary complexity at the moment
