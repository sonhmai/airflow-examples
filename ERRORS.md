# Common Errors

### kubernetes.config.config_exception.ConfigException: Service host/port is not set.
- By default, k8s cluster config is check in file ~/.kube/config. Check if 
  this file is present.
- If local, you might have not started your minicube/ local k8s cluster.
- If remote k8s cluster, check if you have config file to connect to cluster.
You might have to fetch cluster config from cloud provider.
  
### Executor pod does not start (Pending, Error, ..)
- Use `kubectl describe pod <pod-name>` to see what's wrong.

### KubernetesExecutor: task failed but Pod was deleted, no logs to debug
- set airflow.cfg: `kubernetes.delete_worker_pods=False` (default True) so that
Airflow keeps failed pod, we can inspect logs.
