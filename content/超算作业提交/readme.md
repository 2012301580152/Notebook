# 超算作业提交
## 常用命令

1. 作业提交 sbatch *.sbatch
2. 显示job信息 scontrol show job [jobid]
3. 节点状态查看 sinfo
4. 查看作业状态信息squeue
5. 命令取消任务scancel，命令格式为 scancel [jobID]

## 目录结构

## module使用
查看可用软件
module av // module avail
加载软件环境
module load anaconda/2.7
module list：显示用户已加载的编译器及库

module unload：卸载软件环境
示例：module unload anaconda/2.7
将anaconda/2.7从用户环境中卸载。

module help：帮助命令

1. 结点状态查看 sinfo

用户查看其节点的状态:

![slurm_submit1](http://hpc.whu.edu.cn/wp-content/uploads/2018/03/1.png)

其中，PARTITION 表示分区，NODES 表示结点数，NODELIST 为结点列表， STATE 表示结点运行状态。其中，idle 表示结点处于空闲状态，alloc 表示结 点已经分配了一个或多个作业。

2. 作业状态信息查看squeue

用户用其查看作业运行情况:

![slurm_submit2](http://hpc.whu.edu.cn/wp-content/uploads/2018/03/2.png)

其中，JOBID 表示任务 ID，Name 表示任务名称，USER 为用户，TIME 为已 运行时间，NODES 表示占用结点数，NODELIST 为任务运行的结点列表。

3. 交互式作业提交 srun

交互式提交作业：在 shell 窗口中执行srun 命令，主要命令格式如下：

srun [options] program

srun 常用选项srun 包括多个选项，其中最常用的选项主要有以下几个：

-n, –ntasks=number 指定要运行的任务数。请求为 number 个任务分配资源，默认为每个任务一 个处理器核。

-c, –cpus-per-task=ncpus 告知资源管理系统控制进程，作业的每个任务需要 ncpus 个处理器核。若 未指定此选项，则控制进程默认为每个任务分配一个处理器核。

-N, –nodes=minnodes[-maxnodes]  请求为作业至少分配 minnodes 个结点。调度器可能觉得在多于 minnodes 个 结点上运行作业。可以通过 maxnodes 限制最多分配的结点数目（例如“-N 2-4” 或“–nodes=2-4”）。最少和最多结点数目可以相同以指定特定的结点数目（例如， “-N 2”或“–nodes=2-2”将请求两个且仅两个结点）。分区的结点数目限制将覆盖 作业的请求。如果作业的结点限制超出了分区中配置的结点数目，作业将被拒绝。 如果没有指定-N，缺省行为是分配足够多的结点以满足-n 和-c 参数的需求。在 允许的限制范围内以及不延迟作业开始运行的前提下，作业将被分配尽可能多的 结点。

-p, –partition=partition name 在指定分区中分配资源。请使用 -p [hpxg|hpib|debug]指定所使用的分区。 -w, –nodelist=node name list 请求指定的结点名字列表。作业分配资源中将至少包含这些结点。列表可以 用逗号分隔的结点名或结点范围（如 n[0001-0005,0007,…]）指定，或者用文件名指定。如 果参数中包含“/”字符，则会被当作文件名。如果指定了最大结点数如-N 1-2，但 是文件中有多余 2 个结点，则请求列表中只使用前 2 个结点。

-x, –exclude=node name list 不要将指定的结点分配给作业。如果包含“/”字符，参数将被当作文件名。

srun 将把作业请求提交到控制进程，然后在远程结点上启动所有进程。如果资 源请求不能立即被满足， srun 将阻塞等待，直到资源可用以运行作业。如果指 定了–immediate 选项，则 srun 将在资源不是立即可用时终止。

-h, –help 若需使用 srun 更多选项，可通过“srun –h”或“srun –help”查看。

使用示例：在分区hpxg上运行5个任务 hostname：

$srun –p hpxg –n hostname

![slurm_submit3](http://hpc.whu.edu.cn/wp-content/uploads/2018/03/3.png)

4. 批处理作业 sbatch

批处理作业是指用户编写作业脚本，指定资源需求约束，提交后台执行作业。 提交批处理作业的命令为 sbatch，用户提交命令即返回命令行窗口，但此时作业在进入调度状态，在资源满足要求时，分配完计算结点之后，系统将在所分配的第一个计算结点（而不是登录结点）上加载执行用户的作业脚本。

批处理作业的脚本为一个文本文件，脚本第一行以“#!”字符开头，并制定脚 本文件的解释程序，如 sh，bash。由于计算节点为精简环境，只提供 sh 和 bash 的默认支持。

使用示例：例如用户的脚本名为 mybash.sh，内容如下：

#！/bin/bash

hostname

根据该脚本用户提交批处理作业，需要明确申请的资源为 hpxg 分区的 4 个 结点。

注意：需给该文本文件设置 mybash.sh 可执行权限，利用命令：

chmod +x mybash.sh

用户 sbatch 批处理命令如下：

sbatch –N 4 –p hpxg ./mybash.sh

计算开始后，工作目录中会生成以 slurm 开头的.out 文件为输出文件。更多选项，用户可以通过sbatch –help 命令查看。

5.结点资源抢占命令 salloc

该命令支持用户在提交作业前，抢占所需计算资源（此时开始计算所用机 时）。

使用示例salloc 提交方式如下：

首先申请资源，执行如下命令：

salloc –N 1

通过 squeue 查看相应的 jobID 为 15856293，结点为 n0121。用户可以选择如下方式，切换到结点n0121之后执行程序。

 

![slurm_submit4](http://hpc.whu.edu.cn/wp-content/uploads/2018/03/4.png)

6.任务取消 scancel

用户使用 scancel 命令取消自己的作业。命令格式如下：

scancel jobid

jobid 可通过 squeue获得。对于排队作业，取消作业将简单地把作业标记为 CANCELLED 状态而结束作业。对于运行中或挂起的作业，取消作业将终止作 业的所有作业步，包括批处理作业脚本，将作业标记为 CANCELLED 状态，并 回收分配给作业的结点。一般地，批处理作业将会马上终止；交互作业的 srun 进程将会感知到任务的退出而终止；抢占结点资源的 salloc 进程不会自动退出， 除非作业所执行的用户命令因作业或任务的结束而终止。但是在作业被取消时， 控制进程都会发送通知消息给分配资源的 srun 或 salloc 进程。用户可以选择 通过salloc的–kill-command选项设置在收到通知时向所执行的命令发送信号将 其终止。



## [MATLAB MDCS使用指南](http://hpc.whu.edu.cn/matlab_mdcs_submit/)

1. 拷贝/software/MATLAB/MDCS/matlab_mdcs_slurm.sh至您的工作目录
2. 编辑matlab_mdcs_slurm.sh，自定义以下参数：

```bash
# 需要计算的m文件所在目录
work_dir=”/project/xinming/examples/matlab-jobs/”
# 需要计算的m文件名，不需要加.m后缀
mfile=”name_of_m_file”
# 用于计算的Task数量
ntasks=15
# SLURM分区名
partition=”hpxg”
# 保存结果至mat文件
save_mat=”$mfile.mat”
# 是否开启Matlab警告提示
warning=”off”
# 填写账号
account=”$USER”
```

3. 提交MATLAB MDCS作业
```bash
$ ./matlab_mdcs_slurm.sh
```




4. 查询作业情况

```bash
$ squeue
```

# 多线程使用指南

当使用pthread、openmp等多线程程序，一般使用的是单个节点，多个核并行计算。
假设多线程的程序为program，则一般提交的任务的语法为：
**交互式**：
```bash
srun -c 8 program [args]
```
**脚本提交**：
multi.sbatch
```bash
`#!/bin/bash
#SBATCH -c 8program [args]
```
使用
```bash
sbatch multi.sbatch
```
进行提交。

其中-c 指定需要的核数，或者说是运算的线程数量。由于单节点的核数为16，该数量不要超过16。



使用sbatch提交脚本如下(mpitest.sbatch)：
```bash
#!/bin/bash
#SBATCH -n 10
#SBATCH -p hpib
srun --mpi=pmi2 -p hpib -n 10 mpitest
```
提交：
```bash
sbatch mpitest.sbatch
```