# Generator of flexible job shops

Flexible job shop scheduling problems are a generalization of classical job shop scheduling problems which allows an operation to be processed by a subset of machines.
Furthermore, an operation has machine-dependent processing times.<br>

Running the following code generates an instance of such a problem
```
python3 main.py [-pmin PROCESSING_TIME_MIN] [-pmax PROCESSING_TIME_MAX]
                [-dp DELTA_PROCESSING_TIME] [-am AVG_ASSIGNED_MACHINES]
                [-mm MAX_ASSIGNED_MACHINES]
                jobs machines
```

Afterwards, the instance is stored in `./Instances/` which is created as explained in `./Instances/DataSetExplanation.txt`. Some examples with varying problem sizes can be found in `./stances/jawaid/`.

## Background and assumptions

The parameters `jobs` and `machines` not only determine the number of jobs and machines in a flexible job shop scheduling problem, `machines` also equals the number of operations of each job.<br>

As mentioned above, a flexible job store scheduling problem allows an operation to be processed by a subset of machines. In this generator, the subset is bounded by the parameters `max_assigned_machines` and `avg_assigned_machines`. Thus, the maximum and the average number of machines assigned to an operation are determined by `max_assigned_machines` and `avg_assigned_machines`. According to "Tabu Search for the Job-Shop Scheduling Problem with Multi-Purpose Machines" Hurink et. al, 1994.<br>

Additionally, processing times of operations are limited. On the one hand, processing times are limited over a entire scheduling problem by `processing_time_min` and `processing_time_max`. On the other hand, `delta_processing_time` defines the difference of processing times within operations.
