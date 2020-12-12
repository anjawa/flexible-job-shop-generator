import argparse

import random
import numpy as np


def generate_fjsp(jobs, machines, processing_time_min, processing_time_max, delta_processing_time, avg_assigned_machines, max_assigned_machines):
    """Generates a flexible job shop scheduling problem.

    Args:
        jobs : int
            Number of jobs.
        machines : int
            Number of machines.
        processing_time_min : int
            Minimum processing time of an operation. Default to 1.
        processing_time_max : int
            Maximum processing time of an operation. Default to 10.
        delta_processing_time : int
            Maximum gap of processing times within operations. Default to 3.
        avg_assigned_machines : float
            Average number of machines assigned to an operation. Default to 0.5 * machines.
        max_assigned_machines : float
            Maximum number of machines assigned to an operation. Default to 0.8 * machines.

    Returns:
        None
    """

    if avg_assigned_machines == None:
        avg_assigned_machines = .5 * machines

    if max_assigned_machines == None:
        max_assigned_machines = .8 * machines

    operations = machines
    total_operations = operations * jobs
    total_assigned_machines = avg_assigned_machines * total_operations

    if total_assigned_machines != int(total_assigned_machines):
        print('error in parameter value avg_assigned_machines. No such value possible!')
        return

    allocation_matrix = np.ones((jobs, operations), dtype=int)

    while np.sum(allocation_matrix) != total_assigned_machines:

        j = random.randrange(jobs)
        i = random.randrange(operations)

        if allocation_matrix[j, i] < int(max_assigned_machines):
            allocation_matrix[j, i] += 1

    with open('./Instances/data.txt', 'w') as f:

        f.write('{0}\t{1}\t{2}\n'.format(
            jobs, machines, avg_assigned_machines))
        for j in range(jobs):
            f.write('{0}'.format(len(allocation_matrix[j, :])))

            for i in range(len(allocation_matrix[j, :])):
                f.write('\t{0}'.format(allocation_matrix[j, i]))

                machine_list = [item+1 for item in range(machines)]
                processing_time = []

                for k in range(allocation_matrix[j, i]):
                    index = random.choice(range(len(machine_list)))
                    machine = machine_list.pop(index)

                    if k == 0:
                        processing_time.append(random.randint(
                            processing_time_min, processing_time_max))
                        f.write('\t{0}\t{1}'.format(
                            machine, processing_time[k]))
                    else:
                        processing_time.append(random.randint(max(processing_time_min, max(
                            processing_time) - delta_processing_time), min(processing_time_max, min(processing_time) + delta_processing_time)))
                        f.write('\t{0}\t{1}'.format(
                            machine, processing_time[k]))

            f.write("\n")

    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('jobs', type=int, help='Number of jobs.')
    parser.add_argument('machines', type=int, help='Number of machines.')
    parser.add_argument('-pmin',  '--processing_time_min',
                        type=int, default=1, help='Minimum processing time of a operation.')
    parser.add_argument('-pmax',  '--processing_time_max',
                        type=int, default=10, help='Maximum processing time of a operation.')
    parser.add_argument('-dp',  '--delta_processing_time',
                        type=int, default=3, help='Maximum gap of processing time within operations.')
    parser.add_argument('-am',  '--avg_assigned_machines',
                        type=float, help='Average number of machines assigned to a operation.')
    parser.add_argument('-mm',  '--max_assigned_machines',
                        type=float, help='Maximum number of machines assigned to a operation.')

    args = parser.parse_args()
    generate_fjsp(args.jobs, args.machines, args.processing_time_min, args.processing_time_max,
                  args.delta_processing_time, args.avg_assigned_machines, args.max_assigned_machines)
